import requests
name='kenya'

url=f'https://restcountries.com/v3.1/name/{name}'

countries=requests.get(url).json()

print(countries[0]['name'])
print(list(countries[0].keys()).index('currencies'))
print(list(countries[0]['currencies']['KES']['symbol']))