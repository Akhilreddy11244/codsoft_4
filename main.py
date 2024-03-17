import requests
from requests import Response

city = input("Enter the city name: ")

print("Displaying waether report for "+city)

url = 'https://wttr.in/{}'.format(city)

res: Response = requests.get(url)

print(res.text)