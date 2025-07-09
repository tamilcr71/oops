#example for encapsulation(private or protected) or data hiding (public vs provate)\

#public access specifier data in use anywhere by object
#private access specifier data can use in data declaration class only

class c1:
    def __init__(self,i,j):
        self.i=i #public access specifier
        self.__j=j#private access specifier identifier is double underscore like __
        #private access specifier data always start with double underscore(__)
        return
    def result(self):
        print(self.i + self.__j)
        return

obj=c1(3,9)
obj.result()

print(obj.i)

'''
12
3
'''
