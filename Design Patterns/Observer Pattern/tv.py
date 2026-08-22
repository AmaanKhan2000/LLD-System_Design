from good_Example import Observer

class TVDisplay(Observer):
    def update(self, new_temp):
        self.new_temp = new_temp
        print(f"The updated TV display temp is {self.new_temp}")

    