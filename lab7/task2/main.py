from models import Animal, Dog, Cat


def main():
    dog = Dog("Bunny", 3, "Brown", "Labrador")
    cat = Cat("Teddy", 2, "White", 9)
    animal = Animal("Generic", 5, "Gray")

   
    animals = [dog, cat, animal]

   
    for a in animals:
        print(a) 
        print(a.eat())
        print(a.sleep())
        print(a.speak()) 
        print("-" * 30)

    
    print(dog.fetch())
    print(cat.scratch())


if __name__ == "__main__":
    main()