# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:47:06 2020

@author: mbolding3
"""


import bisect as b


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = [''] # empty string prevents search, startsWith
                          # methods from failing.
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        index = b.bisect_left( self.words, word )
        self.words.insert( index, word )
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        index = b.bisect_left( self.words, word )
        if index == len(self.words):
            return( False )
        if self.words[ index ] == word:
            return( True )
        return( False )
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        index = b.bisect_left( self.words, prefix )
        if index == len( self.words ):
            # subwords of a word are less than the word
            return( False )
        word = self.words[ index ]
        if prefix in word:
            if word.index( prefix ) == 0:
                return( True )
        return( False )
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)