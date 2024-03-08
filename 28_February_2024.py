'''
Task:- 
Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.

Example:
head references the list 1 → 2 → 3 → NULL

Manipulate the next pointers of each node in place and return head, now referencing the head of the list 3 → 2 → 1 → NULL.

Function Description:
Complete the reverse function in the editor below.

reverse has the following parameter:
SinglyLinkedListNode pointer head: a reference to the head of a list

Returns:
SinglyLinkedListNode pointer: a reference to the head of the reversed list
'''

'''
Input Format:-
The first line contains an integer t, the number of test cases.

Each test case has the following format:

The first line contains an integer n, the number of elements in the linked list.
Each of the next n lines contains an integer, the data values of the elements in the linked list.
'''

'''
Constraints:- 
 1 ≤ t ≤ 10 
 1 ≤ n ≤ 1000
 1 ≤ list[i] ≤ 1000, where list[i] is the ith element in the list.
'''

'''
Sample Input:- 
1
5
1
2
3
4
5
Sample Output:
5 4 3 2 1 
'''

'''
Explanation:-
The initial linked list is: 1 → 2 → 3 → 4 → 5 → NULL.
The reversed linked list is: 5 → 4 → 3 → 2 → 1 → NULL.
'''

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

'''
Complete the 'reverse' function below.
The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
For your reference:
SinglyLinkedListNode:
    int data
    SinglyLinkedListNode next
'''

def reverse(llist):
    
    '''
    Write your code herenext
    '''
    
    nxt = None
    while llist:
        tmp = llist.next
        llist.next = nxt
        nxt = llist
        llist = tmp
    return nxt
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

'''
Input (stdin):- 
1
5
1
2
3
4
5
'''

'''
Expected Output:- 
5 4 3 2 1
'''