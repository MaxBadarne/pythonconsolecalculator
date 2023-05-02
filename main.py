
def askme():
    x = input("what would you like to do ? (addition , substraction , multiplication , devide) \n")
    x.lower().strip()
    if(x == "addition"):
        addi()
    if(x == "substraction"):
        subs()
    if(x == "multiplication"):
        multip()
    if(x == "devide"):
        devide()
#comment
def addi():
    x =input("please pick the first number")
    y =input("please pick the second number")
    z = int(x) + int(y)
    print("the final result is : ", z)

def subs():
    x = input("please input the first number")
    y = input("please iput the second number")
    z = int(x) - int(y)
    print("the final result is : ",z)
def multip():
    x =input("please pick the first number")
    y =input("please pick the second number")
    z = int(x) * int(y)
    print("the final result is : ", z)

def devide():
    x = input("please input the first number")
    y = input("please iput the second number")
    z = int(x) / int(y)
    print("the final result is : ",z)

askme()