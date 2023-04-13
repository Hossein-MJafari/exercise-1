
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
    def __init__(self, name, age, fur_color, warmblooded):
        super().__init__(name, age)
        self.fur_color = fur_color
        self.warmblooded = warmblooded
class Dog(Mamals):
    pass
class Cat(Mamals):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        self.sound = 'Meow'

    def meow(self):
        return self.sound
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
        self.is_clean = True
    
    def add_animal(self, name, age, weight, height, species):
        animal = Animal(name, age, weight, height, species)
        self.animals.append(animal)
        self.is_clean = False

    def set_food(self, food):
        self.food = food

    def clean(self):
        self.is_clean = True

class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


class CareTaker:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience
        self.animals = []

    def add_animal(self, name, age, weight, height, species):
        animal = Animal(name, age, weight, height, species)
        self.animals.append(animal)
    
    def feed_animal(self, food):
        for animal in self.animals:
            animal.set_food(food)

    def clean_habitat(self):
        for animal in self.animals:
            animal.habitat.clean()



# create objects
leaves = Food('Leaves', 100)
savannah = Habitat('Savannah', 'USA', 'hot-humid')
jane = CareTaker('Jane', 30, 'professional')

# add animal to habitat
savannah.add_animal('Giraffe', 5, 100, 4, 'southern-giraffe')

# add animal to caretaker
jane.add_animal('Lion', 4, 55, 1.5, 'cats')

# set food for habitat
savannah.set_food(leaves.name)
# set food for animal
giraffe = savannah.animals[0]
giraffe.set_food(leaves.name)
lion = jane.animals[0]
lion.set_food(leaves.name)

# caretaker feeds the animals
jane.feed_animal(leaves.name)