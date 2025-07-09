'''
example for how to develop new features  using single inheritance
'''

class uMath0:
    def uSum(self,x,y):
        return x+y
class uMath1(uMath0):
    def uMin(self,x,y):
        return x-y
class uMath2(uMath1):
    def uDiv(self,x,y):
        return x/y


    def uMod(self,x,y):
        return x%y

    def uMul(self,x,y):
        return x*y

class uMath(uMath2):
    pass #later develop definition part for uMath class

#which one object declaration before part has assignment operator(=)
#that kind of object called as named object
#which one object declaration before part missing assignment operator(=)
#that kind of object called as nameless or temporary or anonmyous object
obj=uMath()

su=obj.uSum(9,2)
mi=obj.uMin(8,4)
di=obj.uDiv(10,3)
mu=obj.uMul(0.5,8)
mo=obj.uMod(20,6)

print(su,"\t",mi,"\t",di,"\t",mu,"\t",mo,"\t")


'''
11 	 4 	 3.3333333333333335 	 4.0 	 2 	
'''
