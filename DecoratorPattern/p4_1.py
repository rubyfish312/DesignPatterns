#%%
from abc import ABCMeta, abstractmethod

#%%
class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name
    
    @abstractmethod
    def wear(self):
        print("wears : ")

class Engineer(Person):
    def __init__(self, name, skill):
        super().__init__(name)
        self._skill = skill

    def getSkill(self):
        return self._skill

    def wear(self):
        print("i m " + self.getSkill() + "engineer" + self._name, end = "'")
        super().wear()

class Teacher(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self._title = title

    def getTitle(self):
        return self._title

    def wear(self):
        print("i m " + self._name, self.getTitle(), end = " ' ")
        super().wear()

#%%
class ClothingDecorator(Person):
    """ ClothingBaseClass"""
    def __init__(self, person):
        self._decorated = person
    
    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass

#%%
class CasualPantDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a brown casual pant")

class BeltDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a black belt")

class LeatherShoesDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a pair of darkness shoes")

class KnittedSweaterDecorator(ClothingDecorator):
    def __ini__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a red sweater")

class WhiteShirtDecorator(ClothingDecorator):
    def __ini__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a white shirt")

class GlassesDecorator(ClothingDecorator):
    def __ini__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a sliver glass")

#%%
def testDecorator():
    tony = Engineer("Tony", "user end")
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    shirt = WhiteShirtDecorator(shoes)
    sweater = KnittedSweaterDecorator(shirt)
    glasses = GlassesDecorator(sweater)
    glasses.wear()
    print()
    decorateTeacher = GlassesDecorator(WhiteShirtDecorator(LeatherShoesDecorator(Teacher('wells', 'Prof.'))))
    decorateTeacher.wear()


#%%
testDecorator()    






# %%
