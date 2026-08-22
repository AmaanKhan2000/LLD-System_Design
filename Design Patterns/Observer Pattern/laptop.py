from good_Example import Observer

class LaptopDisplay(Observer):
    def update(self, new_temp):
        self.new_temp = new_temp
        print(f"The updated Laptop display temp is {self.new_temp}")

    