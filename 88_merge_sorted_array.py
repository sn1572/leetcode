class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        try:
            nums2[0] #Checks for an empty nums2.
            keepGoing = True
            indexOfComparison = m-1
            indexOfInsertion = n+m-1
            while keepGoing:
                num2 = nums2.pop()
                num1 = nums1[indexOfComparison]
                if num2 >= num1:
                    nums1[indexOfInsertion] = num2
                else:
                    nums2.append(num2)
                    nums1[indexOfInsertion] = num1
                    indexOfComparison -= 1
    
                #Note that indexOfInsertion >= 0
                indexOfInsertion -= 1
    
                #If nums2 is exhausted, stop.
                try:
                    nums2[0]
                except:
                    keepGoing = False
    
                #If nums1 is exhausted, stop.
                if indexOfComparison < 0:
                    keepGoing = False
    
            try:
                nums2[0]
                keepGoing = True
            except:
                pass
    
            while keepGoing:
                num2 = nums2.pop()
                nums1[indexOfInsertion] = num2
                indexOfInsertion -= 1
                try:
                    nums2[0]
                except:
                    keepGoing = False
        except:
            #If nums2 is empty, do nothing.
            pass