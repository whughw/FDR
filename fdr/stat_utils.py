import MySQLdb
from wordcloud import WordCloud
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import networkx as nx

class WeiboStat:

    def __init__(self, db_user, db_passwd, db_name, stop_word_path='./resources/stop_words.txt'):
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_name = db_name
        self.text = None
        self.stat = None
        self.stop_words = set(line.strip() for line in open(stop_word_path, encoding='utf-8'))

    def get_text(self, uid):
        self.text = ''
        db_conn = MySQLdb.connect(user=self.db_user, passwd=self.db_passwd, host='localhost', db=self.db_name, charset='utf8mb4')
        cursor = db_conn.cursor()
        cursor.execute('SELECT tweet, forwarding FROM Weibos WHERE user_ID=%s', (uid,))
        result = cursor.fetchall()
        for tweet, forwarding in result:
            self.text += tweet
            self.text += forwarding

    def word_stat(self):
        self.word_stat = {}
        word_list = list(jieba.cut(self.text))
        for word in word_list:
            if word in self.stop_words:
                continue
            if word in self.word_stat:
                self.word_stat[word] += 1
            else:
                self.word_stat[word] = 1

    def generate_word_cloud(self, pic_path=None, weibo_user_name=None):
        mask_img = np.array(Image.open('./resources/icons/person.png'))
        word_cloud = WordCloud(font_path='./resources/font.ttf', relative_scaling=.5, mask=mask_img,
                                background_color='white')
        word_cloud.generate_from_frequencies(self.word_stat)

        if (pic_path is not None) and (weibo_user_name is not None):
            plt.imshow(word_cloud, interpolation='bilinear')
            plt.axis('off')
            path = pic_path + '/' + weibo_user_name + '.jpg'
            plt.savefig(path)
        else:
            plt.axis('off')
            plt.imshow(word_cloud, interpolation='bilinear')
            plt.show()



class NetworkStat:

    def __init__(self, db_user, db_passwd, db_name):
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_name = db_name

    def generate_network(self, person_id, pic_path=None):
        db_conn = MySQLdb.connect(user=self.db_user, passwd=self.db_passwd, db=self.db_name)
        cursor = db_conn.cursor()
        G = nx.MultiDiGraph()
        node_labels = {}
        edge_labels = {}

        G.add_node(person_id)
        cursor.execute('SELECT name FROM Persons WHERE person_ID=%s', (person_id,))
        person_name = cursor.fetchone()[0]
        node_labels[person_id] = person_name

        cursor.execute('SELECT relation_type, person2_ID FROM Relations WHERE person1_ID=%s', (person_id,))
        result = cursor.fetchall()
        for relation_type, person2_id in result:
            G.add_node(person2_id)
            cursor.execute('SELECT name FROM Persons WHERE person_ID=%s', (person2_id,))
            person2_name = cursor.fetchone()[0]
            node_labels[person2_id] = person2_name
            G.add_edge(person_id, person2_id)
            edge_labels[(person_id, person2_id)] = relation_type

        cursor.execute('SELECT relation_type, person1_ID FROM Relations WHERE person2_ID=%s', (person_id,))
        result = cursor.fetchall()
        for relation_type, person1_id in result:
            G.add_node(person1_id)
            cursor.execute('SELECT name FROM Persons WHERE person_ID=%s', (person1_id,))
            person1_name = cursor.fetchone()[0]
            node_labels[person1_id] = person1_name
            G.add_edge(person1_id, person_id)
            edge_labels[(person1_id, person_id)] = relation_type

        nx.draw(G, nx.spring_layout(G), labels=node_labels)
        nx.draw_networkx_edge_labels(G, nx.spring_layout(G), edge_labels)
        plt.savefig('./data/network/' + person_id + '.jpg')
        plt.clf()
        db_conn.close()