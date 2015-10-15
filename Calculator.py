#Returns Sum
def add(x,y):
    return x + y
#Returns Differnce
def sub(x,y):
    return x - y
#Returns Product
def mul(x,y):
    return x * y
#Returns Quotient
def div(x,y):
    return x / y
#Input
def put():
    global operation
    operation= input("What do you want to do? (+,-,*,/)")

    if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        print ("You must enter a valid operation.")
        put()

    else:
        calc()
#Number input
def calc():

    num1 = int(input("Enter First Number:"))
    num2= int(input("Enter Second Number:"))

    if(operation == "+"):
        print (add(num1,num2))

    elif(operaion == "-"):
        print (sub(num1,num2))

    elif(operation == "*"):
        print (mul(num1,num2))

    else:
        print (div(num1,num2))

put()
