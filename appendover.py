#prompt the user list of integers.For all values greater than 100,store"over"innstead
n=int(input("total number of integers:"))
list1=[]
for i in range (n):
    a=int(input("Enter an integer:"))
    if a<100:
        list1.append(a)
    else:
        list1.append("over")
print(list1)
