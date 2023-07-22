class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = None
        self.minstack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min == None:
            self.min = val
            self.minstack.append(val)
        else:
            if val <= self.min:
                self.min = val
                self.minstack.append(val)
        return None
        

    def pop(self):
        """
        :rtype: None
        """
        value = self.stack.pop()
        if value == self.minstack[-1]:
            self.minstack.pop()
            if len(self.minstack) > 0:
                self.min = self.minstack[-1]
            else:
                self.min = None
            
        return value
        

    def top(self):
        """
        :rtype: int
        """
        value = self.stack[-1]
        return value

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()