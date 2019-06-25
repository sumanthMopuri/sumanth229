#list comprehension
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[3*i for i in list1]
print(list2)

#without using comprehension
list1=[1,2,3,4,5,6]
list2=[]
for i in list1:
    print(i*3)
