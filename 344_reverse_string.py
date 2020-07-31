# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 08:47:20 2019

@author: mbolding3

"""
# cd C:\Users\mbolding3\Documents\Python Scripts\tensorFlow
# tensorboard --logdir tf_logs/

class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        L = len(s)
        for i in range(L//2):
            s[i], s[~i] = s[~i], s[i]