"""
https://leetcode.com/problems/add-and-search-word-data-structure-design/description/

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string
containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """

        l = len(word)
        for i in range(2**l): # 0,1,2,3, etc.
            bits = "{0:b}".format(i).zfill(l) # 000, 001, 010, 011, etc.

            wword = []
            for i in range(l):
                bit = bits[i]
                char = word[i]
                wword.append("." if bit == "0" else char)
            y = "".join(wword)
            #print(y)
            self.set.add(y)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return word in self.set

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

