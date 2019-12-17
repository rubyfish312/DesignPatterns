#%%
from abc import ABCMeta, abstractmethod

#%%
class Observer(metaclass=ABCMeta):
    """base class of observer"""
    @abstractmethod
    def update(self, observable, object):
        pass

class Observable:
    """base class of observable, eg: WaterHeater"""
    def __init__(self):
        self._observers = []
    def addObserver(self, observer):
        self._observers.append(observer)
    def removeObserver(self, observer):
        self._observers.remove(observer)
    def notifyObservers(self, object=0):
        for o in self._observers:
            o.update(self, object)

# %%
