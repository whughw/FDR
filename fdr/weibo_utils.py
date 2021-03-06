# -*-coding:utf-8-*-
import traceback
import MySQLdb
from datetime import datetime
from bs4 import BeautifulSoup
import random
import time
import re
import weibo
import requests
import time
import json
import math
import pandas as pd
from stat_utils import WeiboStat


# class WeiboClient:

#     def __init__(self, cookie=None, db_user=None, db_passwd=None, db_name=None,
#                 app_key='3396385405', app_secret='b333b2531b57d41456a885271e8c2630',
#                 app_redirect_uri='https://api.weibo.com/oauth2/default.html',
#                 app_user='824476660@qq.com', app_passwd='zhu19970316'):
#         self.cookie = cookie
#         self.agents = [
#             "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
#             "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
#             "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
#             "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
#             "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
#             "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
#             "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
#             "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
#             "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
#             "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
#             "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
#             "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
#             "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
#             "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
#             "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#             "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#             ]
#         self.db_user = db_user
#         self.db_passwd = db_passwd
#         self.db_name = db_name
#         self.app_key = app_key
#         self.app_secret = app_secret
#         self.app_redirect_uri = app_redirect_uri
#         self.app_user = app_user
#         self.app_passwd = app_passwd
#         self.db_conn = MySQLdb.connect(user=self.db_user, passwd=self.db_passwd, host='localhost', db=self.db_name, charset='utf8mb4')
#         self.client = weibo.Client(self.app_key, self.app_secret, self.app_redirect_uri,
#                                 username=self.app_user, password=self.app_passwd)

#     def __del__(self):
#         self.db_conn.close()

#     def get_weibo(self, uid_list):
#         cursor = self.db_conn.cursor()
#         try:
#             for uid in uid_list: #len(self.Id_List)
#                 UA = random.choice(self.agents)
#                 header = {'User-Agen': UA}
#                 #print(uid)
#                 url = 'http://weibo.cn/u/%s' % uid
#                 html = requests.get(url, cookies=self.cookie, headers=header)
#                 user_name = BeautifulSoup(html.text, 'lxml').find('div', class_='ut').find('span', class_='ctt').get_text().split('?')[0].split()[0]
#                 #print(user_name)
#                 if BeautifulSoup(html.text, 'lxml').find('div', class_='pa', id='pagelist') != None:
#                     num = int(BeautifulSoup(html.text, 'lxml').find('div', class_='pa', id='pagelist').find_all('input')[0]['value'])
#                 else:
#                     num = 1
#                 pattern = r'\d+'

