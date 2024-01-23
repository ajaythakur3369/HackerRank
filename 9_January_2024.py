'''
Function Description:- 
Complete the factorial function in the editor below. Be sure to use recursion.
factorial has the following paramter:
 int n: an integer
'''

'''
Returns:- 
 int: the factorial of n
'''

'''
Input Format:-
A single integer, n (the argument to pass to factorial).
'''

'''
Constraints:-
 2 ≤ n ≤ 12
 Your submission must contain a recursive function named factorial.
 '''
 
 '''
Sample Input:-
3
'''

'''
Sample Output:-
6
'''

'''
Explanation:- 
Consider the following steps. After the recursive calls from step 1 to 3, results are accumulated from step 3 to 1.
1. factorial(3) = 3 x factorial(2) = 3 x 2 = 6 
2. factorial(2) = 2 x factorial(1) = 2 x 1 = 2 
3. factorial(1) = 1 
'''

import math
import os
import random
import re
import sys

'''
Complete the 'factorial' function below.
The function is expected to return an INTEGER.
The function accepts INTEGER n as parameter.
'''

def factorial(num):
    return 1 if num == 1 else factorial(num - 1) * num

print(factorial(int(input())))

'''
Input (stdin):- 
3
'''

'''
Expected Output:- 
6
'''








