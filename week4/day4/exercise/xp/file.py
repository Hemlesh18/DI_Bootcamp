# def display_message():
#     print("i am learning python")

# display_message()   


# 2

# def favorite_book(title):
#     print(f"one of my favorite books is {title}")

# favorite_book("Alice in Wonderland")    


# # 3
# def describe_city(city,country="iceLand"):
#     print(f"{city} is in {country}")

# describe_city("Reykjavik")    

# # 4
# import random

# def num():
#     number=int(input("enter an number between 1 and 100: "))
#     print(number)
#     range = random.randrange(1,100)
#     print(int(range))
    
#     if num == range:
#         print("SUCCESS!")
#     else:
#         print("fail")
# num()        

# 5
# def make_shirt(size, text):
#     print(f"The size of the shirt is {size} and the text is {text}")

# make_shirt() 
# 
# def make_shirt(size="medium", text="i love python"):
#     print(f"The size of the shirt is {size} and the text is {text}")

# make_shirt("large") 
# make_shirt("medium")
# make_shirt("small","i a hemlesh")

# def make_shirt(**kwargs):
#     print(kwargs)

# make_shirt(size="large",text="zzzzzzz")    

# 

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for name in magician_names:
        print(name)
show_magicians()     


def show_magicians():
    for name in magician_names:
        print(name)
        
        def make_great():
         for name in magician_names:
            print(f"The great {name}")
    make_great()
show_magicians()

# 7

import random
def get_random_temp():
   return random.randint(-10,40)
