class Laptop:
    processor = None
    ram = None
    graphics_card = None
    display_size = None

    def show_specs(self):
        if self.display_size:
            print(f"Display Size: {self.display_size}")
        if self.processor:
            print(f"Processor Size: {self.processor}")
        if self.ram:
            print(f"Ram Size: {self.ram}")
        if self.graphics_card:
            print(f"Graphics Card: {self.graphics_card}")    

class LaptopBuilder:
    def __init__(self):
        self.__laptop = Laptop()
    def processor(self,processor:str):
        self.__laptop.processor = processor
        return self
    def graphics_card(self,graphics_card:str):
        self.__laptop.graphics_card = graphics_card
        return self
    def display_size(self,display_size:str):
        self.__laptop.display_size = display_size
        return self
    def ram(self,ram:str):
        self.__laptop.ram = ram
        return self
    def build(self):
        return self.__laptop

l1 = LaptopBuilder().display_size("23").ram("35").build() 
l1.show_specs()         