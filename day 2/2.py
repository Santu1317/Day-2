n1=int(input("enter a value for n1"))
n2=int(input("enter a value for n2"))
result=[]
for i in range(n1,n2+1):
    result.append(i)
print(result)
result=[i for i in range(n1,n2+1)]
print(result)



