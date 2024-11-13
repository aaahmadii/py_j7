d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

merged_dict = d1.copy()  

for key, value in d2.items():
    if key in merged_dict:
        merged_dict[key] += value  
    else:
        merged_dict[key] = value 

print(merged_dict)
