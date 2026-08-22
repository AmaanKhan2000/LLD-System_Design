from good_Example import Observer
from typing import List
class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self._observers : List[Observer] = []

    def append_observer(self, new_obs: Observer):
        self.new_obs = new_obs
        self._observers.append(self.new_obs)

    def remove_observer(self, obs: Observer):
        self.obs= obs    
        self._observers.remove(self.obs)        


    def update(self, new_temp):
        self.__temperature = new_temp
        self.notify()

    def notify(self):
        for i in self._observers:
            i.update(self.__temperature)
