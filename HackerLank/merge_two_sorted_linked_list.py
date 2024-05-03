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
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def mergeLists(head1, head2):
    # 병합된 리스트를 관리할 새로운 SinglyLinkedList 인스턴스 생성
    merged_list = SinglyLinkedList()

    # 두 리스트 모두를 순회하며 각 노드를 비교
    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            merged_list.insert_node(head1.data)
            head1 = head1.next
        else:
            merged_list.insert_node(head2.data)
            head2 = head2.next
    
    # head1 또는 head2 중 하나가 먼저 끝에 도달하면 나머지 리스트를 병합 리스트에 추가
    while head1 is not None:
        merged_list.insert_node(head1.data)
        head1 = head1.next
    
    while head2 is not None:
        merged_list.insert_node(head2.data)
        head2 = head2.next

    # 병합된 리스트의 head 반환
    return merged_list.head

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
