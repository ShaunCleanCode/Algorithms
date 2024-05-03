# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import os
import random
import re
import sys

class MyQueue(object):
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                
        print(self.stack2[-1])
            
    def enqueue(self, value):
        self.stack1.append(value)
        
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            self.stack2.pop()
    

if __name__ =="__main__":
    number_of_queries=int(input())
    queue=MyQueue()
    
    for _ in range(number_of_queries):
        query=[]
        query=list(map(int, input().split()))
        
        if len(query)==1:
            if query[0]==2:
                queue.dequeue()
            else:
                queue.peek()
        else:
            queue.enqueue(query[1])


    

















    
