'''
Task:- 
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:
 It contains no unmatched brackets.
 The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

Function Description:
Complete the function isBalanced in the editor below.
isBalanced has the following parameter(s):
 string s: a string of brackets
 
Returns:
 string: either YES or NO
'''
 
'''
Input Format:-
The first line contains a single integer n, the number of strings.
Each of the next n lines contains a single string s, a sequence of brackets.
'''

'''
Constraints:-
 1 ≤ n ≤ 10^3
 1 ≤ |s| ≤ 10^3, where |s| is the length of the sequence.
 All chracters in the sequences ∈ { {, }, (, ), [, ] }.
'''

'''
Output Format:- 
For each string, return YES or NO.
'''

'''
Sample Input:- 
STDIN Function ----- -------- 3 n = 3 {[()]} first s = '{[()]}' {[(])} second s = '{[(])}' {{[[(())]]}} third s ='{{[[(())]]}}'
'''

'''
Sample Output:- 
YES
NO
YES
'''

'''
Explanation:- 
1. The string {[()]} meets both criteria for being a balanced string.
2. The string {[(])} is not balanced because the brackets enclosed by the matched pair { and } are not balanced: [(]).
3. The string {{[[(())]]}} meets both criteria for being a balanced string.
'''

import math
import os
import random
import re
import sys

BRACKETS_MAP = {
    '[': ']',
    '{': '}',
    '(': ')',
}
def isOpen(bracket):
    return bracket in BRACKETS_MAP.keys()

def isClose(bracket):
    return bracket in BRACKETS_MAP.values()

'''
Complete the 'isBalanced' function below.
The function is expected to return a STRING.
The function accepts STRING s as parameter.
'''

def isBalanced(s):
    stack = []
    for bracket in s:
        if(isOpen(bracket)):
            stack.append(bracket)
        elif(isClose(bracket)):
            if(stack == [] or bracket != BRACKETS_MAP.get(stack.pop())):
                return ("NO")
    if(stack != []):
        return ("NO")
    return ("YES")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()