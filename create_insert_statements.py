# CREATE TABLE STATEMENTS
create_listing_table = (""" CREATE TABLE airbnb (
                                                            id INTEGER,
                                                            name VARCHAR,
                                                            host_id INTEGER,
                                                            neighbourhood VARCHAR,
                                                            room_type VARCHAR,
                                                            column_10 INTEGER,
                                                            minimum_nights INTEGER,
                                                            number_of_reviews INTEGER,
                                                            last_review DATE,
                                                            reviews_per_month DECIMAL,
                                                            calculated_host_listings_count INTEGER,
                                                            availability_365 INTEGER,
                                                            updated_date DATE,
                                                            city VARCHAR,
                                                            country VARCHAR,
                                                            coordinates VARCHAR,
                                                            full_location VARCHAR,
                                                            companies JSON
                                                            );
                                                  
""")




# INSERT STATEMENTS
listing_table_insert = ("""INSERT INTO airbnb(id, name, host_id, neighbourhood, room_type, column_10, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365, updated_date, city, country, coordinates, full_location, companies)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        ON CONFLICT
                        DO NOTHING;
""")