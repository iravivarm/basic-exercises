employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# print(type(dict(employees)))
# default_dict={}
# for j in employees:
#     for i in defaults.items():

#         default_dict.update({j:i})

# print(default_dict)

res=dict.fromkeys(employees,defaults)
print(res)