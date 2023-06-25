class MyQueue(object):

    def __init__(self):
        self.stacklist = []
        # self.stacklist.append(None)
        # self.resultArray = []
        self.currentPosition = 0
        self.stacklist_length = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stacklist.append(x)
        self.stacklist_length = self.stacklist_length + 1
        # self.resultArray.append(None)
        # self.currentPosition = self.currentPosition + 1
        
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stacklist) == 0:
            return None
        # self.resultArray.append(self.stacklist[self.currentPosition])
        value = self.stacklist[self.currentPosition]
        self.currentPosition = self.currentPosition + 1
        self.stacklist_length = self.stacklist_length - 1
        return value
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stacklist) == 0:
            return None
        # self.resultArray.append(self.stacklist[self.currentPosition])
        return self.stacklist[self.currentPosition]
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.stacklist_length == 0:
            # self.resultArray.append(True)
            return True
        else:
            # self.resultArray.append(False)
            return False
            
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()