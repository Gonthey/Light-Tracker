import sqlite3
import configparser
#First Run Setup
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("""DROP TABLE torrentindex;""")
sql_command = """
CREATE TABLE torrentindex (
ID INTEGER PRIMARY KEY,
name VARCHAR(100),
genre VARCHAR(30)
);"""
cursor.execute(sql_command)
connection.commit
connection.close
config = configparser.ConfigParser()
config['PATHS'] = {'TorrentPath': './Torrents'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)
