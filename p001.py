"""
title:
POP language vs. obp language
"""
i=5
#declare variable outside of class

class clsA:
    j=55
    #declare class varible inside of class
    #we can class variable without object

    # __init__ is special or magic method
    # special or magic method names always starts and ends with "__"
    # __init__ method develop constructor feature
    # constructor always process begining of class
    # destructor always process ending of class
    # __del__ special method develop destructor feature

    # self is special formal parameter
    #first formal parameter should be self
    #self formal paramter develop instance properties
    # instance alias name is object
    #instance properties are instance varible and instance method

    def __init__(self):
        self.k=555
        return

    print(i) #5
    print(clsA.j)

    #initialzation part = declaration part + definition part

    obj=clsA()
    print(obj.k)#555
    print(clsA().k)#555
