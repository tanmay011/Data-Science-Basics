# Python3 program to find nearest greater value 
min1 = 10**9
_count = 0
  
# Find all the possible permutation of Value A. 
def permutation(str1, i, n, p): 
    global min1, _count 
    if (i == n): 
          
        # Convert into Integer 
        str1 = "".join(str1) 
        q = int(str1) 
  
        # Find the minimum value of A  
        # by interchanging the digits 
        # of A and store min1. 
        if (q - p > 0 and q < min1): 
            min1 = q 
            _count = 1
    else: 
        for j in range(i, n + 1): 
              
            # Swap two character) 
            str1[i], str1[j] = str1[j], str1[i] 
            permutation(str1, i + 1, n, p) 
            str1[i], str1[j] = str1[j], str1[i] 
  
    return min1 
  
# Driver code 
A = 456
B = 500
  
# Convert integer value into to 
# find all the permutation of the number 
str2 = str(A) 
str1 = [i for i in str2] 
le = len(str1) 
  
h = permutation(str1, 0, le - 1, B) 
  
# count=1 means number greater than B exists 
if _count == 1: 
    print(h) 
else: 
    print(-1) 