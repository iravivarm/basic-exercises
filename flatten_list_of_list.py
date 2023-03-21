ori_list = [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
flatten_list=[]
for su_list in ori_list:
    for items in su_list:
        flatten_list.append(items)
print(flatten_list)