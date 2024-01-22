'''
Task:- Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you. You must:
1. Declare 3 variables: one of type int, one of type double, and one of type String.
2. Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your 3 variables.
3. Use the + operator to perform the following operations:
 1. Print the sum of i plus your int variable on a new line.
 2. Print the sum of d plus your double variable to a scale of one decimal place on a new line.
 3. Concatenate s with the string you read as input and print the result on a new line.
'''

'''
Input Format:-
The first line contains an integer that you must sum with i.
The second line contains a double that you must sum with d.
The third line contains a string that you must concatenate with s.
'''

'''
Output Format:- Print the sum of both integers on the first line, the sum of both doubles (scaled to 1 decimal place) on the second line, and then the two concatenated strings on the third line.
'''

'''
Sample Input:-
12
4.0
is the best place to learn and practice coding!
'''

'''
Sample Output:-
16
8.0
HackerRank is the best place to learn and practice coding!
'''

'''
Explanation:- 
When we sum the integers 4 and 12, we get the integer 16.
When we sum the floating-point numbers 4.0 and 4.0, we get 8.0.
When we concatenate HackerRank with is the best place to learn and practice coding!, we get HackerRank is the best place to learn and practice coding!.
'''

'''
Declare second integer, double, and String variables.
'''

i2 = None
d2 = None
s2 = None

'''
Read and save an integer, double, and String to your variables.
'''

i2 = int(input())
d2 = float(input())
s2 = str(input())

'''
Print the sum of both integer variables on a new line.
'''

print(i + i2)

'''
Print the sum of the double variables on a new line.
'''

print(d + d2)

'''
Concatenate and print the String variables on a new line
The 's' variable above should be printed first.
'''

print(s + s2)

'''
Input (stdin):-
12
4.0
is the best place to learn and practice coding!
'''

'''
Expected Output:-
16
8.0
HackerRank is the best place to learn and practice coding!
'''






