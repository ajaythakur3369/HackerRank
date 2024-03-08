'''
Task:-
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Example:
q = [1, 2, 3, 4, 5, 6, 7, 8]
If person 5 bribes person 4, the queue will look like this: 1, 2, 3, 4, 5, 6, 7, 8. Only 1 bribe is required. Print 1.
q = [4, 1, 2, 3]
Person 4 had to bribe 3 people to get to the current position. Print Too chaotic.

Function Description:
Complete the function minimumBribes in the editor below.

minimumBribes has the following parameter(s):
 int q[n]: the positions of the people after all bribes
'''

'''
Returns:- 
No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than 2 people.
'''

'''
Input Format:- 
The first line contains an integer t, the number of test cases.

Each of the next t pairs of lines are as follows:
- The first line contains an integer t, the number of people in the queue
- The second line has n space-separated integers describing the final state of the queue.
'''

'''
Constraints:- 
 1 ≤ t ≤ 10
 1 ≤ n ≤ 10^5 
'''

'''
Subtasks:- 
For 60% score 1 ≤ n ≤ 10^3
For 100% score 1 ≤ n ≤ 10^5
'''

'''
Sample Input:- 
STDIN       Function
-----       --------
2           t = 2
5           n = 5
2 1 5 3 4   q = [2, 1, 5, 3, 4]
5           n = 5
2 5 1 3 4   q = [2, 5, 1, 3, 4]
'''

'''
Sample Output:- 
3
Too chaotic
'''

'''
Explanation:- 
Test Case 1:
The initial state:
After person 5 moves one position ahead by bribing person 4:
Now person 5 moves another position ahead by bribing person 3:
And person 2 moves one position ahead by bribing person 1:
So the final state is 2, 1, 5, 3, 4 after three bribing operations.

Test Case 2:
No person can bribe more than two people, yet it appears person 5 has done so. It is not possible to achieve the input state.
'''

import math
import os
import random
import re
import sys

'''
Complete the 'minimumBribes' function below.
The function accepts INTEGER_ARRAY q as parameter.
'''

def minimumBribes(q):
    
    '''
    Write your code here
    '''
    
    chaotic = ''
    num_swaps = 0
    for i in range(len(q)):
        if(q[i]>i+3):
            chaotic += 'Too chaotic'
        for j in range(max(0,q[i]-2),i):
            if(q[i]<q[j]):
                num_swaps+=1

    if('Too chaotic' in chaotic):
        print('Too chaotic')
    else:
        print(num_swaps)

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)

'''
Input (stdin):- 
2
5
2 1 5 3 4
5
2 5 1 3 4
'''

'''
Expected Output:- 
3
Too chaotic
'''