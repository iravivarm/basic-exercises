def swap_case(s):
    res=""
    for i in s:
        if i.islower():
            res=res+i.upper()
        elif i.isupper:
            res=res+i.lower()
    return res

s="HackerRank.com presents 'Pythonist 2'."
print(swap_case(s))