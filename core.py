import sqlite3
from sqlite3 import Error
from flask import Flask, g, render_template, request

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
        CREATE TABLE IF NOT EXISTS Messages (
            id INT PRIMARY KEY,
            handle TEXT NOT NULL,
            message TEXT NOT NULL
        );
    """ 
    g.message_db.cursor().executescript(cmd)
    g.message_db.close()
    
    return g.message_db


# insert a record to db
def insert_message(request):

    conn = sqlite3.connect("./db/message_db.sqlite")
    cur = conn.cursor()

    maxId = cur.execute("SELECT COUNT(*) FROM messages;").fetchone()

    msg = request.form['message']
    hdl = request.form['handle']  
    
    cmd = \
    f"""
        INSERT INTO messages
        VALUES ('{maxId[0] + 1}', '{msg}', '{hdl}');
    """ 
    if msg and hdl:
        cur.execute(cmd)
        conn.commit()
        conn.close() 

        return True
    else:
        conn.close()

        return False

def random_messages(n):
    conn = sqlite3.connect("./db/message_db.sqlite")
    cur = conn.cursor()

    cmd = \
    f"""
        SELECT *
        FROM messages ORDER BY RANDOM() LIMIT {n};
    """ 
    rdm_msg = cur.execute(cmd).fetchall()
    cur.close()

    return rdm_msg



