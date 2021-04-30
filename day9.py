def addition(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def div(a,b):
    return a/b
def quo(a,b):
    return a//b
def power(a,b):
    return a**b
def square(a):
    return a**2
def prev(res):
    with open("Memory.txt", "r") as file:
        prev = int(file.read())
        print(prev)
print("press 1 - addition")
print("press 2 - subtraction")
print("press 3 - multiplication")
print("press 4 - division")
print("press 5 - quotient")
print("press 6 - square")
print("press 7 - power")
print("press 8- exit")
while True:
    while True:
          print("choose your choice and press number :")
          num = int(input())
          if num == 1:
             print("enter input values of a,b are :")
             a = int(input())
             b = int(input())
             res = addition(a, b)
             print("result is :", res)
          elif num == 2:
             print("enter input values of a,b are :")
             a = int(input())
             b = int(input())
             res = sub(a, b)
             print("result is :", res)
          elif num == 3:
            print("enter input values of a,b are :")
            a = int(input())
            b = int(input())
            res = multiplication(a, b)
            print("result is :", res)
          elif num == 4:
            print("enter input values of a,b are :")
            a = int(input())
            b = int(input())
            res = div(a, b)
            print("result is :", res)

          elif num == 5:
              print("enter input values of a,b are :")
              a = int(input())
              b = int(input())
              res = quo(a, b)
              print("result is :", res)
          elif num == 6:

              print("enter input value of a:")
              a = int(input())
              res = square(a)
              print("result is :", res)
          elif num == 7:

              print("enter input values of a,b are :")
              a = int(input())
              b = int(input())
              res = power(a, b)
              print("result is :", res)
          elif num==8:
              break
          elif num==9:
              ac=prev(res)
              print("previous element",ac)
          else:
              print("invalid entry")
              continue
    if num==8:
        break
