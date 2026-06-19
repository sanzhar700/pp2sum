class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(self.brand)

# Create the object c1 with the brand "Ford"
c1 = Car("Ford")

# Call the show method
c1.show()
