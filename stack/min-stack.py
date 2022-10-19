"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack or val <= self.minstack[-1]:
            self.stack += [val]
            self.minstack += [val]
        else:
            self.stack += [val]
            
    def pop(self):
        """
        :rtype: None
        """
        stack_val = self.stack.pop()
        if (stack_val == self.minstack[-1]):
            self.minstack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        
"""
Solution:
    1. Use a list for the stack itself; the start will be the bottom and the end will be the top
    2. Keep a stack that keeps track of your minimum value; same orientation as other stack
    2. For push, if stack is empty, add to both stacks; if value is less than the top item in the minimum stack, add to both; else add to normal stack
    3. For top, return the last element in the list
    4. For pop, remove the last element in the list; if this item is also the top element in the min stack, then we remove it from there as well
    5. For getMin, return the top of the min stack
"""