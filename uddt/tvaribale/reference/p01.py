#EXAMPLE FOR REFERENCE TYPE VARIABLE

class p01:
    def __init__(self):
        print("constructor")
        return
    def __del__(self):
        print("destructor")
        return

obj=p01 #store p01 class address to obj variable
obj() #here operate obj variable has address task

'''
constructor
destructor
'''
