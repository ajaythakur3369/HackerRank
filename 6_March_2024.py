'''
Task:- 
You are a waiter at a party. There is a pile of numbered plates. Create an empty answers array. At each iteration, i, remove each plate from the top of the stack in order. Determine if the number on the plate is evenly divisible by the ith prime number. If it is, stack it in pile Bi. Otherwise, stack it in stack Ai. Store the values in Bi from top to bottom in answers. In the next iteration, do the same with the values in stack Ai. Once the required number of iterations is complete, store the remaining values in Ai in answers, again from top to bottom. Return the answers array.

Example:
A = [2, 3, 4, 5, 6, 7]
q = 3
An abbreviated list of primes is [2, 3, 5, 7, 11, 13]. Stack the plates in reverse order.
A0 = [2, 3, 4, 5, 6, 7]
answers = []

Begin iterations. On the first iteration, check if items are divisible by 2.
A1 = [7, 5, 3]
B1 = [6, 4, 2]

Move B1 elements to answers.
answers = [2, 4, 6]

On the second iteration, test if A1 elements are divisible by 3.
A2 = [7, 5]
B2 = [3]

Move B2 elmements to answers.
answers = [2, 4, 6, 3]

And on the third iteration, test if A2 elements are divisible by 5.
A3 = [7]
B3 = [5]

Move B2 elmements to answers.
answers = [2, 4, 6, 3, 5]

All iterations are complete, so move the remaining elements in A3, from top to bottom, to answers.
answers = [2, 4, 6 3, 5, 7]. Return this list.

Function Description:
Complete the waiter function in the editor below.
waiter has the following parameters:
 int number[n]: the numbers on the plates
 int q: the number of iterations

Returns:
int[n]: the numbers on the plates after processing
'''

'''
Input Format:- 
The first line contains two space separated integers, n and q.
The next line contains n space separated integers representing the initial pile of plates, i.e., A.
'''

'''
Constraints:- 
 1 ≤ n ≤ 5 x 10^4
 2 ≤ number[i] ≤ 10^4
 1 ≤ q ≤ 1200
'''

'''
Sample Input:- 
5 1
3 4 7 6 5
'''

'''
Sample Output:- 
4
6
3
7
5
'''

'''
Explanation:-
Initially:
A0 = [3, 4, 7, 6, 5]<-TOP
After 1 iteration:
A0 = []<-TOP
B1 = [6, 4]<-TOP
A1 = [5, 7, 3]<-TOP
We should output numbers in B1 first from top to bottom, and then output numbers in A1 from top to bottom.
'''

import math
import os
import random
import re
import sys

'''
Complete the 'waiter' function below.
The function is expected to return an INTEGER_ARRAY.
The function accepts following parameters:
 1. INTEGER_ARRAY number
 2. INTEGER q
'''

'''
Generate primes
'''

lower = 2
upper = 10000
prime = [i for i in range(lower, upper + 1) if all(i % j != 0 for j in range(2, i))]

def waiter(number, n, q):
    A = [number]
    B = []
    for i in range(q):
        A_pile = []
        B_pile = []
        while len(A[i]) != 0:
            n = A[i].pop()
            if n % prime[i] == 0:
                B_pile.append(n)
            else:
                A_pile.append(n)
        A.append(A_pile)
        B.append(B_pile)
    result = []
    for i in range(len(B)):
        if B[i] != []:
            result.extend(reversed(B[i]))
    for i in range(len(A)):
        if A[i] != []:
            result.extend(reversed(A[i]))
    return result   
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    number = list(map(int, input().rstrip().split()))
    result = waiter(number, n, q)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

'''
Input (stdin):- 
5 1
3 4 7 6 5
'''

'''
Expected Output:- 
4
6
3
7
5
'''