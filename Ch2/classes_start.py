#
# Example file for working with classes
#

class myClass(): 
    def methord1(self): 
        print("myclass methord1")
    
    def methord2(self,someString):  
        print("myClass methord2" + someString)

class anotherClass(myClass): 
    def methord1(self): 
        # myClass.methord1(self)
        print("anotherClass methord1")
    
    def methord2(self,someString):  
        myClass.methord2(self,someString)
        print("anotherClass methord2"+ someString)


def main():
    c = myClass()
    c.methord1()
    c.methord2(" This is a String")
    
    c2 = anotherClass()
    c2.methord1()
    c2.methord2(" This is a String from methord2")

if __name__ == "__main__":
    main()
