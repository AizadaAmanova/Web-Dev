from models import Animal, Dog, Cat


def main():
    animal = Animal("Buddy", 5, "brown")
    dog = Dog("Rocky", 3, "black", "Labrador")
    cat = Cat("Misty", 2, "white", True)

    animals = [animal, dog, cat]

    for item in animals:
        print(item)
        print(item.speak())
        print(item.move())

        if isinstance(item, Dog):
            print(item.fetch())

        if isinstance(item, Cat):
            print(item.climb())

        print("-" * 30)


if __name__ == "__main__":
    main()