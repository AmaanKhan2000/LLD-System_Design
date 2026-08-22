from weather_station import WeatherStation
from tv import TVDisplay
from mobile import MobileDisplay
from laptop import LaptopDisplay

ws = WeatherStation()
tv = TVDisplay()
ws.append_observer(tv)
ws.append_observer(MobileDisplay())
ws.append_observer(LaptopDisplay())
ws.update(30)