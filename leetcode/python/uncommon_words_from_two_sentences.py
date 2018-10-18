"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

We are given two sentences A and B.  (A sentence is a string of space separated
words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does
not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

---

"s z z z s"
"s z ejt"

unique_a = s
unique_b = s z ejt
"""

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        all_words = set()
        for word in A.split(" ") + B.split(" "):
            if word not in all_words:
                all_words.add(word)


        word_count_a = {}
        for word in A.split(" "):
            if word not in word_count_a:
                word_count_a[word] = 1
            else:
                word_count_a[word] += 1


        word_count_b = {}
        for word in B.split(" "):
            if word not in word_count_b:
                word_count_b[word] = 1
            else:
                word_count_b[word] += 1

        words_a = set(A.split(" "))
        words_b = set(B.split(" "))
        ans = []

        for word in list(all_words):
            word_in_a = word in words_a
            word_in_b = word in words_b

            # does not appear in other
            a_but_not_in_b = word_in_a and not word_in_b
            b_but_not_in_a = word_in_b and not word_in_a

            if a_but_not_in_b or b_but_not_in_a:
                # exactly once in one of the sentances
                if a_but_not_in_b:
                    if word_count_a[word] == 1:
                        ans.append(word)

                if b_but_not_in_a:
                    if word_count_b[word] == 1:
                        ans.append(word)

        return ans

