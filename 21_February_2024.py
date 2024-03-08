'''
Task:- 
We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.
 If x has only  digit, then its super digit is .
 Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
For example, the super digit of  will be calculated as:
	super_digit(9875)   	9+8+7+5 = 29 
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2  
Example:
n = ' 9875'
k = 4

The number p is created by concatenating the string n k times so the initial p = 9875987598759875.

    superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = superDigit(8)
All of the digits of p sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it is the super digit.

Function Description:

Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):
 string n: a string representation of an integer
 int k: the times to concatenate n to make p
Returns:

int: the super digit of n repeated k times
'''

'''
Input Format:-

The first line contains two space separated integers, n and k.
'''

'''
Constraints:- 
 1 ≤ n < 10^100000
 1 ≤ k ≤ 10^5
'''

import math
import os
import random
import re
import sys

'''
Complete the 'superDigit' function below.
The function is expected to return an INTEGER.
The function accepts following parameters:
 1. STRING n
 2. INTEGER k
'''

def superDigit(n, k):
    
    '''
    Write your code here
    '''
    
    digits = map(int, list(n))
    return get_super_digit(str(sum(digits) * k))

def get_super_digit(p):
    if len(p) == 1:
        return int(p)
    else:
        digits = map(int, list(p))
        return get_super_digit(str(sum(digits)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
    
'''
Input (stdin):- 
148 3
'''

'''
Expected Output:- 
3 
'''