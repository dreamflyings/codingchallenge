"""
https://leetcode.com/problems/find-and-replace-in-string/description/
"""


class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        d = {}
        for index, source, target in zip(indexes, sources, targets):
            replace = S[index:index + len(source)] == source
            if replace:
                d[index] = source, target

        s = []
        i = 0
        while i < len(S):
            if i in d:
                source, target = d[i]
                s.append(target)
                i += len(source)
            else:
                s.append(S[i])
                i += 1

        return "".join(s)
