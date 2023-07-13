# OOP Assignment

# Challenge 1: Square Numbers and Return their Sum:

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        print("SqSum of the values are: ")


    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2


x = int(input("Enter the value x: "))
y = int(input("Enter the value y: "))
z = int(input("Enter the value z: "))

sqsum1 = Point(x,y,z)
print(sqsum1.sqSum())    
#---------------------------------------------------------------------------------------------------

# Challenge 2: Implement a Calculator Class
# Write a Python class called Calculator by completing the tasks below

class Calculator:

    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("calculator operation is")
   
    def add(self):
        return self.num1 + self. num2 
    def subtract(self):
        return self.num2 - self. num1
    def multiply(self):
        return self.num1 * self. num2
    def divide(self):
        return self.num2 / self. num1

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))    

obj = Calculator(num1,num2)   
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())
#------------------------------------------------------------------------------------------------------

# Challenge 3. Implement the Complete Student Class

class Student:
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    def getName(self):
        return self.name
    def getRollNumber(self):
        return self.rollnumber
    
    @classmethod
    def setname(cls, new_name):
        cls.name = new_name
        return new_name
    
    def setRollNumber(cls, new_rollNumber):
        cls.rollnumber = new_rollNumber
        return new_rollNumber
    
obj = Student("Mike","185")
print(obj.name,obj.rollnumber)
print(obj.setname("BIG MIKE"))
print(obj.setRollNumber("25"))
#------------------------------------------------------------------------------------------------------
# Challenge 4. Implement a Banking Account

class Account:
    def __init__(self, title, Balance):
        self.title = title
        self.Balance = Balance
    def myfunc(self):
        return f"Account{self.title, self.Balance}"

class SavingsAccount(Account):
    def __init__(self, title, Balance, interestRate):
        Account.__init__(self, title, Balance)
        self.interestRate = interestRate
    def interst(self):
        return f"Account{self.title, self.Balance, self.interestRate}"

title = input("Enter the name: ")
Balance = int(input("Enter the balance: "))
interestRate = int(input("Enter the interest rate: "))

obj1 = Account(title,Balance)
print(obj1.myfunc())

obj2 = SavingsAccount(title,Balance,interestRate)
print(obj2.interst()) 
#-------------------------------------------------------------------------------------------------------------

#Challenge 5: Handling a Bank Account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return f"Account{self.title, self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return (f"Rs.{amount} is deposited in your account.")

    def withdrawal(self, amount):
        if amount > self.balance:
            return ("Insufficient balance.")
        else:
            self.balance -= amount
            return (f"Rs.{amount} has been withdrawn from your account.")

class SavingsAccount(Account):
    def __init__(self, title, balance,interestRate):
        Account. __init__(self, title, balance)
        self.interestRate = interestRate

    def interestAmount(self,interestRate,balance):
        return (interestRate * balance)/(100) 


obj1 = Account("Ashish",5000)

print(obj1.deposit(500))    
print(obj1.withdrawal(2000))   
print(obj1.getBalance())

obj2 = SavingsAccount('Ashish',2000, 5)
print(obj2.interestAmount(5,2000))