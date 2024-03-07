from air_bnb import get_airbnb
from get_companies_data import download_most_recent_company_file
from map_trick import map_zip_codes_and_cities
from insert import insert_csv_data



# execute all the functions 


def main():
    get_airbnb()
    filepath = download_most_recent_company_file()
    map_zip_codes_and_cities(filepath)
    insert_csv_data('air_bnb_data.csv', 'companies_city.csv')
    return('execution complete')



if __name__ == '__main__':
    main()