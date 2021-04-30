'''
@:function-to perform additions of two elements
@:param -there are two parameters a,b
@:return- it will return sum of the numbers
'''
def addition(a,b):
    return a+b
'''
@:function-to perform subtraction of two elements
@:param -there are two parameters a,b
@:return- it will return subtraction of the numbers
'''
def sub(a,b):
    return a-b
'''
@:function-to perform multiplication of two elements
@:param -there are two parameters a,b
@:return- it will return multiplication of the numbers
'''
def multiplication(a,b):
    return a*b
'''
@:function-to perform divison of two elements
@:param -there are two parameters a,b
@:return- it will return divison of the numbers
'''
def div(a,b):
    return a/b
'''
@:function-to perform modulo of two elements
@:param -there are two parameters a,b
@:return- it will return modulo of the numbers
'''
def mod(a,b):
    return a//b
'''
@:function-to perform power of two elements
@:param -there are two parameters a,b
@:return- it will return power of the numbers
'''
def power(a,b):
    return a**b
''' 
@:function-to perform square of element
@:param -there is one parameter a
@:return- it will return square of number
'''
def square(a):
    return a**2
def prev(res):
    with open("stepin.txt", "r") as file:
        prev = int(file.read())
        print(prev)
def printresult(res):
    print("result is:",res)
    return

print("press 1 - addition")
print("press 2 - subtraction")
print("press 3 - multiplication")
print("press 4 - division")
print("press 5 - quotient")
print("press 6 - square")
print("press 7 - power")
print("press 8-  previous element")
print("press 9- exit")
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
              res = mod(a, b)
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
          elif num==9:
              break
          elif num==8:
               # After every calculation store the result in a file
              printresult(res)
              with open("stepin.txt", "w") as file:
                  file.write(str(res))
          else:
              print("invalid entry")
              continue
    if num==8:
        break
