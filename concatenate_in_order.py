list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

order_list=[]
for i  in range(len(list1)):
    for j in range(len(list2)):
        order_list.append(list1[i]+list2[j])
print(order_list)