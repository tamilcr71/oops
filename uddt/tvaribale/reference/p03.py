#EXAMPLE FOR REFERENCE TYPE VARIABLE

class p03:
    def __init__(self,x=0):
        self.i=x
        print("constructor")
        return
    def __del__(self):
        print("destructor")
        return
    def show(self):
        print("i value",self.i)
        return

obj=p03
#above statement store address of class po3 variable tp object

obj(97)

obj().show()

obj(56).show()

'''
constructor
destructor
constructor
i value 0
destructor
constructor
i value 56
destructor
'''
