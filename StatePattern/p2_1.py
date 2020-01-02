#%%
from abc import ABCMeta, abstractmethod

# %%
class Water:
    """ H2O """
    def __init__(self, state):
        self._temperature = 25
        self._state = state

    def setState(self, state):
        self._state = state

    def changeState(self, state):
        if (self._state):
            print("from", self._state.getName(), "to", state.getName())
        else:
            print("initial", state.getName())
        self._state = state

    def getTemperature(self):
        return self._temperature
    
    def setTemperature(self, temperature):
        self._temperature = temperature
        if (self._temperature <= 0):
            self.changeState(SolidState("solid"))
        elif (self._temperature <= 100):
            self.changeState(LiquidState("liquid"))
        else:
            self.changeState(GaseousState("gas"))
        
        

    def riseTemperature(self, step):
        self.setTemperature(self._temperature + step)
    
    def reduceTemperature(self, step):
        self.setTemperature(self._temperature - step)

    def behavior(self):
        self._state.behavior(self)


#%%
class state(metaclass=ABCMeta):
    """3 states"""
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name
    
    @abstractmethod
    def behavior(self, water):
        """ different behavior in each state """
        pass

class SolidState(state):
    def __init__(self, name):
        super().__init__(name)
    
    def behavior(self, water):
        print("current temperature" + str(water.getTemperature()) + 
        "please use me to attack someone")

class LiquidState(state):
    def __init__(self, name):
        super().__init__(name)
    
    def behavior(self, water):
        print("current temperature" + str(water.getTemperature()) +
        "please drink me")

class GaseousState(state):
    def __init__(self, name):
        super().__init__(name)
    
    def behavior(self, water):
        print("current temperature" + str(water.getTemperature()) +
        "i am flying")

#%%
def testState():
    # water = Water()
    water = Water(LiquidState("liquid"))
    water.behavior()
    
    water.setTemperature(-4)
    water.behavior()
    
    water.setTemperature(18)
    water.behavior()
    
    water.setTemperature(110)
    water.behavior()


#%%
testState()




# %%
