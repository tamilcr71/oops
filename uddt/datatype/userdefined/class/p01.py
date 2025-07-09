#how to develop user defined datatype like class?

class p01: #declare user defined class(p01)
    #class indentation or scope or block has variables(p01,i,self.j,po1.k)
    #special method(__init__,__del__)and user-defined methods(readInput,show)
    i=5#initialize class variable:i

    def __init__(self):#declare default constructor using init attribute
        #define default constructor,it has instance and class variable initialization statements
        self.j=10;
            #here initialize variable(j)
            #instance variable alias name is object variable or non-static variable
            #instance variable develop self pre defined parameter

        p01.k=15
            #class variable initialixation statement syntax:<class-name>.<variable-name>=<value>
            #for example class name is p01 variable name is k varible value is 15
        print("default constructor process")

        return
            #jump statement terminate a subprogram like procedure,function,method or property
            #here terminate subprogram using return jump statement without return value
            #so which one sub-program did not return value is called procedure
            #therefore,which one sub-program return value then it is called function]
            #note:declare alais name is create
            #class inide declared sub-program called as member sub-program or method
            #class outside declared sub-program called as just sub-program
            #class outside declared procedure just called as procedure


        def __del__(self): #declare destructor usind del attribute
            #define constructor for erase instance and class variable from memory
            print("destructor process")
            return
        def readInput(self):
            try:
                self.j=int(input("enter j value"))
            except Exception as ex:
                self.j=0
                print("err:",ex)
            try:
                p01.k=int(input("enter k value"))
            except Exception as ex:
                p01.k=0
                print("err:",ex)
            return
        def show(self):
            print("i value",p01.i)
            print("j value",self.j)
            print("k value",p01.k)
            return           

obj=p01()
obj.show()
obj.readInput()
obj.show()
