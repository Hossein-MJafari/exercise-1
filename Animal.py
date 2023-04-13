
class Animal:
    def __init__(self, name, age, weight, height, species):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.species = species
        self.food = None
    
    def set_food(self, food_name):
        self.food = food_name

    def move(self):
        pass

    def eat(self):
        print(f"{self.name} is eating {self.food.name}.")

    def communicate(self):
        pass

    def breed(self):
        pass

    def sleep(self):
        pass

class Mamals(Animal):
    pass
class Dog(Mamals):
    pass
class Cat(Mamals):
    pass
class Horse(Mamals):
    pass
class Cow(Mamals):
    pass
class Elephant(Mamals):
    pass


class Birds(Animal):
    pass
class Eagle(Birds):
    pass
class Penguin(Birds):
    pass
class Parrot(Birds):
    pass


class Fish(Animal):
    pass
class Shark(Fish):
    pass
class Salmon(Fish):
    pass


class Reptiles(Animal):
    pass
class Snake(Reptiles):
    pass
class Lizard(Reptiles):
    pass


class Amphibian(Animal):
    pass
class Frog(Amphibian):
    pass


class Habitat:
    def __init__(self, name, location, climate):
        self.name = name
        self.location = location
        self.climate = climate
        self.food = None
        self.animals = []
    
    def add_animal(self, name, age, weight, height, species):
        animal = Animal(name, age, weight, height, species)
        self.animals.append(animal)


class Food:
    def __init__(self, name):
        self.name = name


class CareTaker:
    pass



# create objects
leaves = Food('Leaves')
savannah = Habitat('Savannah', 'USA', 'hot-humid')

# add animal to habitat
savannah.add_animal('Giraffe', 5, 100, 4, 'southern-giraffe')