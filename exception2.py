a=int(input("enter a value"))
b=int(input("enter b value"))
try:
    print(b/a)
    print(c/a)
except ZeroDivisionError as b:
     print("error: ",b)
except(ZeroDivisionError, NameError):
    print("alternate block")
finally:
    print("this is final")
    
