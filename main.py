#def greeting(name):
#  print("Hello, " + name)
#
#  guestname = input("what is your name: ")
#
#greeting(guestname)




def addnumbers(num1, num2):
  print(num1 + num2)

def subnumbers(num1, num2):
  print(num1 - num2)

num1 = int(input("enter number 1: "))
operator = input("add or subtract: ")
num2 = int(input("enter number 2: "))

if operator.lower() == "+":
  addnumbers(num1, num2)
elif operator.lower() == "-":
  subnumbers(num1, num2)
else:
  print("thats not an operator")