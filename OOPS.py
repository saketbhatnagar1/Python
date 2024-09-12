#objects::
#list and strings are objects:

# class Student:
#     name = "Saket"
#creating a student object :Object is an instance of a class"
# s1 = Student()
# s1.name = "SAKEEE"
# print(s1.name)


# class car:
#     color = "white"
#     brand = "BMW"
# car1 = car()
# print(car1.color)

#INIT FUNCTION:: CONSTRUCTOR::
#Constructo function is invoked automatically at the time of invokation:

# car2 = car()
# print(car2.color)
# print(car2.brand)


#constructor always takes a self parametre:
class teacher():
    def __init__(self):
        print(self)
        print("NEW Teacher ADDED")

t1 = teacher()

#attributes::

#methods:
class airplane():
    

    def __init__(self,nam,age,marks):
        self.name = nam
        self.age = age
        self.marks = marks
    def getmarks(self):
        return self.marks

a320 = airplane("airbus",10,100)
print(a320.age)

class student:
    def __init__(self,name,marks):#assume marks is a list
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        length = len(self.marks)
        for value in self.marks:
            sum+=value
        print("HELLO ",self.name,"You'r average score is :",sum/length)

s1 = student("SAKET BHATNAGAR",[60,70,80,90])
s1.get_avg()

class student:

    @staticmethod #known as a decorator,that converts a normal function to a static method::
    def hello():
        print("Hello This is a static method")

    def __init__(self,name,marks):#assume marks is a list
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        length = len(self.marks)
        for value in self.marks:
            sum+=value
        print("HELLO ",self.name,"You'r average score is :",sum/length)

s1 = student("SAKET BHATNAGAR",[60,70,80,90])
s1.get_avg()
s1.hello()

#static methods::Methods that dont use the self parametre:


#Abstraction :Hiding implementation details of a class:
             #:Achieved through:
class Car:
    def __init__(self):
        self.acc = False
        self.brk = True
        self.clutch = False

    def start(self):
        self.clutch = True
        self.brk = False
        self.acc=True
        print("Car started")
car1 = Car()
car1.start()


#Encapsulation:

#Wrapping of data members and functions into a single unit:that is our object
class BankAccount():
    def __init__(self,accountNo,balance = 0):
        self.balance = balance
        self.accountNo = accountNo

    def setAccount(self,acn):
        self.accountNo = acn
    def credit(self,amount):
        
        

        balance+=amount

        

    def debit(self,amount):
        input_account = int(input("Enter Your Account Number: "))
        self.accountNo = input_account
        self.balance = self.balance-amount
        print(f"the balance remaining for  {self.accountNo} is {self.balance}")
        print("BALANCE :",self.balance)

b1 = BankAccount(20,100)
b1.debit(30)

