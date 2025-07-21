import os
import sqlite3

db_folder = "model/repository"
os.makedirs(db_folder, exist_ok=True)




def create_database():
    # اتصال
    connection = sqlite3.connect("user_db.sqlite")

    # ساخت جدول
    # عملیات ذخیره، ویرایش، حذف و انواع جستجو و گزارش
    cursor = connection.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS USERS
                   (
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
                   CREATE TABLE IF NOT EXISTS USER_PASSENGER
                   (
                       code         integer primary key,
                       name         text not null,
                       family       text not null,
                       phone_number text
                   )
                   """)

    connection.commit()

    # قطع اتصال
    cursor.close()
    connection.close()
