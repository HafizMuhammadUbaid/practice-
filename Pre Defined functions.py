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
