#bring all the methods and variables from a parent class to the child class

from oopsdemo import Calculator

class childImpl(Calculator):
    num2=100

    def __init__(self):
        Calculator.__init__(self)

    def getcompletedata(self):
        return self.num2+self.num+ self.summation()


obj = childImpl()
print(obj.getcompletedata(self,5,10))
print(obj.getcompletedata())
