#example for polymorphism(method overriding)
#method overriding feature develop only by inherited classes

class Grandparent:
    def div(self,i,j):
        print(i/j)
        return
class parent(Grandparent):
    def div(self,i,j):
        print("%f" %(i/j))
        return
class child(parent):
    def div(self,i,j):
        print("%.02f" %(i/j))
        return

objgp=Grandparent()
objp=parent()
objc=child()

objgp.div(10,3)
objp.div(10,2)
objc.div(10,2)

'''
3.3333333333333335
5.000000
5.00
'''
