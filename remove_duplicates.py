a=[1,1,2,2,2,3,4,6,6,6,9,0,10]
a_dict={}
for i in a:
    if i in a_dict:
        a_dict[i] += 1
    else:
        a_dict[i] = 1
print(list(a_dict.keys()))