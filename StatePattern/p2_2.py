#%%
from abc import ABCMeta, abstractmethod

# %%
class Context(metaclass=ABCMeta):
    """the context of envirnment class in state pattern"""
    def __init__(self):
        self._states = []
        self._curState = None
        # the attribute that state depends on as changing 
        # set this variable as a single class when it is decided by multiple variables
        self._stateInfo = 0

    def addState(self, state):
        if (state not in self._states):
            self._states.append(state)

    def changeState(self, state):
        if (state is None):
            return False
        if (self._curState is None):
            print("initial as ", state.getName())
        else:
            print("from", self._curState.getName(), "to", state.getName())
        self._curState = state
        self.addState(state)
        return True

    def getState(self):
        return self._curState
    
    def _setStateInfo(self, stateInfo):
        self._stateInfo = stateInfo
        for state in self._states:
            if (state.isMatch(stateInfo)):
                self.changeState(state)
    
    def _getStateInfo(self):
        return self._stateInfo
    
#%%
class State:
    """basic class of states"""
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def isMatch(self, stateInfo):
        "check if the stateInfo attribute is in the state._curState"
        return False
    
    @abstractmethod
    def behavior(self, context):
        pass
    
    