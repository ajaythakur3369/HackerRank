'''
Task:- 
You will be given a list of integers, arr, and a single integer k. You must create an array of length k from elements of arr such that its unfairness is minimized. Call that array arr'. Unfairness of an array is calculated as
max(arr') - min(arr') 
Where:
- max denotes the largest integer in arr'.
- min denotes the smallest integer in arr'.

Example:
arr = [1, 4, 7, 2]
k = 2
Pick any two elements, say arr' = [4, 7].
unfairness = max(4, 7), min(4, 7) = 7 - 4 = 3
Testing for all pairs, the solution [1, 2] provides the minimum unfairness.

Note: 
Integers in arr may not be unique.

Function Description:
Complete the maxMin function in the editor below.
maxMin has the following parameter(s):
 int k: the number of elements to select
 int arr[n]:: an array of integers

Returns:
 int: the minimum possible unfairness
'''

'''
Input Format:- 
The first line contains an integer n, the number of elements in array arr.
The second line contains an integer k.
Each of the next n lines contains an integer arr[i] where 0 ≤ i ≤ n.
'''

'''
Constraints:- 
 2 ≤ n ≤ 10^5 
 2 ≤ k ≤ n 
 0 ≤ arr[i] ≤ 10^9 
'''

'''
Sample Input:- 
Sample Input #01: 
10
4
1
2
3
4
10
20
30
40
100
200
'''

'''
Sample Output:-
Sample Output #01:
3
'''

'''
Explanation:-
Explanation #01:
Here K = 4; selecting the 4 integers 1, 2, 3, 4, unfairness equals

max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3
'''

import math
import os
import random
import re
import sys

'''
Complete the 'maxMin' function below.
The function is expected to return an INTEGER.
 The function accepts following parameters:
  1. INTEGER k
  2. INTEGER_ARRAY arr
'''

def maxMin(k, arr):
    
    '''
    Write your code here
    '''
    
    arr.sort()
    result = arr[k-1] - arr[0]
    for i in range(n-k+1):
        if arr[i+k-1] - arr[i] < result:
            result = arr[i+k-1] - arr[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    k = int(input().strip())
    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()

'''
Input (stdin):- 
7
3
10
100
300
200
1000
20
30
'''

'''
Expected Output:- 
20
'''