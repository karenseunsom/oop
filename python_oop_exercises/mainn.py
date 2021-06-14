from person import Person
from vehicle import Vehicle

sonny = Person("Sonny", 'sonny@hotmail.com', '483-485-4948')
jordan = Person("Jordan", 'jordan@aol.com', '495-586-3456')

car = Vehicle('Nissan', 'Leaf', 2015)

# sonny.greet(jordan)
# jordan.greet(sonny)

# print(sonny.email)
# print(sonny.phone)

# print(jordan.email)
# print(jordan.phone)


# sonny.print_contact_info()

# jordan.friends.append(sonny)
# print(len(jordan.friends))

# print(jordan.friends)
# print(len(jordan.friends))

# jordan.add_friend(sonny)
# print(jordan.num_friends())

# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)

print(str(jordan))
print(str(sonny))