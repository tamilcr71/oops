class A:

    def show(self):
        print("show:A")
        return

class B(A):
    def show(self):
        super().show()
        print("show:B")
        return

obj=B()
obj.show()

'''
show:A
show:B
'''
