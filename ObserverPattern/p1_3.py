#%%
from abc import ABCMeta, abstractmethod
from ObserverPattern import p1_2
#from p1_2 import Observable, Observer
#import p1_2

# %%
class WaterHeater(p1_2.Observable):
    
    def __init__(self):
        super().__init__()
        self._temperature = 25
    
    def getTemperature(self):
        return self._temperature

    def setTemperature(self, temperature):
        self._temperature = temperature
        print("current temperature is : " + str(self._temperature) + " ")
        self.notifyObservers()


# %%
class WashingMode(p1_2.Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and \
           observable.getTemperature() >= 50 and  observable.getTemperature() < 70:
            print("hot water is ready for taking a bath")

class DrinkingMode(p1_2.Observer):
     def update(self, observable, object):
         if isinstance(observable, WaterHeater) and  observable.getTemperature() >= 100:
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
