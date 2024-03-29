import requests
import os.path
import json
import csv

# Get the AirBnB listing data for France

def get_airbnb():
    url = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/air-bnb-listings/exports?where=column_19%20%3D%20%22France'
    response = requests.get(url)
    link = response.json()['links'][1]['href']
    data = requests.get(link, stream=True)
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "air_bnb_data.csv")
    with open(file_path, mode="wb") as file:
        for chunk in data.iter_content(chunk_size=512 * 1024):
            file.write(chunk)
    print("Download complete!") 
