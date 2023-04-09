#!/usr/bin/env python3
import db
import csv


def menu():
    connection= db.connect()
    db.create_tables(connection)
    # Read the CSV file and insert the data into the table
    with open('data_books.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            db.add_books(connection,row)
            
menu()