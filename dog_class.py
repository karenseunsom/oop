class Dog:
   # Class Attribute
   species = 'mammal'

   # Initialize / Instance Attributes
   def __init__(self, name, age):
       self.name = name
       self.age = age

   # Instance Method
   def description(self):
       return f"{self.name} is {self.age} years old"
    
   def bark_at(self, other_dog):
       print(f"{self.name} barked furiously at {other_dog.name}")


nelson = Dog("Nelson", 3)
baxter = Dog('Baxter', 16)

# print(nelson.description())
# print(baxter.description())

nelson.bark_at(baxter)

# when we have nelson, it's a new instance of class Dog.