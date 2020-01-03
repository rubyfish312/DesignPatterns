#%%
from abc import ABCMeta, abstractclassmethod
from p2_2 import Context, State

# %%
class Water(Context):
    """water"""
    def __init__(self):
        super().__init__()
        self.addState(SolidState("solid"))
        self.addState(LiquidState("liquid"))
        self.addState(GaseousState("gas"))
        self.addState(BalanceState("3Balance"))
        self.setTemperature(25)

    def getTemperature(self):
        return self._getStateInfo()

    def setTemperature(self, temperature):
        self._setStateInfo(temperature)
    
    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        state = self.getState()
        if (isinstance(state, State)):
            state.behavior(self)

#%% 
# singleton decorator
def singleton(cls, *args, **kwargs):
    instance = {}
    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton

#%%
@singleton
class SolidState(State):
    def ___init___(self, name):
        super().__init__(name)
    
    def isMatch(self, stateInfo):
        return stateInfo <= 0
    
    def behavior(self, context):
        print("current temperature", context._getStateInfo(),
        "please use me to attack someone")


@singleton
class LiquidState(State):
    def ___init___(self, name):
        super().__init__(name)
    
    def isMatch(self, stateInfo):
        return ((stateInfo > 0 and stateInfo < 100) and (stateInfo != 0.01))

    def behavior(self, context):
        print("current temperature", context._getStateInfo(),
        "please drink me")

@singleton
class GaseousState(State):
    def ___init___(self, name):
        super().__init__(name)
    
    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self, context):
        print("current temperature", context._getStateInfo(), 
        "i am flying")

@singleton
class BalanceState(State):
    def ___init___(self, name):
        super().__init__(name)
    
    def isMatch(self, stateInfo):
        return stateInfo == 0.01

    def behavior(self, context):
        print("current temperature", context._getStateInfo(), 
        "3 balance point")

#%%
def testState():
    # water = Water(LiquidState("liquid"))
    water = Water()
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()

#%%
testState()


# %%
