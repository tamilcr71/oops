#example for nameless object

class p02:
    def __init__(self,x=0):
        print("constructor:overload")
        self.i=x
        return
    def __del__(self):
        print("destructor")
        del self.i
        return
    def show(self):
        print(self.i)
        return
print("main scope start")

p02()
print(p02().i)
p02().show()

p02(79)
print(p02(79).i)
p02(79).show()

print("main scope end")
'''
main scope start
constructor:overload
destructor
constructor:overload
destructor
0
constructor:overload
0
destructor
constructor:overload
destructor
constructor:overload
destructor
79
constructor:overload
79
destructor
main scope end
'''
