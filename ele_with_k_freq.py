a=[2,4,4,5,5,6,8,9,8,9,10,10,10,12,8,5,5,5]
k=3

# count=0
# res=[]
# for i in a:
#     if i in res:
#         res.append(i)
#         count += 1
a_dict={}
for i in a:
    if i in a_dict:
        a_dict[i] += 1
    else:
        a_dict[i] = 1
print(a_dict)
ele=[]
for key,value in a_dict.items():
    if value >= k:
        ele.append(key)
print(ele)