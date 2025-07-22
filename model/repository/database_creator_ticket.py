import sqlite3


def create_database():
    # اتصال
    connection = sqlite3.connect("ticket_db.sqlite")

    # ساخت جدول
    # عملیات ذخیره، ویرایش، حذف و انواع جستجو و گزارش
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS tickets")

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS USERS  (
                   
                       code     integer primary key AUTOINCREMENT 
                       "name"     text not null,
                       family   text not null,
                       birth_date text not null unique,
                       origin text  not null,
                       destination   text not null,
                       start_date_time text not null,
                       end_date_time text not null,
                       ticket_type text not null,
                       seat_number text not null,
                       price text not null,
                       
                   )
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS TICKET (
                   
                       code         integer primary key,
                       "name"         text not null,
                       family       text not null,
                       origin       text not null,
                       destination   text not null,
                       
                      );
                   """)

    connection.commit()

    # قطع اتصال
    cursor.close()
    connection.close()


