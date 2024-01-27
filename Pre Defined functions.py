import math
x = math.sqrt(64)
print(x)

import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

import math
x = math.pi
print(x)

import datetime
x = datetime.datetime.now()
print(x)

import datetime
x = datetime.datetime(2024,1,27)
print(x)

def evenOdd(x):
          if(x % 2 == 0):
             print("even")
          else:
            print("odd")
#Driver code
evenOdd(2)
evenOdd(3)



# Python program to demonstrate
# default arguments
def myFun(x, y = 50):
  print("x: ", x)
  print("y: ", y)
#Driver code
myFun(10)


def student(firstname, lastname):
 print(firstname, lastname)
#keyword argumennts
student(firstname = 'Geeks',lastname = 'practice')
student(lastname = 'practice',firstname = 'geeks')

def student(firstname, lastname):
 print(firstname, lastname)
#keyword argumennts
student(firstname = 'Geeks',lastname = 'practice')
student(lastname = 'practice',firstname = 'Geeks')

def add_numbers (num1, num2):
    sum = num1 + num2
    print("sum: ",sum)
    
add_numbers(5,4)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

ages = {"Muhammad Ubaid": 15, "Musaddiq": 30}
print(ages["Muhammad Ubaid"])
    
