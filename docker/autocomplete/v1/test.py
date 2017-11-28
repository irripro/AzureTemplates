import json
from pprint import pprint

products = json.load(open('products.json'))
productnames = []

for product in products:
    productnames.append(product['name'])

productnames_json = json.dumps(productnames)
print(productnames_json)
