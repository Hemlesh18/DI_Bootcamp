# # 1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class siamese(Cat):
#     def sing(self, sounds):
#         return f'{"sound"}'
    
# all_cats = [Bengal("kitty",5),Chartreux("sammy",6),siamese("shasha",2)]    

# sara_pet =Pets(all_cats)
# sara_pet.walk()

# 2
class Dog:
    def __init__(self,name,age,weight):
        self.name=name 
        self.age=int(age)
        self.weight=int(weight)
    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        return self.weight/self.age*10
    def fight(self,other_dog):
        self.other_dog=other_dog
        if int(self.run_speed())*int(self.weight)> int(other_dog.run_speed())* int(other_dog.weight):
            print(f"{other_dog.name} has won")

my_dog1 =Dog("snoopy",3,10)
my_dog2=Dog("danzo",5,14)
my_dog3 =Dog("simba",1,8)
my_dog3.fight(my_dog2)




        
