n1=int(input("enter a value for n1"))
n2=int(input("enter a value for n2"))
array=[i for i in range(n1,n2+1)]
print(array)
result=[]
for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
