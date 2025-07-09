class A:
    def __init__(self):
        print("constructor:A")
        return
    def __del__(self):
        print("destructor:A")
        return

class B (A):

    def __init__(self):
        A.__init__(self)
        print("constructor:B")
        return
    def __del__(self):
        print("destructor:B")
        A.__del__(self)
        return

obj=B()

'''
constructor:A
constructor:B
destructor:B
destructor:A

'''

