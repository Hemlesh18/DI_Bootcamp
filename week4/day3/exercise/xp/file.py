
# 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
item_dictionary=dict(zip(keys,values))
print(item_dictionary)


# 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for member, age in family.items():
  if age < 3:
    ticket_price = 0
  elif age >= 3 and  age<= 12:
    ticket_price = 10
  else:
    ticket_price = 15
  total_cost += ticket_price
print("The family's total cost for the movie ticket is", total_cost)  

# 3

brand={"name":"Zara",
         "creation_date":"1975",
           "creator_date":"Amancio Ortega Gaona",
           "type_of_clothes":["men", "women" , "children" , "home"],
        "international_competitors":["Gap","H&M","Benetton"],
          "number_stores":"7000",
            "major_color": {"France":"blue",
                            "Spain":"red",
                            "US":["pink","green"]}
  }
brand["number_stores"]= "2"
print(brand,"\n")

print("Zara's clients are:", brand['type_of_clothes'][0:3] ,"\n")

brand["country_creation"]= "spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual") 
print(brand,"\n")    
del brand["creation_date"]
print(brand,"\n")

print(brand["international_competitors"][-1],"\n")

print(brand["major_color"]["US"],"\n")

print(len(brand),"\n")

print(brand.keys(),"\n")

more_on_zara= {"creation_date": 1975,
               "number_stores": 10000
               }

brand.update(more_on_zara)
print(brand)
print(brand["number_stores"])

# 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A={}
for index, user in enumerate(users):
    disney_users_A[user] = index

print(disney_users_A)

disney_users_B = {}
for (index, value) in enumerate(users):
    disney_users_B[index] = value

print(disney_users_B)

users.sort()
print(users)
disney_users_C = {key: i for i, key in enumerate(users)}
print(disney_users_C)

disney_users_A={"Mickey": 0,
                 "Minnie": 1,
                   "Donald": 2,
                     "Ariel": 3,
                       "Pluto": 4
}



#4(1)
new_dict = {}
counter = 0 
for user in disney_users_A:
  if "i" in user:
    new_dict[user] = counter
    counter +=1
print(new_dict)


