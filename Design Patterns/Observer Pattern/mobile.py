from good_Example import Observer

class MobileDisplay(Observer):
    def update(self, new_temp):
        self.new_temp = new_temp
        print(f"The updated Mobile display temp is {self.new_temp}")

    