#                 for n in range(1, num+1):
#                     print('{0}: {1}/{2} pages'.format(user_name, n, num))
#                     url2 = 'http://weibo.cn/u/%s?page=%s' % (uid, n)
#                     html2 = requests.get(url2, cookies=self.cookie, headers=header, timeout = 10)
#                     time.sleep(3)
#                     soup2 = BeautifulSoup(html2.text, 'lxml').find_all('div', class_='c')
#                     if len(soup2) > 3:
#                         for i in range(1, len(soup2) - 2):
#                             div_ls = soup2[i].find_all('div')
#                             if len(div_ls) == 3:
#                                 tweet = div_ls[2].get_text().split('??')[0][5:]
#                                 tweet = tweet.encode('gbk', 'ignore')
#                                 tweet = str(tweet.decode('gbk', 'ignore'))
#                                 forwarding = div_ls[0].find('span', class_='ctt').get_text().replace('[^\u0000-\uFFFF]', '')
#                                 if div_ls[0].find('span', class_='ctt').find('a') != None:
#                                     a_l = div_ls[0].find('span', class_='ctt').find_all('a')
#                                     for a1 in a_l:
#                                         if a1.get_text() == '全文':
#                                             href = 'https://weibo.cn' + a1['href']
#                                             req = requests.get(href, cookies=self.cookie, headers=header)
#                                             time.sleep(2)
#                                             forwarding = BeautifulSoup(req.text, 'lxml').find_all('div', class_='c')[2].find('span', class_='ctt').get_text()
#                                             break
#                                 all_num = div_ls[2].find_all('a')
#                                 if all_num[-1].get_text() == '收藏':
#                                     num_likes = int(re.findall(pattern, all_num[-4].get_text())[0])
#                                     num_forwardings = int(re.findall(pattern, all_num[-3].get_text())[0])
#                                     num_comments = int(re.findall(pattern, all_num[-2].get_text())[0])
#                                 else:
#                                     num_likes = int(re.findall(pattern, all_num[-5].get_text())[0])
#                                     num_forwardings = int(re.findall(pattern, all_num[-4].get_text())[0])
#                                     num_comments = int(re.findall(pattern, all_num[-3].get_text())[0])
#                                 #print(tweet)
#                                 picture = 0
#                                 videos = 0
#                                 zf = 1
#                                 if tweet == '转发微博' or tweet.split('//@')[0] == '转发微博':
#                                     luozhuan = 1
#                                 else: luozhuan = 0
#                                 others = div_ls[2].find('span', class_='ct').get_text().split('?')
#                                 if others[0]:
#                                     post_time = str(others[0])
#                             elif len(div_ls) == 1:
#                                 tweet = div_ls[0].find('span',class_='ctt').get_text()
#                                 tweet = tweet.encode('gbk', 'ignore')
#                                 tweet = str(tweet.decode('gbk', 'ignore'))
#                                 forwarding = ''
#                                 if div_ls[0].find('span', class_='ctt').find('a') != None:
#                                     a_l = div_ls[0].find('span', class_='ctt').find_all('a')
#                                     for a1 in a_l:
#                                         if a1.get_text() == '全文':
#                                             href = 'https://weibo.cn' + a1['href']
#                                             req = requests.get(href, cookies=self.cookie, headers=header)
#                                             tweet = BeautifulSoup(req.text, 'lxml').find_all('div', class_='c')[2].find('span', class_='ctt').get_text()
#                                             break
#                                 all_num = div_ls[0].find_all('a')
#                                 if all_num[-1].get_text() == '收藏':
#                                     num_likes = int(re.findall(pattern, all_num[-4].get_text())[0])
#                                     num_forwardings = int(re.findall(pattern, all_num[-3].get_text())[0])
#                                     num_comments = int(re.findall(pattern, all_num[-2].get_text())[0])
#                                 else:
#                                     num_likes = int(re.findall(pattern, all_num[-5].get_text())[0])
#                                     num_forwardings = int(re.findall(pattern, all_num[-4].get_text())[0])
#                                     num_comments = int(re.findall(pattern, all_num[-3].get_text())[0])
#                                 #print(tweet)
#                                 picture = 0
#                                 if re.findall('秒拍视频',tweet):
#                                     videos = 1
#                                 else:
#                                     videos = 0
#                                 zf = 0
#                                 luozhuan = 0
#                                 others = div_ls[0].find('span', class_='ct').get_text().split('?')
#                                 if others[0]:
#                                     post_time = str(others[0])

