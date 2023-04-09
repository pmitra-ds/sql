# create the books database with sqlite3 from the books csv file

import csv
import sqlite3



CREATE_TABLES= "CREATE TABLE IF NOT EXISTS BOOKS (bookid INTEGER,title TEXT,author TEXT,category TEXT,status TEXT)"
INSERT_BOOK = "INSERT INTO BOOKS(bookid,title,author,category,status) VALUES (?,?,?,?,?);"
GET_BY_BOOK = "SELECT * FROM BOOKS WHERE title =?;"
GET_BY_AUTHOR = "SELECT * FROM BOOKS WHERE author =?;"
GET_BY_CATEGORY = "SELECT * FROM BOOKS WHERE category =?;"
COUNT_CATEGORY = 'SELECT category, COUNT(*) FROM BOOKS GROUP BY category'
## functions to create and operatee the database

def connect():
    return sqlite3.connect('books_db.db')
    
    
def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLES)
        
        
        
def add_books(connection,row):
    with connection:
        connection.execute(INSERT_BOOK,row)
        
        
        
def get_by_bookname(connection,title):
    with connection:
        return connection.execute(GET_BY_BOOK,(title,)).fetchall()


def get_by_authorname(connection,author):
    with connection:
        return connection.execute(GET_BY_AUTHOR,(author,)).fetchall()


       
def get_by_category(connection,category):
    with connection:
        return connection.execute(GET_BY_CATEGORY,(category,)).fetchall()

def count_by_category(connection):
    with connection:
        return connection.execute(COUNT_CATEGORY)
       
    
