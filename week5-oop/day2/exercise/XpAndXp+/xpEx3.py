from w5exxp import Dog

class petDog(Dog):
    def __init__(self,name,age,weight,trained= False):
       Dog.__init__(self,name,age,weight)
       self.trained = trained
    def train(self):
        print(self.bark())
        self.trained= True

    def play(self, *args):
        print(f"{args} all play together ")
   

    def do_a_trick(self):
        if self.trained == True:
            print(f"{self.name} do this")

        else:
            pass

my_dog = petDog()


