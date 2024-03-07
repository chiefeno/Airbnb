import os
import json
import csv
from datetime import datetime
from db_config import DB_HOST, DB_NAME, DB_PORT
import pandas as pd
import psycopg2
from create_insert_statements import create_listing_table, create_company_table, listing_table_insert, company_table_insert



def insert_csv_data(csv_file1, csv_file2):
    

    # Establish a connection to the database
    conn = psycopg2.connect(
    host= DB_HOST,
    database= DB_NAME,
    port = DB_PORT
)

    cur = conn.cursor()
    
    try:
        # Execute the CREATE TABLE statements
        cur.execute(create_listing_table)
        cur.execute(create_company_table)
        conn.commit()

        
        # Insert data from CSV file 1 into the listing table
        with open(csv_file1, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            cur.executemany(listing_table_insert, reader)
            conn.commit()

        # Insert data from CSV file 2 into the company table
        with open(csv_file2, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            cur.executemany(company_table_insert, reader)
            conn.commit()

        print("Data inserted successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error inserting data:", error)
    finally:
        # Close the database connection
        if cur:
            cur.close()
        if conn:
            conn.close()
