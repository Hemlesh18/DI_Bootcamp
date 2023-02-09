#  1
# word = input("enter a word: ")

# dictionary = {}

# for index, letter in enumerate(word):
#   if letter not in dictionary:
#     dictionary[letter] = []
#     dictionary[letter].append(index)
#   else:
#     dictionary[letter].append(index)

# print(dictionary)


# ex2
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1000",
  "Fertilizer": "$20"
}



items = list(items_purchase.values())
print(items)

wallet_str = input("Enter your wallet amount: ")
wallet = int(wallet_str.replace("$", ""))
affordable_items = []

for item in items:
  price = items_purchase[item] 
  price = price.replace("$","") 

price = int(price)
if price <=  wallet:
    affordable_items.append(item)

elif len(affordable_items) > 0:
  print("You can afford the following items: ", affordable_items)
else:
  print("Nothing")


