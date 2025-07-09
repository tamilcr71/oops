#abstract(base) class or abstact method
from abc import ABC, abstractmethod

class drinks(ABC):
    def ucategories(self):
        pass

class hot(drinks):
    #override abstract method
    def ucategories(self):
        print("hot drinks:coffee,tea,milk")
        return

class cool(drinks):
    #override abstract method
    def ucategories(self):
        print("cool drinks:coke,7up,pepsi")
        return
class soft(drinks):
    #override abstract method
    def ucategories(self):
        print("soft drinks:orange,mango,grape juice")
        return
obj=hot()
obj.ucategories()
obj=cool()
obj.ucategories()
obj=soft()
'''
hot drinks:coffee,tea,milk
cool drinks:coke,7up,pepsi
'''
