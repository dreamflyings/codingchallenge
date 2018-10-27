"""
https://leetcode.com/problems/generalized-abbreviation/description/

Write a function to generate the generalized abbreviations of a word.

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### Notes ###

* Find length use bitmask
* shift the mask left
mask[i] = 0
mask[i+1] = 1
* reconstruct string

l = 4
mask_width = 4-i

i mw j msk   i+1
---------------
0 4  0 0001  1
     1 0010
     2 0100
     3 1000

1 3  0 001   2
     1 010
     2 100

2 2  0 01    3
     1 10

3 1  0 1     4


# ARGH! I did fully understand the problem. Did not communicate the implementation and WASTED 20 min.

"""


class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        l = len(word)
        abbrvs = []

        for i in range(l):
            mask_width = l - i
            mask = [0] * l

            for j in range(mask_width):
                mask[j] = 1
                abbrv = []

                wi = 0
                for use in mask:
                    print(use, wi)
                    if use:
                        abbrv.append(str(i + 1))
                        wi += i + 1
                    else:
                        if wi < l:
                            abbrv.append(word[wi])
                            wi += 1

                abbrvs.append("".join(abbrv))

                mask[j] = 0

        return abbrvs
