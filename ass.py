# Step 1: Create a base class Animal with a method make_sound()
class Animal:
    def make_sound(self):
        print("Generic animal sound")

# Step 2: Create two subclasses Dog and Cat, each inheriting from the Animal class.
class Dog(Animal):
    # Step 3: Override the make_sound() method in the Dog class with its respective sound (bark).
    def make_sound(self):
        print("Bark! Bark!")

class Cat(Animal):
    # Step 3: Override the make_sound() method in the Cat class with its respective sound (meow).
    def make_sound(self):
        print("Meow! Meow!")

# Step 4: Implement a function called animal_sound_in_zoo() that takes an animal object as a parameter and calls its make_sound() method.
def animal_sound_in_zoo(animal):
    animal.make_sound()

# Step 5: Create instances of Dog and Cat classes and call the animal_sound_in_zoo() function with these instances as arguments to observe their unique sounds.
if _name_ == "_main_":
    dog = Dog()
    cat = Cat()

    animal_sound_in_zoo(dog)
    animal_sound_in_zoo(cat)
        
        
