CREATE DATABASE IF NOT EXISTS FDR;

use FDR;

CREATE TABLE IF NOT EXISTS Persons(
    person_ID CHAR(36),
    name VARCHAR(20) DEFAULT NULL,
    last_meet_time DATETIME DEFAULT NULL,
    PRIMARY KEY (person_ID)
) DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Meets(
    meet_ID BIGINT UNSIGNED AUTO_INCREMENT,
    meet_time DATETIME,
    meet_place VARCHAR(255),
    person_ID CHAR(36) NOT NULL,
    PRIMARY KEY (meet_ID)
)DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Vectors(
    vector_ID BIGINT UNSIGNED AUTO_INCREMENT,
    vector BLOB NOT NULL,
    person_ID CHAR(36) NOT NULL,
    PRIMARY KEY (vector_ID)
) DEFAULT CHARSET=utf8;