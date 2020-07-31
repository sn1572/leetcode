class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        try:
            oldMin = self.minimum[-1]
            if x < oldMin:
                self.minimum.append(x)
            else:
                self.minimum.append(oldMin)
        except:
            self.minimum.append(x)


    def pop(self):
        """
        :rtype: void
        """
        self.minimum.pop()
        return(self.stack.pop())        


    def top(self):
        """
        :rtype: int
        """
        return(self.stack[-1])


    def getMin(self):
        """
        :rtype: int
        """
        return(self.minimum[-1])



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()