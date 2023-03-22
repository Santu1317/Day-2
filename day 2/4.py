from collections import Counter
list_of_marks=(12,11,2,25,6,2,10,18)
sum_of_list=sum(list_of_marks)
print(sum_of_list)
avg=sum_of_list/len(list_of_marks)
print(avg)
for i in list_of_marks:
    if i>avg:
        print(i)
result=sorted(list_of_marks)
print(result)
tup_freq=dict(Counter(list_of_marks))
print(tup_freq)

