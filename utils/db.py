import sqlite3
import datetime

def init():
    connection = sqlite3.connect('/home/pi/BrYOUno/utils/database.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS errors
                 (id integer primary key, timestamp datetime NOT NULL, error text NOT NULL, info text, file text)''')
    c.execute('''CREATE TABLE IF NOT EXISTS actions
                 (id integer primary key, timestamp datetime NOT NULL, action text NOT NULL, info text NOT NULL)''')
    connection.commit()
    connection.close()
    #

def log_error(error, info, file):
    connection = sqlite3.connect('/home/pi/BrYOUno/utils/database.db')
    c = connection.cursor()
    c.execute('''INSERT INTO errors(timestamp,error,info,file) VALUES (?,?,?,?)''', (datetime.datetime.now(), error, info, file))
    connection.commit()
    connection.close()

def log_action(action, info):
    connection = sqlite3.connect('/home/pi/BrYOUno/utils/database.db')
    c = connection.cursor()
    c.execute('''INSERT INTO actions(timestamp,action,info) VALUES (?,?,?)''', (datetime.datetime.now(), action, info))
    connection.commit()
    connection.close()

if __name__ == "__main__":
    init()
