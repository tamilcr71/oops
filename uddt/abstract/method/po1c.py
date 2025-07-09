#abstract (base) class or abstract method
from abc import ABC, abstractmethod

class drinks(ABC):
    @abstractmethod
    def ucategories(self):
        pass
class hot(drinks):
    def ucategories(self):
        print("hot drinks:coffee,tea,milk")
        return

#according to python,object creation part called as driver code
print(issubclass(hot,drinks))
print(isinstance(hot(),drinks))

'''
True
True
'''
