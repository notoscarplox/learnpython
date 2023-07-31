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

#TODO: Write the function that will allow new countries

def add_new_country(country_visit, times_visit, cities_visit):
    new_country={}
    new_country["country"] = country_visit                #Remember: to index a key in a dictionary you index the actual key
    new_country["visits"] = times_visit
    new_country["cities"] = cities_visi
    travel_log.append(new_country)





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