#                             elif len(div_ls) == 2:
#                                 z = div_ls[1].find_all('span')
#                                 if len(z)>=2:
#                                     zf = 1
#                                     tweet = div_ls[1].get_text().split('??')[0][5:]
#                                     tweet = tweet.encode('gbk', 'ignore')
#                                     tweet = str(tweet.decode('gbk', 'ignore'))
#                                     forwarding = div_ls[0].find('span', class_='ctt').get_text().replace('[^\u0000-\uFFFF]', '')
#                                     all_num = div_ls[1].find_all('a')
#                                     if div_ls[0].find('span', class_='ctt').find('a') != None:
#                                         a_l = div_ls[0].find('span', class_='ctt').find_all('a')
#                                         for a1 in a_l:
#                                             if a1.get_text() == '全文':
#                                                 href = 'https://weibo.cn' + a1['href']
#                                                 req = requests.get(href, cookies=self.cookie, headers=header)
#                                                 forwarding = BeautifulSoup(req.text, 'lxml').find_all('div', class_='c')[2].find('span', class_='ctt').get_text()
#                                                 break
#                                     if all_num[-1].get_text() == '收藏':
#                                         num_likes = int(re.findall(pattern, all_num[-4].get_text())[0])
#                                         num_forwardings = int(re.findall(pattern, all_num[-3].get_text())[0])
#                                         num_comments = int(re.findall(pattern, all_num[-2].get_text())[0])
#                                     else:
#                                         num_likes = int(re.findall(pattern, all_num[-5].get_text())[0])
#                                         num_forwardings = int(re.findall(pattern, all_num[-4].get_text())[0])
#                                         num_comments = int(re.findall(pattern, all_num[-3].get_text())[0])
#                                     #print(tweet)
#                                     if tweet == '转发微博' or tweet.split('//@')[0] == '转发微博':
#                                         luozhuan = 1
#                                     else:
#                                         luozhuan = 0
#                                     videos = 0
#                                     picture = 0
#                                 else:
#                                     zf = 0
#                                     luozhuan = 0
#                                     str_t = div_ls[0].find('span', class_='ctt').get_text()
#                                     tweet = str_t.encode('gbk', 'ignore')
#                                     tweet = str(tweet.decode('gbk', 'ignore'))
#                                     forwarding = ''
#                                     if div_ls[0].find('span', class_='ctt').find('a') != None:
#                                         a_l = div_ls[0].find('span', class_='ctt').find_all('a')
#                                         for a1 in a_l:
#                                             if a1.get_text() == '全文':
#                                                 href = 'https://weibo.cn' + a1['href']
#                                                 req = requests.get(href, cookies=self.cookie, headers=header, timeout=10)
#                                                 tweet = BeautifulSoup(req.text, 'lxml').find_all('div', class_='c')[2].find('span', class_='ctt').get_text()
#                                                 break
#                                     all_num = div_ls[1].find_all('a')
#                                     if all_num[-1].get_text() == '收藏':
#                                         num_likes = int(re.findall(pattern, all_num[-4].get_text())[0])
#                                         num_forwardings = int(re.findall(pattern, all_num[-3].get_text())[0])
#                                         num_comments = int(re.findall(pattern, all_num[-2].get_text())[0])
#                                     else:
#                                         num_likes = int(re.findall(pattern, all_num[-5].get_text())[0])
#                                         num_forwardings = int(re.findall(pattern, all_num[-4].get_text())[0])
#                                         num_comments = int(re.findall(pattern, all_num[-3].get_text())[0])
#                                     #print(tweet)
#                                     videos = 0
#                                     picture = 1

#                                 others = div_ls[1].find('span', class_='ct').get_text().split('?')
#                                 if others[0]:
#                                     post_time = str(others[0])
#                             else:
#                                 continue

#                             sql = 'INSERT INTO Weibos (`user_id`, `user_name`, `tweet`,  `forwarding`,`num_likes`,`num_forwardings`,\
#                                 `num_comments`,`post_time`) VALUES ( %(user_id)s, %(user_name)s, %(tweet)s, %(forwarding)s, %(num_likes)s,\
#                                  %(num_forwardings)s, %(num_comments)s, %(post_time)s)'
#                             value = {
#                                 'user_id': uid,
#                                 'user_name': user_name,
#                                 'tweet': tweet,
#                                 'forwarding': forwarding,
#                                 'num_likes': num_likes,
#                                 'num_forwardings' : num_forwardings,
#                                 'num_comments': num_comments,
#                                 'post_time': post_time
#                             }
#                             cursor.execute(sql, value)
#                             self.db_conn.commit()
#                 print('{0}: all pages done'.format(user_name))
#         except Exception as e:
#             print("Error: ", e)
#             traceback.print_exc()

