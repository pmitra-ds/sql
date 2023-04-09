#!/usr/bin/env python3
import db
import csv


MENU_PROMPT = """
--- WELCOME TO THE LIBRARY DATABASE---
Please choose one of these options
1. Navigate categories
2. Search by book name
3. Search by author
4.exit    
                  
Your Selection:
"""
               



def menu():
    connection= db.connect()
    db.create_tables(connection)
    # user input
    while(user_input := input(MENU_PROMPT)) != "4":
        
        if user_input == "1":
            result = db.count_by_category(connection)
            print ("Number of books in each category:-----")
            for row in result:
                print (row)
        elif user_input == "2":
            try:
                bookname = input("Enter book title: ")
                out1 = db.get_by_bookname(connection,bookname)
                for out in out1:
                    print (f'Title: {out[1]}, Author: {out[2]},Type: {out[3]}, Status: {out[4]}')
            except:
                print ('This book does not exist, please try again!')
        elif user_input== "3":
            try:
                a_n = input("Enter author name: ")
                out2 = db.get_by_authorname(connection,a_n)
                for out in out2:
                    print (f'Title: {out[1]}, Author: {out[2]},Type: {out[3]}, Status: {out[4]}')
            except:
                print ('The author does not exist, please try again!')
        
        else:
            print('Invalid Input')
     


    
menu()



       
        
        