import requests

# setting number of fake data for each table
NUMBER_OF_USERS = 50
NUMBER_OF_PRODUCTS = 50
NUMBER_OF_ORDERS = 1000


# getting some fake product data from an API
products = requests.get('https://fakestoreapi.com/products').json()
TITLES = [product['title'] for product in products]
PRICES = [product['price'] for product in products]

# getting some fake names from an API
users = requests.get('https://fakestoreapi.com/users').json()
FIRST_NAMES = [user['name']['firstname'] for user in users]
LAST_NAMES = [user['name']['lastname'] for user in users]

