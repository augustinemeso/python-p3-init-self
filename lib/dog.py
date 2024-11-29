# lib/dog.py
class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

# Testing Dog Class
if __name__ == "__main__":
    dog1 = Dog("Fido")
    print(dog1.name)  # Should print "Fido"
    print(dog1.breed)  # Should print "Mutt"

    dog2 = Dog("Snoopy", "Beagle")
    print(dog2.name)  # Should print "Snoopy"
    print(dog2.breed)  # Should print "Beagle"
