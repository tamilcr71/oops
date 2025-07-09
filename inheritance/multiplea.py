'''
example for hierarchical inheritance
'''

class uA:
    def __init__(self):
        print("uA:constructor")
        return
    def __del__(self):
        print("uA:destructor")
        return

class uB:
    def __init__(self):
        print("uB:constructor")
        return
    def __del__(self):
        print("uB:destructor")
        return

class uC(uA,uB): #derived (or child) class: uc,base(pr parent) classes :uA,uB
    def __init__(self):
        uA.__init__(self)
        uB.__init__(self)
        print("uC:constructor")
        return

    def __del__(self):
        print("uC:destructor")
        uB.__del__(self)
        uA.__del__(self)
        return

#declare named object (obj) to class (uC)
obj=uC()
print("main indent")
'''
uA:constructor
uB:constructor
uC:constructor
main indent
uC:destructor
uB:destructor
uA:destructor

'''
