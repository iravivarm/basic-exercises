list1 = [5, 10, 15, 20, 25, 50, 20]
########################### Replace all 20s in list with 200 ###################
for i in range(len(list1)):

    if list1[i] == 20:
        print(i)
        list1[i]=200
print(list1)
######################################## replace First Occurance ########################
k=list1.index(20)
list1[k]=200
print(list1)
