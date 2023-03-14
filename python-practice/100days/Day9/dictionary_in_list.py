travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

    




# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



product = {"itemid" : 1234, "name" : "tshirt", "colour":"white"}
print(product['name'])

product['size'] = 'small'

print(product)

del product["name"]

print(product)


product["size"] = ["small", "medium", "large"]

print(product['size'][1])


products = [
  {'itemid':'1001', 'name':'tshirt', 'colour':'white', 'size':['small', 'medium', 'large']},
  {'itemid':'1002', 'name':'sweatshirt', 'colour':'white', 'size':['x-large', 'medium', 'large']},
  {'itemid':'1003', 'name':'hoody', 'colour':'white', 'size':['small', 'medium', 'large']}
            ]

print(products[0]['itemid'], products[1]['colour'], products[2]['size'])