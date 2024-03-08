'''
Task:- 
Given an integer n, find each x such that:
 0 ≤ x ≤ n 
 n+x = n ⊕ x
where ⊕ denotes the bitwise XOR operator. Return the number of x's satisfying the criteria.

Example:
n = 4
There are four values that meet the criteria:
 4 + 0 = 4 ⊕ 0 = 4
 4 + 1 = 4 ⊕ 1 = 5
 4 + 2 = 4 ⊕ 2 = 6
 4 + 3 = 4 ⊕ 3 = 7
Return 4.

Function Description:
Complete the sumXor function in the editor below.

sumXor has the following parameter(s):
- int n: an integer

Returns:
- int: the number of values found
'''

'''
Input Format:- 
A single integer, n.
'''

'''
Constraints:- 
 0 ≤ n ≤ 10^15
'''

'''
Subtasks:- 
 0 ≤ n ≤ 100 for 60% of the maximum score.
'''

'''
Output Format:- 
Sample Input 0:
5
Sample Output 0:
2
Explanation 0:
For n = 5, the x values 0 and 2 satisfy the conditions:
 5 + 0 = 5, 5 ⊕ 0 = 5
 5 + 2 = 7, 5 ⊕ 2 = 7
'''

'''
Sample Input 1:-
10
Sample Output 1:
4
Explanation 1:
For n = 10, the x values 0, 1, 4, and 5 satisfy the conditions:
 10 + 0 = 10, 10 ⊕ 0 = 10
 10 + 1 = 11, 10 ⊕ 1 = 11
 10 + 4 = 14, 10 ⊕ 4 = 14
 10 + 5 = 15, 10 ⊕ 5 = 15
'''

import math
import os
import random
import re
import sys

'''
Complete the 'sumXor' function below.
The function is expected to return a LONG_INTEGER.
The function accepts LONG_INTEGER n as parameter.
'''

def sumXor(n):
    
    '''
    Write your code here
    '''
    
    return 2**bin(n)[2:].count('0') if n else 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = sumXor(n)
    fptr.write(str(result) + '\n')
    fptr.close()

'''
Input (stdin):- 
5
'''

'''
Expected Output:- 
2 
'''