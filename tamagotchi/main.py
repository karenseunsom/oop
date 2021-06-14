from pet import Pet
from cuddlypet import CuddlyPet
from toy import Toy

# cujo = Pet('Cujo the Dog')
# benji = Pet('Benji')
# nelson = Pet('Nelson')

pet_name = input("What is your pet called? ")
pet_type = int(input("""
1. Pet
2. Cuddly Pet
Which pet would you like? """))

if pet_type == 1:
    pet = Pet(pet_name)
elif pet_type == 2:
    pet = CuddlyPet(pet_name)

    
while True:
    print(pet)
    choice = int(input("""
1. Feed Pet
2. Play with pet
3. Do Nothing
4. Give toy
"""))


    if choice == 1:
        # feed the pet
        pet.eat_food()
    elif choice == 2:
        # play with pet
        pet.get_love()
    elif choice == 4:
        pet.give_toy(Toy())

    
    # Each time the loop runs, the pet 
    # will need some attention

    pet.be_alive()
    if not pet.is_alive():
        print(pet)
        print(f'rip {pet.name}')
        break