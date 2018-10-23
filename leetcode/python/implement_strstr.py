# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_h = len(haystack)
        len_n = len(needle)
        h = 0
        n = 0
        first = None

        if haystack == "" and needle == "":
            return 0

        if needle == "":
            return 0

        while h < len_h:
            h_val = haystack[h]
            n_val = needle[n]

            if h_val == n_val and n == len_n - 1:
                return h - len_n + 1
            elif h_val == n_val:
                if first == None:
                    first = h
                n += 1
                h += 1
            elif first != None:
                n = 0
                h = first + 1
                first = None
            else:
                h += 1

        return -1
