# lib/person.py
class Person:
    def __init__(self, name):
        self.name = name

# Testing Person Class
if __name__ == "__main__":
    person1 = Person("Alice")
    print(person1.name)  # Should print "Alice"

    person2 = Person("Bob")
    print(person2.name)  # Should print "Bob"
