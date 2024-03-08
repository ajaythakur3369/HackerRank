'''
Task:- 
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

Example:
s = abc 
This is a valid string because frequencies are {a:1, b:1, c:1}.
s = abcc
This is a valid string because we can remove one c and have 1 of each character in the remaining string.
s = abccc
This string is not valid as we can only remove 1 occurrence of c. That leaves character frequencies of {a:1, b:1, c:2}.

Function Description:
Complete the isValid function in the editor below.
isValid has the following parameter(s):
 string s: a string

Returns:
string: either YES or NO
'''

'''
Input Format:- 
A single string s.
'''

'''
Constraints:-
 1 ≤ |s| ≤ 10^5
 Each character s[i] ∈ ascii [a - z]
'''

'''
Sample Input:- 
aabbcd
'''

'''
Sample Output:- 
NO
'''

'''
Explanation:- 
2 is the minimum number of removals required to make it a valid string. It can be done in following two ways:
Remove c and d to get aabb.
Or remove a and b to get abcd.
'''

import math
import os
import random
import re
import sys

'''
Complete the 'isValid' function below.
The function is expected to return a STRING.
The function accepts STRING s as parameter.
'''

def isValid(s):
    
    '''
    Write your code here
    '''
    
    if len(s) <= 1:
        return "YES"
        
    freq = {}
    
    for i in s:
        freq[i] = freq.get(i, 0) + 1
    
    a = freq[s[0]]
    count_a = 0
    b = 0
    count_b = 0
    for i in freq:
        if freq[i] == a:
            count_a += 1
        elif not b:
            b = freq[i]
            count_b +=1
        elif freq[i] == b:
            count_b += 1
        else:
            return "NO"
    
    if count_a == 1:
        if a - b == 1 or a == 1:
            return "YES"
    elif count_b == 1:
        if b - a == 1 or b == 1:
            return "YES"
    elif count_a == 0 or count_b == 0:
        return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()

'''
Input (stdin):- 
aabbcd
'''

'''
Expected Output:- 
NO
'''