# 1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat("cat1",3)
# cat2 =Cat("cat2",5)
# cat3= Cat("cat3",6)

# def find_the_oldest_cat(cats):
#     oldest_cat = cats[0]
#     for cat in cats[1:]:
#         if cat.age > oldest_cat.age:
#             oldest_cat= cat
#     return oldest_cat
# oldest_cat = find_the_oldest_cat([cat1,cat2,cat3])
# print(f"the oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old")

# 2
# class Dog:
#     def __init__(self, name,height):
#         self.name =name
#         self.height=height

#     def bark(self):
#         print("{} goes woof!".format(self.name))
#     def jump(self):
#         print(f"{self.name} jumps {2* self.height} cm high!")


# davids_dog =Dog("rex",50)

# print(f'Dog details -- Name: {davids_dog.name}, Height: {davids_dog.height}')
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog =Dog("Teacup",20)
# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
#     print(f'The bigger dog is {davids_dog.name}')
# else:
#     print(f'The bigger dog is {sarahs_dog.name}')

# 3 
class Song:
    def __init__(self,lyrics):
        self.lyrics=[]

    def sing_me_a_song(self):
        print(f"{self.lyrics}")
        
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])



