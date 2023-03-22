def function(num):
    num2=str(num*2)
    num=str(num)
    count=0
    for i in num:
       if i in num2:
          count+=1
       else:
          return False
    if len(str(num2))==len(str(num)):
        return True
print(function(2))
print(function(125874))
