a = [10, 20, 30, 50, 80, 70, 70, 80, 10]
a_dict={}
for i in a:
    if i in a_dict:
        a_dict[i] += 1
    else:
        a_dict[i] = 1
print(len(a_dict)) 

l=[]
count=0
for i in a:
    if i not in l:
        l.append(i)
        count += 1
print(len(l))