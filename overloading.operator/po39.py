#example for(arithmetic) operator (+,-,*,/) overloading
#__add__,__sub__,__mul__,__truediv__ attributes are
#develops +,*,-,/ operator overloading

#in addition example for 'str' attribute also

class uCalcu:
    def __init__(self,i=0):
        self.i=i
        print("default or overload constructor")
        return
    def __add__(self,x):
        print("__addition__")
        return uCalcu(self.i + x)

    def __sub__(self,x):
        print("__SUBTRACTION__")
        return uCalcu(self.i - x)
    def __mul__(self,x):
        print("__multiplication__")
        return uCalcu(self.i * x)
    def __truediv__(self,x):
        print("__division__")
        return uCalcu(self.i / x)


    #__str__attribute helps for return class property (lik data) value to object
    #__str__attrubute automatically start process ehrn put object in output statement
    #in case __str__ attribute not found then output statement has object return its address only


    def __str__(self):
        return str(self.i)

obja=uCalcu(100)
objb=obja+50
objc=objb-25
objd=objc*10
obje=objd/5

print(obja)
print(objb)
print(objc)
print(objd)
print(obje)



'''
default or overload constructor
__addition__
default or overload constructor
__SUBTRACTION__
default or overload constructor
__multiplication__
default or overload constructor
__division__
default or overload constructor
100
150
125
1250
250.0
'''
