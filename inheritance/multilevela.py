'''
example for inheritance with constructor and destructor
'''

class udrinks:
    def __init__(self):
        print("drinks:constructor")
        return
    def __del__(self):
        print("drinks:destructor")
        return

#here develop inheritance concept
#base (or parent) class:udrinks
#derived(or child) class:udrinks

class uhot(udrinks):
    def __init__(self):
        #super class nameless object declaration part calld base class constructor
        #using init attribute
        super(uhot,self).__init__()
        print("hot:constructor")
        return
    def __del__(self):
        print("hot:destructor")
        #super class nameless object declaration part calld base class constructor
        #using del attribute
        super(uhot,self).__del__()


#here develop inheritance concept
#base (or root or grandparent)class:udrinks
#base(or parent or child)class:uhot
#derived(or grandchild or child)class:ucoffee

class ucoffee(uhot):
    def __init__(self):
        #super class always mean base class
        super(ucoffee,self).__init__()
        print("ucoffee:constructor")
        return
    def __del__(self):
        print("coffee:destructor")
        super(ucoffee,self).__del__()
        return
#declare named object (obj) to class (ucofee)
obj=ucoffee()

print("main indent")

#declare nameless object to class(ucoffee)
#therefore nameless object declaration part missing assignment operator like =
#ucoffee()


'''
drinks:constructor
hot:constructor
ucoffee:constructor
main indent
coffee:destructor
hot:destructor
drinks:destructor
'''
    
