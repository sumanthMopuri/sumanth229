list2=[]
list3=[]
n=int(input("enter list size"))
for i in range(n):
    l=input("enter the string")
    list2.append(l)
for i in range(len(list2)):
    list3.append(len(list2[i]))
list3.sort()
print(list3[-1])
