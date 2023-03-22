def translate(dict,list):
    list2=[]
    for i in list:
        list2.append(dict[i])
    return list2    
dict={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list=["merry","and"]
print(translate(dict,list))
