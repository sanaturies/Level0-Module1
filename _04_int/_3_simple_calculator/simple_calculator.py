"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

x=9
y=8
operation='o'
if operation=='+':
  print(x+y)
elif operation=='-':
  print(x-y)
elif operation=='*':
  print(x*y)
elif operation=='/':
  print(x/y)
else:
    print('not supported')
