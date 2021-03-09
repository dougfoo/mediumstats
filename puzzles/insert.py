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

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    node = head
    while (node):
        if (node.next is None or node.next.data > data):
            newnode = DoublyLinkedListNode(data)
            if (node.data > data):  # swap node vals
                newnode.data = node.data
                node.data = data
            newnode.next = node.next
            newnode.prev = node

            if (node.next is not None):
                node.next.prev = newnode

            node.next = newnode
            break

        node = node.next

    return head

if __name__ == '__main__':
    llist = DoublyLinkedList()
    inputs =  [1, 3, 4, 10]

    for i in inputs:
        llist.insert_node(i)

    data = 0

    llist1 = sortedInsert(llist.head, data)

    print_doubly_linked_list(llist1, ' ')

