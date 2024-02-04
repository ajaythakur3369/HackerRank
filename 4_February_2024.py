'''
Task:- 
You will be given a list of 32 bit unsigned integers. Flip all the bits (1 → 0 and 0 → 1) and return the result as an unsigned integer.

Example:
n = 9(10) [of base 10]
9(10) [of base 10] = (1001)2. We're working with 32 bits, so:
(000 ... 0001001)2 [of base 2] = 9(10) [of base 10]
(111 ... 1110110)2 [of base 2] = (4294967286)10 [of base 10]

Return 4294967286 

Function Description:
Complete the flippingBits function in the editor below.

flippingBits has the following parameter(s):
 int n: an integer

Returns: 
 int: the unsigned decimal integer result
'''

'''
Input Format:- 
The first line of the input contains q, the number of queries.
Each of the next q lines contain an integer, n, to process.
'''

'''
Constraints:- 
 1 ≤ q ≤ 100
 0 ≤ n < 2^32 
'''

'''
Sample Input:- 
3 
2147483647 
1 
0
'''

'''
Sample Output:- 
2147483648 
4294967294 
4294967295
'''

'''
Explanation:- Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001 and doing the flipping we get 11111111111111111111111111111110 which in turn is 4294967294.
'''

import math
import os
import random
import re
import sys

'''
Complete the 'flippingBits' function below.
The function is expected to return a LONG_INTEGER.
The function accepts LONG_INTEGER n as parameter.
'''

def flippingBits(n):
    
'''
Write your code here 
'''

    return ~n+2**32

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        fptr.write(str(result) + '\n')
    fptr.close()

'''
Input (stdin):- 
3
2147483647
1
0
'''

'''
Expected Output:- 
147483648
4294967294
4294967295
'''