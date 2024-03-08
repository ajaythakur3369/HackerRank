'''
Task:- 
Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

Example:
headA refers to 1 → 3 → 7 → NULL 
headB refers to 1 → 2 → NULL 
The new list is 1 → 1 → 2 → 3 → 7 → NULL 

Function Description:
Complete the mergeLists function in the editor below.

mergeLists has the following parameters:
 SinglyLinkedListNode pointer headA: a reference to the head of a list
 SinglyLinkedListNode pointer headB: a reference to the head of a list

Returns:
SinglyLinkedListNode pointer: a reference to the head of the merged list
'''

'''
Input Format:- 
The first line contains an integer t, the number of test cases.

The format for each test case is as follows:
The first line contains an integer n, the length of the first linked list.
The next n lines contain an integer each, the elements of the linked list.
The next line contains an integer m, the length of the second linked list.
The next m lines contain an integer each, the elements of the second linked list.
'''

'''
Constraints:-
 1 ≤ t ≤ 10
 1 ≤ n,m ≤ 1000
 1 ≤ list[i] ≤ 1000, where list[i] is the ith element of the list.
'''

'''
Sample Input:-
1
3
1
2
3
2
3
4
Sample Output
1 2 3 3 4 
'''

'''
Explanation:- 
The first linked list is: 1 → 3 → 7 → NULL
The second linked list is: 3 → 4 → NULL
Hence, the merged linked list is: 1 → 2 → 3 → 3 → 4 → NULL 
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
Complete the mergeLists function below.
For your reference:
SinglyLinkedListNode:
    int data
    SinglyLinkedListNode next
'''

def mergeLists(headA, headB):
    if headA == None:
        return headB
    if headB == None:
        return headA
    
    if headA.data <= headB.data:
        head = headA
        headA = headA.next
    else:
        head = headB
        headB = headB.next
    
    current = head
    while headA != None or headB != None:
        if headA == None:
            current.next = headB
            break
        if headB == None:
            current.next = headA
            break
        if headA.data <= headB.data:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next
        current = current.next
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())
        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())
        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
        llist3 = mergeLists(llist1.head, llist2.head)
        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()

'''
Input (stdin):- 
1
3
1
2
3
2
3
4
'''

'''
Expected Output:- 
1 2 3 3 4 
'''