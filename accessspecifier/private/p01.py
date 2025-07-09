class counter:
    __secretcount=0

    def count(self):
        self.__secretcount += 1
        print(self.__secretcount)


c1=counter()
c1.count()
c1.count()
#print(c1.__secretcount)
#attribute error counter object has no attribute '__secretcount'
#print(self.__secretcount)
#attribute error counter object has no attribute '__secretcount'


#private methods/variables-ascessible only in their own class
#starts with two underscores
