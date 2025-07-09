'''
example for single inheritance
'''

class uA:
    def __init__(self):
        print("uA:constructor")
        return
    def __del__(self):
        print("uA:destructor")
        return
class uB:
    def __init__(self): # derived (or child) class:uB,base (or parent) class:uA
        uA.__init__(self)
        print("uB:contructor")
        return
    def __del__(self):
        print("uB:destructor")
        uA.__del__(self)
        return
#declare named object (obj) to class(uB)
obj=uB()
print("main indent")


'''
uA:constructor
uB:contructor
main indent
uB:destructor
uA:destructor

'''
