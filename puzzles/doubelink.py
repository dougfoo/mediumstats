#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

    def __repr__(self):
       return f'Node {self.data} < { self.prev.data if self.prev else 0 } > { self.next.data if self.next else 0 }'

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)


# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):   # single linked list
    stk = list()

    while (head != None):
        stk.append(head)
        head = head.next

    h = stk.pop()
    head = h
    while stk:
        n = stk.pop()
        h.next = n
        h = n
    h.next = None
    return head

def reverse1(head):  # iterative ?
    cur = head
    last = head
    while cur != None:
        tmp_next = cur.next
        cur.next = cur.prev
        cur.prev = tmp_next

        last = cur
        cur = tmp_next
        print(cur)

    return last


if __name__ == '__main__':
    t = [1, 2, 3, 4]

    llist = DoublyLinkedList()

    for t_itr in t:
        llist_item = t_itr
        llist.insert_node(llist_item)

    print_doubly_linked_list(llist.head, ' ')

    llist1 = reverse(llist.head)

    print_doubly_linked_list(llist1, ' ')
    print('exit')