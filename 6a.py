import re 
str = '11001001' 
match = re.search('1(0+)1', str) 
# If-statement after search() tests if it succeeded 
if match: 
  print('found') ## 'found word:cat' 
else: 
  print('did not find') 
def patternCount(str): 
    # Variable to store the last character 
    last = str[0] 
    i = 1; counter = 0 
    while (i < len(str)): 
          
        # We found 0 and last character was '1', 
        # state change 
        if (str[i] == '0' and last == '1'): 
            while (str[i] == '0'): 
                i += 1 
                # After the stream of 0's, we got a '1', 
                # counter incremented 
                if i < len(str) and str[i] == '1': 
                    counter += 1