a="abc"
b="xyz"
def login():
    c=input("Enter ur user id : ")
    if c==a:
       passs()
    else:
        login()
def passs():
    d=input("Enter ur password : ")
    if d==b:
        print("login was success ")
    else:
        login()

login()

        
