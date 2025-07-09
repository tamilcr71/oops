#example for encapsulation (private or protected)
#protected and or public access specifier data can use anywhere by object
#protected and or public access specifier data can use anywhere in inherited classes

class c1:
    def __init__(self,i,j):
        self.i=i#public access specifier
        self._j=j #protected access specifier indentifier is simple underscore like _
        #protected access specifier data always starts with single underscore(_)
        return
    def result(self):
        print(self.i + self._j)
        return

obj=c1(3,9)
obj.result() #12

print(obj.i)#3
print(obj._j)#9

'''
12
3
9
'''
