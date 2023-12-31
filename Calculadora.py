#-Calculator-#
#--#
#-Introduction and selection of the math operation
def math_operation():
  while 1==1:
    print("Choose a number to do a math operation")
    print("1- addition")
    print("2- substration")
    print("3- multiplication")
    print("4- divition")
    try:
     value = int(input())
    except ValueError:
     value = 0
    if (value>= 1) and (value <=4):
     if value == 1:
      value = addition()
     if value == 2:
      value = substration()
     if value == 3:
      value = multiplication()
     if value == 4:
      value = division()
    break
  return value

#-program for addition
def addition():
    try: 
      n1 = int(input("put any number "))
      n2 = int(input("Put another number again "))
      answer = n1 + n2
      print (answer)
    except ValueError:
     print ("Plese insert only a number ")
    except Exception as a:
     print (" UNKNOW ERROR", a)
     print (addition())
#-program for substration
def substration():
    try:
      n1 = int(input("put any number "))
      n2 = int(input("Put another number again "))
      answer = n1 - n2
      print (answer)
    except ValueError:
     print ("Plese insert only a number ")
    except Exception as a:
     print (" UNKNOW ERROR", a)
     print (substration())
#-program for multiplication
def multiplication():
    try:
      n1 = int(input("put any number "))
      n2 = int(input("Put another number again "))
      answer = n1 * n2
      print (answer)
    except ValueError:
     print ("Plese insert only a number ")
    except Exception as a:
     print (" UNKNOW ERROR", a)
     print (multiplication())
#-program for division
def division():
    try:
      n1 = int(input("put any number"))
      n2 = int(input("Put another number again "))
      answer = n1 / n2
      print (answer)
    except ValueError:
     print ("Plese insert only a number ")
    except Exception as a:
     print (" UNKNOW ERROR", a)
     print (division())
#-Main Program
math_operation()