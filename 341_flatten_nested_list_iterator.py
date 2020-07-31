# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Flattener(object):


    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = nestedList
        self.length = len(self.list)
        self.position = 0
        self.current = None


    def next(self):
        """
        :rtype: int
        """
        if self.current is None:
            try:
                nestedInt = self.list[self.position]
            except:
                return('F')
            if nestedInt.isInteger():
                self.position += 1
                return(nestedInt.getInteger())
            else:
                self.current = Flattener(nestedInt.getList())
                val = self.current.next()
                if not self.current.hasNext():
                    self.current = None
                    self.position += 1
                return(val)
        else:
            val = self.current.next()
            if not self.current.hasNext():
                self.current = None
                self.position += 1
            return(val)


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.position < self.length:
            return(True)
        else:
            return(False)


class NestedIterator(object):


    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flattener = Flattener(nestedList)
        self.output = []
        while self.flattener.hasNext():
            self.output.append(self.flattener.next())
        temp = []
        for item in self.output:
            if item is not 'F':
                temp.append(item)
        self.output = temp[::-1]


    def next(self):
        return(self.output.pop())


    def hasNext(self):
        if len(self.output) > 0:
            return(True)
        else:
            return(False)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())