#     def get_uid(self, nick_name):
#         try:
#             uid = self.client.get('users/show', screen_name=nick_name)['idstr']
#             return uid
#         except Exception as e:
#             print('Error: user does not exist!')
#             return None

#     def save_info(self, person_name, nick_name, uid):
#         cursor = self.db_conn.cursor()
#         cursor.execute('SELECT person_ID FROM Persons WHERE name=%s', (person_name,))
#         result = cursor.fetchall()
#         if len(result) == 0:
#             print('Error: person does not exist')
#             return False
#         person_id = result[0][0]
#         cursor.execute('INSERT INTO WeiboAccounts (person_ID, weibo_name, weibo_uid) VALUES (%s, %s, %s)',
#                         (person_id, nick_name, uid))
#         self.db_conn.commit()
#         return True



class WeiboCrawler():

    headers = {'Accept':'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate, br',
               'Accept-Language':'zh-CN,zh;q=0.9',
               'Host':'m.weibo.cn',
               'Referer':'https://m.weibo.cn/',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; KNT-UL10 Build/HUAWEIKNT-UL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.0.0 Mobile Safari/537.36'
               }

    def __init__(self, db_login,
                app_key='3396385405', app_secret='b333b2531b57d41456a885271e8c2630',
                app_redirect_uri='https://api.weibo.com/oauth2/default.html',
                app_user='824476660@qq.com', app_passwd='zhu19970316'):
        self.db_login = db_login
        api_addr = 'http://webapi.http.zhimacangku.com/getip?num=15&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
        try:
            self.proxygetter = requests.get(api_addr , timeout = 5)
        except:
            pass
        self.ip_list = self.proxygetter.text.splitlines()
        if (self.proxygetter.text[0] == "{"):
            reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
            whitelist = reip.findall(self.proxygetter.text)
            print(whitelist[0] + "未被添加白名单, 正在添加...")
            try:
                requests.get("http://web.http.cnapi.cc/index/index/save_white?neek=47525&appkey=334504bcbdd380c4a4cb5c04ed62aa3e&white=" + whitelist[0],timeout = 5)
                self.proxygetter = requests.get(api_addr, timeout = 5)
            except:
                pass
            self.iplist = self.proxygetter.text.splitlines()
        self.weibo_client = weibo.Client(app_key, app_secret, app_redirect_uri,
                                username=app_user, password=app_passwd)


    def get_content(self,URL):
        htm = ''
        try:
            for t in range(1,4):
                if len(htm)< 20:
                    time.sleep(0.2)
                    proxyip = random.choice(self.ip_list)
                    proxydict = {'http': 'http://' + proxyip}
                    print("正在使用代理", proxydict)
                    try:
                        htm = requests.get(URL,headers = self.headers,proxies=proxydict,timeout=5).text
                    except:
                        print("Error")
                else:
                    break
        except:
            time.sleep(30)
        return htm


    def DeliterContent(self,contex):
        context = re.sub(r'\u200b','',contex)
        context = re.sub(r'<span class="url-icon">', '', context)
        context = re.sub(r'</span>', '', context)
        context = re.sub(r'<img src="//h5.sinaimg.cn/m/emoticon/icon/.*png" style="width:1em;height:1em;" alt="\[.*\]">', '', context)
        context = re.sub(r'<a href="/status/\d*">','',context)
        context = re.sub(r'<a class=\'k\' href=\'https://m.weibo.cn/k/.*?from=feed\'>#','',context)
        context = re.sub(r'</\w*>', '', context)
        if context.find('<a href=')!=-1:
            context = re.sub('<a.*>@','',context)
        context = re.sub(r'</\w*>', '', context)
        if len(context) ==0:
            context = re.sub(r'[^\u4e00-\u9fa5\|，！？。]','',contex)

        return context

    def get_uid(self, nick_name):
        try:
            uid = self.weibo_client.get('users/show', screen_name=nick_name)['idstr']
            return str(uid)
        except Exception as e:
            return ''

    def get_weibos(self, uid, progress_queue=None, max_pages=None):

        weibolist = []
        starturl = 'https://m.weibo.cn/api/container/getIndex?uid={uid1}&luicode=10000011&type=all&containerid=107603{uid2}&page={p}'.format(uid1=uid, uid2=uid, p=1)
        #proxyip = random.choice(self.ip_list)
        #proxydict = {'http': 'http://' + proxyip}
        #print("A正在使用代理", proxydict)
        try:
            html = requests.get(starturl, headers=self.headers, timeout = 8).text
        except:
            pass
        time.sleep(0.3)
        jsondata = json.loads(html)
        try:
            total = jsondata['data']['cardlistInfo']['total']  # 帖子总数
            t_p = math.ceil(int(total / 10))+1
            # t_p =5
        except:
            t_p = 2

        if max_pages is not None and t_p > max_pages:
            t_p = max_pages

        for i in range(1,t_p+1):
            url = 'https://m.weibo.cn/api/container/getIndex?uid={uid1}&luicode=10000011&type=all&containerid=107603{uid2}&page={p}'.format(uid1=uid, uid2=uid, p=i)
            try:
                html = self.get_content(url)
            except:
                pass

            if progress_queue is not None:
                progress_queue.put((i-1, t_p))
            else:
                print('第{i}页，总页数{t}'.format(i = i,t = t_p))

            try:
                jsondata = json.loads(html)
                cardlist = jsondata['data']['cards']
            except Exception as e:
                print(e)
                cardlist = []

            for cards in cardlist:
                weibodict = {}
                try:
                    data = cards['mblog']
                except:
                    continue

                nickname = description = follow_count = followers_count = statuses_count = text = created_at = uid = bid =source=forward =commentcount =attitudescount =''
                try:
                    nickname = data['user']['screen_name'] #博主
                except:
                    pass
                try:
                    description = data['user']['description'] #简介
                except:
                    pass
                try:
                    follow_count = data['user']['follow_count'] #关注数
                except:
                    pass
                try:
                    followers_count = data['user']['followers_count'] #粉丝数
                except:
                    pass
                try:
                    statuses_count = data['user']['statuses_count'] #微博数
                except:
                    pass
                try:
                    text = data['text']#博文
                    # text = self.DeliterContent(text)
                    text = BeautifulSoup(text,'lxml').text
                except:
                    pass
                try:
                    created_at = data['created_at'] #发布时间
                except:
                    pass
                try:
                    uid = data['user']['id']
                except:
                    pass
                try:
                    bid = data['bid']
                except:
                    pass
                weibourl = 'http://weibo.com/{uid}/{bid}'.format(uid=uid, bid=bid) #博文独立网址
                try:
                    source = data['source'] #发布终端
                except:
                    pass
                try:
                    forward = data['reposts_count'] #转发数
                except:
                    pass
                try:
                    commentcount = data['comments_count'] #评论数
                except:
                    pass
                try:
                    attitudescount = data['attitudes_count'] #点赞数
                except:
                    pass


                tusername = t_bozhu = tweibourl = ttext = tcreated_time = t_source = t_forward = t_commentcount = t_attitudescount =''
                try:
                    retweeteddata = data['retweeted_status'] #转发的原微博
                    tusername = retweeteddata['user']['screen_name'] #转发博主名称
                    tuid = retweeteddata['user']['id']
                    t_bozhu= 'https://weibo.com/horsehorse?refer_flag={}_'.format(tuid) #转发博主主页
                    tbid = retweeteddata['bid']
                    ttext = retweeteddata['text']  # 转发博文内容
                    # ttext = self.DeliterContent(ttext)
                    ttext = BeautifulSoup(ttext,'lxml').text
                    tcreated_time = retweeteddata['created_at']  # 转发博文时间
                    tweibourl= 'http://weibo.com/{uid}/{bid}'.format(uid=tuid, bid=tbid) #转发博文独立网址
                    t_source = retweeteddata['source']#转发博文终端
                    t_forward = retweeteddata['reposts_count']#转发转发数
                    t_commentcount = retweeteddata['comments_count']#转发评论数
                    t_attitudescount = retweeteddata['attitudes_count']#转发点赞数
                except:
                    pass

                weibodict['uid'] = uid
                weibodict['博主'] = nickname
                weibodict['简介'] = description
                weibodict['关注数'] = follow_count
                weibodict['粉丝数'] = followers_count
                weibodict['微博数'] = total
                weibodict['博文'] = text
                weibodict['发布时间'] = created_at
                weibodict['博文独立网址'] = weibourl
                weibodict['发布终端'] = source
                weibodict['转发数'] = forward
                weibodict['评论数'] = commentcount
                weibodict['点赞数'] = attitudescount

                weibodict['转发博主名称'] = tusername
                weibodict['转发博主主页'] = t_bozhu
                weibodict['转发博文内容'] = ttext
                weibodict['转发博文时间'] = tcreated_time
                weibodict['转发博文独立网址'] = tweibourl
                weibodict['转发博文终端'] = t_source
                weibodict['转发转发数'] = t_forward
                weibodict['转发评论数'] = t_commentcount
                weibodict['转发点赞数'] = t_attitudescount
                # print(weibodict)
                weibolist.append(weibodict)

        if progress_queue is not None:
            progress_queue.put((t_p+1, t_p))
        return weibolist

    def export_to_excel(self, data, file_name):
        writer = pd.ExcelWriter('{}.xlsx'.format(file_name))
        df = pd.DataFrame(data)
        df.to_excel(writer, file_name,
                    columns=['博主', '简介', '关注数', '粉丝数', '微博数', '博文', '发布时间', '博文独立网址', '发布终端', '转发数', '评论数', '点赞数',
                             '转发博主名称', '转发博主主页', '转发博文内容', '转发博文时间', '转发博文独立网址', '转发博文终端', '转发转发数', '转发评论数', '转发点赞数'],
                    index=False)
        writer.save()
        writer.close()

    def export_to_database(self, data):
        db_conn = MySQLdb.connect(user=self.db_login['user'], passwd=self.db_login['passwd'], db=self.db_login['db'])
        db_conn.set_character_set('utf8')
        cursor = db_conn.cursor()
        # cursor.execute('SET NAMES utf8;')
        # cursor.execute('SET CHARACTER SET utf8;')
        # cursor.execute('SET character_set_connection=utf8;')
        cursor.execute('DELETE FROM Weibos WHERE user_ID=%s', (data[0]['uid'],))
        for weibo in data:
            sql = 'INSERT INTO Weibos (`user_id`, `user_name`, `tweet`,  `forwarding`,`num_likes`,`num_forwardings`,\
                                `num_comments`,`post_time`) VALUES ( %(user_id)s, %(user_name)s, %(tweet)s, %(forwarding)s, %(num_likes)s,\
                    %(num_forwardings)s, %(num_comments)s, %(post_time)s)'
            value = {
                'user_id': weibo['uid'],
                'user_name': weibo['博主'],
                'tweet': str(weibo['博文'].encode('gbk', 'ignore').decode('gbk', 'ignore')),
                'forwarding': str(weibo['转发博文内容'].encode('gbk', 'ignore').decode('gbk', 'ignore')),
                'num_likes': weibo['点赞数'],
                'num_forwardings' : weibo['转发数'],
                'num_comments': weibo['评论数'],
                'post_time': weibo['发布时间']
            }
            cursor.execute(sql, value)
        db_conn.commit()
        db_conn.close()
