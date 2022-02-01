import sqlite3
from sqlite3 import Error
from flask import Flask, g, request

# create a database
def get_message_db():
    if 'message_db' not in g:
        try:
            g.message_db = sqlite3.connect("./db/message_db.sqlite")
            print(sqlite3.version)
        except Error as e:
            print(e)

    cmd = \
    f"""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            handle TEXT NOT NULL,
            message TEXT NOT NULL
        );
    """ 
    g.message_db.cursor().executescript(cmd)
    g.message_db.close()
    
    return g.message_db


# insert a record to db
def insert_message(request):
    
    cmd = \
    f"""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            handle TEXT NOT NULL,
            message TEXT NOT NULL
        );
    """ 
