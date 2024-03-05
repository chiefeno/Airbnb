from geopy.geocoders import Nominatim

# Create a geocoder object
geolocator = Nominatim(user_agent='my-application')

# Define the latitude and longitude
latitude = 48.87405135519706
longitude = 2.334464400546129

# Reverse geocode the coordinates
location = geolocator.reverse(f"{latitude}, {longitude}")

# Extract the zip code from the address
zip_code = location.raw['address']['postcode']

# Print the zip code
print(zip_code)