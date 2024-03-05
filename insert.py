import os
import json
from datetime import datetime
from db_config import DB_HOST, DB_NAME, DB_PORT
import pandas as pd
import psycopg2
from create_insert_statements import create_listing_table, listing_table_insert


# Read the first CSV file
df1 = pd.read_csv('air_bnb_data.csv', delimiter=';')

# Read the second CSV file 
df2 = pd.read_csv('companies_city.csv')

# Group the company data by city and create an array of JSON objects for each city
df2_arranged = df2.groupby('city').apply(lambda x: x[['id', 'address', 'zip', 'created_at']].to_dict('records')).reset_index()
df2_arranged.columns = ['city', 'companies']

# Perform the inner join based on the common 'id' column
merged_df = pd.merge(df1, df2_arranged, left_on='city', right_on='city', how='inner')

# Rename "column 19" to "country"
merged_df = merged_df.rename(columns={"column_19": "country", "column_20": "full_location"})


print(merged_df.columns.tolist())
# drop extra column

# Filter the merged data to include only rows where the country is France
merged_df_france = merged_df[merged_df['country'] == 'France']





# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host= DB_HOST,
    database= DB_NAME,
    port = DB_PORT
)


# drop if exist, create table and insert it in the database
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS airbnb")
cur.execute(create_listing_table)

for _, row in merged_df_france.iterrows():
    last_review = None if pd.isnull(row['last_review']) or row['last_review'] == 'NaN' else datetime.strptime(row['last_review'], "%Y-%m-%d").date()
    values = (
        row['id'],
        row['name'],
        row['host_id'],
        row['neighbourhood'],
        row['room_type'],
        row['column_10'],
        row['minimum_nights'],
        row['number_of_reviews'],
        last_review,
        row['reviews_per_month'],
        row['calculated_host_listings_count'],
        row['availability_365'],
        row['updated_date'],
        row['city'],
        row['country'],
        row['coordinates'],
        row['full_location'],
        json.dumps(row['companies']) 
    )
    cur.execute(listing_table_insert, values)

conn.commit()
cur.close()
conn.close()
