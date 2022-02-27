'''
countr = input("Introduzca un pais:\n")
visiti = int(input("Cuantas veces visito ese pais?:\n") )
citie = input("introduzca las ciudades que visito dentro del pais:\n").split()

country = {
    "country": countr,
    "visits": visiti,
    "cities": citie
    }

travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "stuttgart"]
},
]

travel_log.append(country)

print(travel_log)
'''

travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "stuttgart"]
},
]

def add_new_country(countried, visits, citys):
    '''
    new_country = {}
    new_country["country"] = countried
    new_country["visits"] = visits
    new_country["cities"] = citys
    travel_log.append(new_country)
    '''
    dic = {"country": countried, "visities": visits, "cities": [citys]}
    travel_log.append(dic)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

dict = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
}

for key in dict:
    dict[key] += 1

    print(dict)