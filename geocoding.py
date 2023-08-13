#Geocoding Project made in python
#Geocoding is the process of converting addresses (like a street address) into geographic coordinates (like latitude and longitude)
#Taken API Key from https://locationiq.com/

#pip install requests
import requests
import random

location_list = ['bern',"atlanta","delhi","Delhi Public School","strawberry fields high school","new york","rome","berlin","los angeles","munich","zurich"]
random_location = random.choice(location_list)

url = "https://us1.locationiq.com/v1/search.php"

#you can use any address or just press enter
address = input("Input the address: ") or random_location

#API Key used here from https://locationiq.com/ its sensitive but still sharing it pls keep it private
private_token = "pk.ed002d4160b46a131e0b4e8bd141af64"

data = {
    'key': private_token,
    'q': address,
    'format': 'json'
}

response = requests.get(url, params=data)

latitude = response.json()[0]['lat']
longitude = response.json()[0]['lon']

print("The location is",address+".")
print(f"The latitude of the given address is: {latitude}")
print(f"The longitude of the given address is: {longitude}")
