import sqlite3
from sqlite3 import Error
from flask import Flask, g, render_template, request

# core methods

# create a database
def get_message_db():

    # check if 'message_db' exists, if not then establish one
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

    # create a table - 'Messages'
    g.message_db.cursor().executescript(cmd)
    g.message_db.close()
    
    return g.message_db


# insert a record to db
def insert_message(request):

    # connect to the db
    conn = sqlite3.connect("./db/message_db.sqlite")
    cur = conn.cursor()

    # find the rows in table for future usage
    maxId = cur.execute("SELECT COUNT(*) FROM messages;").fetchone()

    # get message and name contents submitted by user
    msg = request.form['message']
    hdl = request.form['handle']  
    
    cmd = \
    f"""
        INSERT INTO messages
        VALUES ('{maxId[0] + 1}', '{msg}', '{hdl}');
    """

    # if user filled both message and name, write into db 
    if msg and hdl:
        cur.execute(cmd)
        conn.commit()
        conn.close() 

        return True
    else:
        conn.close()

        return False

# read n messages randomly from table
def random_messages(n):
    # connect to db
    conn = sqlite3.connect("./db/message_db.sqlite")
    cur = conn.cursor()

    cmd = \
    f"""
        SELECT *
        FROM messages ORDER BY RANDOM() LIMIT {n};
    """ 
    # randomly choosing [n] records from table
    rdm_msg = cur.execute(cmd).fetchall()
    cur.close()

    return rdm_msg



