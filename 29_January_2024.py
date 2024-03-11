'''
Task:- 
Given set S = {1, 2, 3, ..., N}. Find two integers, A and B (where A < B), from set S such that the value of A&B is the maximum possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.

Function Description: 
Complete the bitwiseAnd function in the editor below.

bitwiseAnd has the following paramter(s):
- int N: the maximum integer to consider
- int K: the limit of the result, inclusive

Returns: 
- int: the maximum value of A&B within the limit.
'''

'''
Input Format- 
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines defines a test case as 2 space-separated integers, N and K, respectively.
'''

'''
Constraints:- 
 1 ≤ T ≤ 10^3 
 2 ≤ N ≤ 10^3 
 2 ≤ K ≤ N
'''

'''
Sample Input:- 
STDIN   Function
-----   --------
3       T = 3
5 2     N = 5, K = 2
8 5     N = 8, K = 5
2 2     N = 8, K = 5
'''

'''
Sample Output:- 
1
4
0
'''

'''
Explanation:- 
N = 5, K = 2, S = {1, 2, 3, 4, 5}

All possible values of A and B are:
1. A = 1, B = 2, A&B = 0
2. A = 1, B = 3, A&B = 1
3. A = 1, B = 4, A&B = 0
4. A = 1, B = 5, A&B = 1
5. A = 2, B = 3, A&B = 2
6. A = 2, B = 4, A&B = 0
7. A = 2, B = 5, A&B = 0
8. A = 3, B = 4, A&B = 0
9. A = 3, B = 5, A&B = 1
10. A = 4, B = 5, A&B = 4

The maximum possible value of A&B that is also < (K = 2) is 1, so we print 1 on a new line.
'''

import math
import os
import random
import re
import sys

'''
Complete the 'bitwiseAnd' function below -
 The function is expected to return an INTEGER.
 The function accepts following parameters:
  1. INTEGER N
  2. INTEGER K
'''

def bitwiseAnd(N, K):

    '''
    Write your code here
   '''

    return (K-1 if ((K-1) | K) <= N else K-2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()

'''
Input (stdin):- 
3
5 2
8 5
2 2
'''

'''
Expected Output (stdout):- 
1
4
0
'''
