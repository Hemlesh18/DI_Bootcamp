
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}   
    
    def add_animal(self, type, count=1):
        if type in self.animals:
            self.animals[type] += count
        else:
            self.animals[type] = count
    
    def get_info(self):
        output=f"{self.name}'s farm"
        for type, count in self.animals.items():
            output=output+f"\n{type} :{count}"
        return output

    def get_animal_types(self):
        animal_types = []
        for a in self.animals.keys():
            animal_types.append(a)
        return sorted(animal_types)
            
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print("\t E-I-E-I-0")
print(macdonald.get_animal_types())
