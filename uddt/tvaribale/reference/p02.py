#EXAMPLE FOR REFERENCE TYPE VARIABLE

class p02:
    def __init__(self):
        print("constructor")
        return
    def __del__(self):
        print("destructor")
        return
    def show(self):
        print("method:show")
        return

obj=p02().show
#above statement first process anonymus object (p02) initialization part
#next store show method address to obj variable
#finally process destructor by anonymus object po2 initilization part

obj()
#above statement process it has show method address task

'''
constructor
method:show
'''
