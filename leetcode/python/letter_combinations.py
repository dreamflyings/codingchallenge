"""
### Problem ###
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

### Notes ###
23
abc, def


abc -> a, def -> ad,ae,af
       b, def -> bd,be,bf
       c, def -> cd,ce,cf

234
abc,def,ghi

level   0      1         2
        abc -> a, def -> a, d, ghi
                         a, e, ghi
                         a, f, ghi
               b, def
               c, def
"""

import unittest


class LetterCombinationsTest(unittest.TestCase):
    def letterCombinations(self, digits):
        if digits == "": return []

        digit_to_letters = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"],
                            6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}

        letters = list(map(lambda x: digit_to_letters[int(x)], digits))  # [[a,b,c],[d,e,f]]

        num_levels = len(letters)

        result = []

        def f(level, wip):
            letters_at_level = letters[level]
            num_letters_at_level = len(letters_at_level)
            last_level = level == num_levels - 1

            for i in range(num_letters_at_level):
                this_letter = letters_at_level[i]
                if last_level:
                    result.append(wip + [this_letter])
                else:
                    f(level + 1, wip + [this_letter])

        f(0, [])



        return list(map(lambda x: "".join(x), result))

    def test_basic(self):
        input = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(expected, self.letterCombinations(input))

    def test_three_digits(self):
        input = "234"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(expected, self.letterCombinations(input))

    def test_bounds(self):
       input = ""
       expected = []
       self.assertEqual(expected, self.letterCombinations(input))
