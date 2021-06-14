class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print(f"Hello {other_person.name}, I am {self.name}!")
        self.greeting_count += 1

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}")
        print(f"{self.name}'s phone number: {self.phone}")
    
    def add_friend(self, other_friend):
        self.friends.append(other_friend.name)
    
    def num_friends(self):
        return len(self.friends)

    def __str__(self):
        return f'''
Person: {self.name}
Email: {self.email}
Number: {self.phone}
'''
    