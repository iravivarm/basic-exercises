list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
###########################Using Loop ###################
result=[]
for i in range(len(list1)):
    if list1[i] != "":
        print(i)
        result.append(list1[i])
print(result)

########################## using inbuilt #####################

result1=list(filter(None, list1))
print(result1)