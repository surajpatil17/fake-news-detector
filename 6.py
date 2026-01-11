dict1 = {'stdno': '532', 'stuname': 'naveen', 'stuage': '21', 'stucity': 'hyderabad'}
print("\ndictionary is:", dict1)
print("\nstudent name is:", dict1['stuname'])
print("\nstudent city is:", dict1['stucity'])
print("\nall keys in dictionary")
for x in dict1:
	print(x)
print("\nall values in dictionary")
for x in dict1:
	print(dict1[x])
dict1["phno"] = 6884762859
print("updated dictionary is:", dict1)
dict1["stuname"] = "jerry"
print("updated dictionary is:", dict1)
dict1.pop("stuage")
print("updated dictionary is:", dict1)
print("length of dictionary is:", len(dict1))
dict2 = dict1.copy()
print("\nnew dictionary is:", dict2)
dict1.clear()
print("updated dictionary is:", dict1)