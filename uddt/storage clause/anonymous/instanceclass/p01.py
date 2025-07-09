#example for named object
'''
named object vs.nameless(anonymous or temprovary) object
named object life time is lifetime of indentation
namless object lifetime is lifetime of expression

syntax:
named object syntax:
<object name>=<class name>(optional actual paramter)

namless object syntax:
<class name>(optional actual paramter)

example:
named object eith zero number of actual paramter example
obj=p01()

named object with on actual paramter
obj=p01(79)

namless object with zero actual parmater
p01()

namless object with actual paramter
p01(79)

#1
develop overload constructor using optional formal paramter feature
'''
class p01:
    def __init__(self,x=0):
        print("constructor:overload")
        self.i=x
        return
    def __del__(self):
        print("destructor")
        del self.i
        return
    def show(self):
        print(self.i)
        return
    
print("main scope start")
obj=p01()
print(obj.i)
obj.show()
del obj
obj=p01(79)

print(obj.i)
obj.show()

del obj
print("main scope end")

'''
main scope start
constructor:overload
0
0
destructor
constructor:overload
79
79
destructor
main scope end
'''
