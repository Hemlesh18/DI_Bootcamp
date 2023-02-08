# ex1
# my_fav_numbers={1,2,3,4,5,6,9}
# my_fav_numbers.add(18)
# my_fav_numbers.add(28)
# my_fav_numbers.remove(28)
# friend_fav_numbers={12,15,4,54,9,8,7,2}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# ex2
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# it is not possible to add more integer as tuple are immutable

# ex3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("kiwi")

# print(basket.insert(0,"Apples"))
# print(basket.count("Apples"))
# print(basket.clear())
# print(basket)

# ex4
# What is a float? What is the difference between an integer and a float?
#  A data type that store numbers with decimal point.
# Can you think of another way to generate a sequence of floats?

# current_num = 1.5
# while current_num <= 5.5:
#     print(current_num)
#     current_num += 0.5

# sequence = []
# for i in range(1, 6):
#     x = i + 0.5
#     sequence.append(x)
# print(sequence)

# ex5
# for num in range(1,21):
#      print(num)
# 
# for num in range(1, 21):
#     if num % 2 == 0:
#         print(num)


# ex6
# name =''
# while name != "khavind":
#     name = input("Enter name:")

# ex7
# favorite_fruits=input("enter your favorite fruit(s)and seperate them with a single space:")
# list_of_fruits= favorite_fruits.split()
# print(list_of_fruits)
 
# fruits=input("enter  fruit: ")
# if fruits in list_of_fruits:
#         print("You chose one of your favorite fruits! Enjoy!")

# else:
#     print("You chose a new fruit. I hope you enjoy")

# ex8
# topping= input("add topping on your pizza:")
# active =True
# while active:
#     adding=input("topping added, choose more or quit?")
#     if adding == "quit":
#         active=False

# print("Your total is:", 10+2.5, "for each topping")

# ex9
# age=int(input("Enter age or enter '0' to quit:"))
# price = []
# active= True
# while age != 0:
#     age=int(input("Enter age or enter '0' to quit:"))
#     if age <= 3:
#           price.append(0)
#     elif age>3 and age<12:
#           price.append(10)
#     elif age== 0:
#           active = False
#     else:
#           price.append(15)
# print(sum(price))

# teenagers_group= int(input("how many teenagers? "))
# teens_allowed=[]
# for teen in range(teenagers_group):
#       name = input("enter your names:")
#       age =int(input("enter {}'s age:".format(name)))
      
#       if  16<= age <=21: 
#            teens_allowed.append(name)
# print("Final list of allowed teens:", teens_allowed)     
            

# ex 10,11
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich" ,"Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
print(sandwich_orders)
finished_sandwiches =[]

print("The Deli has run out of pastrami")
while 'Pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')
print()
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"i made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)



