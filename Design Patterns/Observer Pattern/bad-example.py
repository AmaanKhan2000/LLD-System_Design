class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__phone_display = PhoneDisplay()

    def update_temperature(self, up_temp):
        self.__temperature = up_temp
        self.notify_display()

    def notify_display(self):
        self.__phone_display.update(self.__temperature)       

class PhoneDisplay:
    def update(self, new_temp):
        self.new_temp = new_temp
        print(f"The updated temperature is {self.new_temp} degrees")

ws = WeatherStation()
ws.update_temperature(30)


