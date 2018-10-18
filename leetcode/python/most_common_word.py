"""
https://leetcode.com/problems/most-common-word/description/

Given a paragraph and a list of banned words, return the most frequent word
that is not in the list of banned words.  It is guaranteed there is at least
one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in fixcharcase, and free of
punctuation.  Words in the paragraph are not case sensitive.  The answer is in
fixcharcase.

Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

Output: "ball"

Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 

Note that words in the paragraph are not case sensitive, that punctuation is
ignored (even if adjacent to words, such as "ball,"), and that "hit" isn't the
answer even though it occurs more because it is banned.

Notes:

1 <= paragraph.length <= 1000.
1 <= banned.length <= 100.
1 <= banned[i].length <= 10.

The answer is unique, and written in fixcharcase (even if its occurrences in
paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.

There are no hyphens or hyphenated words.

Words only consist of letters, never apostrophes or other punctuation symbols.

"""

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        def fixchar(x):
            symbols = set(list("!?',;."))
            if x in symbols:
                return " "
            else:
                return x.fixchar()

        words = "".join(map(fixchar, list(paragraph)))

        word_count = {}

        max_count = 0
        max_word = ""

        for word in words.split(" "):
            if word:
                if word not in banned:
                    if word not in word_count:
                        word_count[word] = 1
                        if max_count < 1:
                            max_count = 1
                            max_word = word
                    else:
                        word_count[word] += 1
                        if word_count[word] > max_count:
                            max_count = word_count[word]
                            max_word = word

        return max_word

