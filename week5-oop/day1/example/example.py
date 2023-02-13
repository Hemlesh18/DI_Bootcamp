# class Dog():#instance of a calss
#     def __init__(self):#constuctor
#         print("inatiating dog creation..woof")
# class Human():
#     def __init__(self) -> None:
#         pass
# class pizza():
#     def __init__(self) -> None:
#         print("my pizza ")

      
              
# my_dog=Dog()#my dog is an object
# other_dog=Dog()


# class Planets():
#     def __init__(self):
#         print("Planets in our solar system:")
    

# our_planet=Planets()

# class Car():
#     def __init__(self) -> None:
#         print("create car ")
#         self.color="blue"# best practice
#         self.brand="honda"
#         self.engine_started= False

#     def accelerate(self):
#         print("Accelerating to the speed of sound..")

# my_car=Car()
# my_car.accelerate()
# # my_car.color= "blue"#not a good practice 
# print(f" my car is :{my_car.color}") 
# print(my_car.brand) 
# another_car= Car()
# print(f" my is {my_car.color}")   

# class Car():
#     def __init__(self,brand,color):
#         print("create car ")
#         self.color=color
#         self.brand=brand
#         self.engine_started= False

#     def start_engine(self):
#         self.engine_started= True

#     def stop_engine(self):
#         self.engine_started= False

#     def accelerate(self):
#         if self.engine_started:
#             print("Accelerating to the speed of sound..")
#         else:
#             print("start engine first")


# my_car=Car("Toyota","Yellow")
# my_car.start_engine()
# my_car.accelerate()
# my_car.stop_engine()

# print(f" my {my_car.brand} is {my_car.color}") 
# print(my_car.brand) 

# another_car= Car("Porsche","blue")
# print(f" my {my_car.brand} is {my_car.color}") 
# print(another_car.brand) 
# print(another_car.color)


# class Car():
#     def __init__(self,brand,color):
#         print("create car ")
#         self.color=color
#         self.brand=brand
#         self.engine_started= False

#     def start_engine(self):
#         self.engine_started= True

#     def stop_engine(self):
#         self.engine_started= False

#     def accelerate(self):
#         if self.engine_started:
#             print("Accelerating to the speed of sound..")
#         else:
#             print("start engine first")
#     def display_info(self):
#         print(f" my {self.brand} is {self.color}")


# my_car=Car("Toyota","Yellow")
# my_car.start_engine()
# my_car.accelerate()
# my_car.stop_engine()
# my_car.display_info()
# print("\n")
# another_car= Car("Porsche","blue")
# another_car.accelerate()
# another_car.display_info()

# my_garage=[]
# my_garage.append(my_car)
# my_garage.append(another_car)
# for car in my_garage:
#     # my_garage.dislay_info()




class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")