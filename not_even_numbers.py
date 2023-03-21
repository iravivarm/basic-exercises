n = [7,32,81,20,25,14,23,27]

odd_num=[]
for i in n:
    if i%2 !=0:
        odd_num.append(i)

print(odd_num)
#################### list cpomprehension #################
odd_num=[i for i in n if i%2!=0]