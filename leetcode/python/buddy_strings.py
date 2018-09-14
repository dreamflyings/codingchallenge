import unittest


class BuddyStringsTest(unittest.TestCase):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        aa = [A[i] for i in range(len(A))]
        bb = [B[i] for i in range(len(B))]

        swap_indices = list(map(lambda x: x[1], filter(lambda x: x[0] == True, map(lambda x: (x[0] != x[1], x[2]),
                                                                                   zip(aa, bb, range(len(A)))))))

        num_swaps = len(swap_indices)

        if num_swaps == 2:
            tmp = aa[swap_indices[0]]
            aa[swap_indices[0]] = aa[swap_indices[1]]
            aa[swap_indices[1]] = tmp
            return True if aa == bb else False
        elif num_swaps == 1:
            return False
        elif num_swaps == 0:
            # only true if duplicate character, I needed a hint for this case
            seen = set()
            for a in A:
                if a in seen:
                    return True
                else:
                    seen.add(a)
            return False
        else:
            return False

    def test_basic(self):
        self.assertFalse(self.buddyStrings("aa", "aabbbb"))
        self.assertFalse(self.buddyStrings("", "aa"))
        self.assertTrue(self.buddyStrings("ab", "ba"))
        self.assertFalse(self.buddyStrings("aa", "ba"))
        self.assertTrue(self.buddyStrings("aaaaaaabc", "aaaaaaacb"))
        self.assertFalse(self.buddyStrings("abcd", "dcba"))

    def test_hard(self):
        self.assertTrue(self.buddyStrings("aa", "aa"))
        self.assertTrue(self.buddyStrings("aaaabc", "aaaabc"))
        self.assertFalse(self.buddyStrings("ab", "ab"))
