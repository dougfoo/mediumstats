#!/bin/python3

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
        fptr.write(' ' + str(id(node)) + ':')
        fptr.write(str(node.data) + ' ')

        node = node.next

        if node:
            fptr.write(sep)


# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1: SinglyLinkedListNode, head2: SinglyLinkedListNode):
    m = {}
    cur = head1
    while (cur):
        m[id(cur)] = head1.data
        cur = cur.next

    cur = head2
    while (cur):
        if (m.get(id(cur)) != None):
            return cur.data
        cur = cur.next


if __name__ == '__main__':
    fptr = sys.stdout # open(os.environ['OUTPUT_PATH'], 'w')

    inputs = [1,2,3,1,2,3,1,1]

    tests = int(inputs.pop(0))

    index = int(inputs.pop(0))

    llist1_count = int(inputs.pop(0))

    llist1 = SinglyLinkedList()

    for _ in range(llist1_count):
        llist1_item = int(inputs.pop(0))
        llist1.insert_node(llist1_item)

    llist2_count = int(inputs.pop(0))

    llist2 = SinglyLinkedList()

    for _ in range(llist2_count):
        llist2_item = int(inputs.pop(0))
        llist2.insert_node(llist2_item)

    ptr1 = llist1.head;
    ptr2 = llist2.head;

    for i in range(llist1_count):
        if i < index:
            ptr1 = ptr1.next

    for i in range(llist2_count):
        if i != llist2_count - 1:
            ptr2 = ptr2.next

    ptr2.next = ptr1

    result = findMergeNode(llist1.head, llist2.head)

    fptr.write(str(result) + '\n')

    fptr.close()