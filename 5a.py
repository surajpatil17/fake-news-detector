import re  
def search(ip_str):  
	re_exp = '[A-Z]+[a-z]+$' 
	if re.search(re_exp, ip_str):  
		print('Yes, the required sequence exists!') 
	else:  
		print('No, the required sequence does not exists!') 

ip_str = input("Enter the string: ") 
search(ip_str) 