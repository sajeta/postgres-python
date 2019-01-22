# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:55:20 2019

@author: marin
"""

#!/usr/bin/python
import psycopg2
from psycopg2.sql import SQL, Identifier
import config as cf
import load_excel as ex

#creates table in database. Name of the table and column names are passed as variables
def create_table(table_name, columns, conn):
    """ create tables in the PostgreSQL database"""
    try:
        cur = conn.cursor()
        cur.execute(SQL("CREATE TABLE {} ( {} INTEGER PRIMARY KEY, {} VARCHAR(100), {} VARCHAR(100), {} VARCHAR(10));").format(Identifier(table_name), Identifier(columns[0]), Identifier(columns[1]), Identifier(columns[2]), Identifier(columns[3]) ))
        # commit the changes
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
          
#inserts data to table
def fill_table(table_name, columns, data, conn):
    """ insert a new vendor into the vendors table """
    sql = SQL("INSERT INTO {}({},{},{},{}) VALUES(%s, %s, %s, %s);").format(Identifier(table_name), Identifier(columns[0]), Identifier(columns[1]), Identifier(columns[2]), Identifier(columns[3]))
    try:
        cur = conn.cursor()
        for row in data:
            values = []
            for c in row:
                values.append(c[1])
            # execute the INSERT statement
            cur.execute(sql, (int(values[0]), values[1], values[2], values[3]))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

#prints everything in table        
def get_table():
    """ query data from the vendors table """
    conn = None
    try:
        params = cf.config()
        tableInfo = cf.tableInfo()
        table_name = tableInfo["name"]
        
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute(SQL("SELECT * FROM {}").format(Identifier(table_name)))
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#connects to database, loads data from excel file, creates empty table and finally inserts data into table    
def run():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = cf.config()
        tableInfo = cf.tableInfo()
        table_name = tableInfo["name"]
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()
        
 # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        
        values, columns = ex.loadExcel()
        
        create_table(table_name, columns, conn)
        fill_table(table_name, columns, values, conn)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        
    