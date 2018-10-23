"""
https://leetcode.com/problems/reverse-vowels-of-a-string/description/

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"

Example 2:

Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".


h e l l o
0 1 2 3 4
  *     *
1 4

l e e t c o d e
0 1 2 3 4 5 6 7

1 2 5 7

1 7
2 5

l e o t c e d e
0 1 5 3 4 2 6 7

"""


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        def isVowel(c):
            return c in set(["a", "e", "i", "o", "u"])

        vowels = []

        for ci in range(len(s)):
            c = s[ci]
            if isVowel(c.lower()):
                vowels.append(ci)

        num_vowels = len(vowels)
        print(vowels)

        l = list(s)  # strings are immutable

        for vi in range(int(num_vowels / 2)):
            li = vowels[vi]
            ri = vowels[num_vowels - vi - 1]
            print(li, ri)

            tmp = l[li]
            l[li] = l[ri]
            l[ri] = tmp

        return "".join(l)
