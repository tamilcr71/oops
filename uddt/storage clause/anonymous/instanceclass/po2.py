#differenciate class or static and instance or object or member variable?

class p01:
    i=5
    def __init__(self):
        self.j=10;
        p01.k=15
        print("default constrctor process")
        return
    def __del__(self):
        print("destructor proccess")
        return
print("main indentation starts here")
obj=p01()
print("i value",p01.i)
print("j value",obj.j)
print("k value",p01.k)

obj=None

print("main indentation ends here")

'''
main indentation starts here
default constrctor process
i value 5
j value 10
k value 15
destructor proccess
main indentation ends here
'''
