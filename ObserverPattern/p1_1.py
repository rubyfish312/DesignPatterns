#p1_1
#%%
from abc import ABCMeta, abstractmethod

#%% ducking type
class WaterHeater:

    def __init__(self):
        self._observers = []
        self._temperature = 25
    
    def getTemperature(self):
        return self._temperature

    def setTemperature(self, temperature):
        self._temperature = temperature
        print("current temperature is : " + str(self._temperature) + " ")
        self.notifies()

    def addObserver(self, observer):
        self._observers.append(observer)

    def notifies(self):
        for o in self._observers:
            o.update(self)


# %%
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, WaterHeater):
        pass
#%%
class WashingMode(Observer):
    def update(self, WaterHeater):
        if WaterHeater.getTemperature()>=50 and WaterHeater.getTemperature()<70:
            print("hot water is ready for taking a bath")

class DrinkingMode(Observer):
    def update(self, WaterHeater):
        if WaterHeater.getTemperature()>=100:
            print("hot water is ready to drink")
#%%     
heater = WaterHeater()
washingObser = WashingMode()
drinkingObser = DrinkingMode()
heater.addObserver(washingObser)
heater.addObserver(drinkingObser)
heater.setTemperature(40)
heater.setTemperature(60)
heater.setTemperature(100)




# %%
