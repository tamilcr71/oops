#concrete method

from abc import ABC , abstractmethod

class drinks(ABC):
    @abstractmethod
    def ucategories(self):
        print("drink categories are hot cool and soft")
        return
class hot(drinks):
    #override abstract method
    def ucategories(self):
        super().ucategories()
        print("hot drinks: tea,milk and coffee")
        return

obj=hot()
obj.ucategories()
'''
drink categories are hot cool and soft
hot drinks: tea,milk and coffee
'''
