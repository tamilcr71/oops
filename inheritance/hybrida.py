'''
example for hybrid inheritance
'''

class uA:
    def __init__(self):
        print("uA:constructor")
        return
    def __del__(self):
        print("uA:destructor")
        return

class uB(uA):
    def __init__(self):
        uA.__init__(self)
        print("uB:constructor")
        return
    def __del__(self):
        print("uB:destructor")
        uA.__del__(self)
        return

class uC(uA): #derived (or child) class: uc,base(pr parent) classes :uA,uB
    def __init__(self):
        uA.__init__(self)
        print("uC:constructor")
        return

    def __del__(self):
        print("uC:destructor")
        uA.__del__(self)
        return
class uD(uB,uC):
    def __init__(self):
        uB.__init__(self)
        uC.__init__(self)
        print("uD:constructor")
        return
    def __del__(self):
        print("uD:destructor")
        uC.__del__(self)
        uB.__del__(self)
        return
#declare named object (obj) to class (uC)
obj=uD()
print("main indent")
'''
uA:constructor
uB:constructor
uA:constructor
uC:constructor
uD:constructor
main indent
uD:destructor
uC:destructor
uA:destructor
uB:destructor
uA:destructor
'''
