#p1_1
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
    def update(self, waterHeater):
        pass

# %%
