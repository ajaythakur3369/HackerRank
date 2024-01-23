'''
Task:- 
Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.
'''

'''
Input Format:- 
A single string, S.
'''

'''
Constraints:- 
 1 ≤ |S| ≤ 6, where |S| is the length of string S.
 S is composed of either lowercase letters (a - z) or decimal digits (0 - 9).
'''
 
'''
Output Format:- 
Print the parsed integer value of S, or Bad String if S cannot be converted to an integer.
'''

'''
Sample Input 0:- 
3
'''

'''
Sample Output 0:- 
3
'''

'''
Sample Input 1:- 
za
'''

'''
Sample Output 1:- 
Bad String
'''

'''
Explanation:- 
Sample Case () contains an integer, so it should not raise an exception when we attempt to convert it to an integer. Thus, we print the 3.
Sample Case 1 does not contain any integers, so an attempt to convert it to an integer will raise an exception. Thus, our exception handler prints Bad String.
'''

import math
import os
import random
import re
import sys

try:
    print(int(input().strip()))
except ValueError:
    print("Bad String")

'''
Input (stdin):- 
3
'''

'''
Expected Output:- 
3
'''





