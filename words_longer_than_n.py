n=4
str="Find the List of Words that are Longer than n from a given List of Words"

k=str.split(" ")
print(k)
for i in k:
    if len(i) > n:
        print(i)