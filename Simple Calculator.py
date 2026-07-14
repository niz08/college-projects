#Simple Calculator

def add(a,b):
    s=a+b
    return s
def subtract(a,b):
    su=a-b
    return su
def multiply(a,b):
    mu=a*b
    return mu
def divide(a,b):
    di=a/b
    return di
while True:
    print("Welcome to Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    ch=int(input("what is your choice? [1-5]"))
    if ch == 5:
        break
    a=int(input("Enter Number 1:"))
    b=int(input("Enter Number 2:"))
    if ch == 1:
        print(add(a,b))
    elif ch == 2:
        print(subtract(a,b))
    elif ch == 3:
        print(multiply(a,b))
    elif ch == 4:
        print(divide(a,b))
