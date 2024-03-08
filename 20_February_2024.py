'''
Task:- 
Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.

Example:
arr = [5, 6, 8, 11]
8 is between two subarrays that sum to 11.
arr = [1]
The answer is [1] since left and right sum to 0.

You will be given arrays of integers and must determine whether there is an element that meets the criterion. If there is, return YES. Otherwise, return NO.

Function Description:
Complete the balancedSums function in the editor below.

balancedSums has the following parameter(s):
 int arr[n]: an array of integers

Returns:
string: either YES or NO
'''

'''
Input Format:- 
The first line contains T, the number of test cases.
The next T pairs of lines each represent a test case.
- The first line contains n, the number of elements in the array arr.
- The second line contains n space-separated integers arr[i] where 0 ≤ i ≤ n.
'''

'''
Constraints:- 
 1 ≤ T ≤ 10 
 1 ≤ n ≤ 10^5 
 1 ≤ arr[i] ≤ 2x10^4 
 0 ≤ i < n
'''

'''
Sample Input:- 
2
3
1 2 3
4
1 2 3 3
'''

'''
Sample Output:- 
NO
YES
'''

'''
Explanation:- 
For the first test case, no such index exists.
For the second test case, A[0]+A[1] = A[3], therefore index 2 satisfies the given conditions.
'''

import math
import os
import random
import re
import sys

'''
Complete the 'balancedSums' function below.
The function is expected to return a STRING.
The function accepts INTEGER_ARRAY arr as parameter.
'''

def balancedSums(arr):
    
    '''
    Write your code here
    '''
    
    res = 'NO'
    right = sum(arr)
    left = 0
    
    for el in arr:
        right -= el
        
        if right == left:
            res = 'YES'
            break
            
        left += el      
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        fptr.write(result + '\n')
    fptr.close()
