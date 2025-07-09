class A:
    "parent class"#parent class
    def display(self):
        print("this is base class")
        return


class B(A):
    "child class"#derived class
    def display(self):
        A.display(self)
        print("this is derived class")
        print(A.__doc__)
        print(B.__doc__)
        return

obj=B()
obj.display()

'''
this is base class
this is derived class
parent class
child class
'''
