list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# for i in range(len(list1)):
#     print(i, list1[i])
print(list1[2][1][2])
# list1[2][1][2].extend(sub_list)
# print(list1)
sub_list.extend(list1)
print(sub_list)
