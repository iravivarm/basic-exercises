import operator
a={2:40, 3:50,4:20}
sorted_a = sorted(a.items(), key=operator.itemgetter(1)) ##asecnding
sorted_d =sorted_d = sorted(a.items(), key=operator.itemgetter(1), reverse=True)##descending
print(sorted_d)