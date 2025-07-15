import sqlite3


def create_database():
    # اتصال
    connection = sqlite3.connect("ticket.db.sqlite")

    # ساخت جدول
    # عملیات ذخیره، ویرایش، حذف و انواع جستجو و گزارش
    cursor = connection.cursor()

    cursor.execute(""",
                   CREATE TABLE IF NOT EXISTS Ticket,
                   (
                       code     integer primary key AUTOINCREMENT
                       name     text not null
                       family   text not null
                       username text not null unique
                       password text not null
                       role     text not null
                       locked   tinyint default 0
                   )
                   """)

    cursor.execute(""",
                   CREATE TABLE IF NOT EXISTS Patient
                   (
                       code        integer primary key,
                       name       text not null,
                       family      text not null,
                       phone_number text
                   )
                   """)

    connection.commit()

    # قطع اتصال
    cursor.close()
    connection.close()
