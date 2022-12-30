''''#classes are user defined blue prints or prototype
#class will have methods,class variables, intance variable, constructor etc
#example- class of making a calculator

class Calculator:
    num=100  #Class variables: Variables inside class, they are constant no matter how many objects you create

    def __int__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b # here first and second number are Instance variable

        print("I am called automatically when object is created")

    def getData(self):
        print("Executing as method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num


obj = Calculator(2,3)   #syntax to create objects in python
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.summation())



#constructor name should be __init__
#self keyword is mandatory for calling variable names into method

#Note- Instance variable changes for every new object creation whereas class variables are constant
#You can never call a variable with its name instance variable will be called as self.variablename
#class variable will be called as classname.variablename or can also use self.variablename'''

class Calculator:
    num = 100  #class variables
    #default constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())

