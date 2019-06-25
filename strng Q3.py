s=input("enter string")
p="ly"
r="ing"
if len(s)<3:
    print(s)
elif s.endswith("ing"):
    print(s+p)
else:
     print(s+r)
    
