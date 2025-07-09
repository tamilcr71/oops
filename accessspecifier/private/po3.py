class student:
    __a=10
    b=20

    def __private_method(self):
        print("private method is called")

    def public_method(self):
        self.__private_method()
        print("public method is called")
        print("a=",self.__a)

s1=student()
#print("a=",s1.__a) #genrate error
print("b=",s1.b)
#s1.__private_method() #genrate error
s1.public_method()

'''
b= 20
private method is called
public method is called
a= 10
'''
