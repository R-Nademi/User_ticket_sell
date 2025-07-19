import os
import sqlite3

db_folder = "model/repository"
os.makedirs(db_folder, exist_ok=True)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def create_database():

    connection = sqlite3.connect("tickets_db.sqlite")
    cursor = connection.cursor()


    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS USERS (
                   
                       code     integer primary key AUTOINCREMENT ,
                       name     text not null,
                       family   text not null,
                       username text not null unique,
                       password text not null,
                       role     text not null,
                       locked   tinyint default 0
                   )
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Patient (
                   
                       code         integer primary key,
                       name         text not null,
                       family       text not null,
                       phone_number text
                   )
                   """)

    connection.commit()


    cursor.close()
    connection.close()
