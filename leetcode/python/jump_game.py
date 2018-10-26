"""
### Problem ###
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false

Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

### Notes ###

Backtracking with caching.  Not fast enough to pass worst case.

Obviously, this is a dynamic programming problem, for which I have zero
experience with.

The solution mentions a greedy solution where we track the left-most GOOD
position as a separate variable.  If we can reach a GOOD index, then our
position is also good.

Iterate right to left, tracking left-most good pointer.

[9, 4, 2, 1, 0, 2, 0]
 0  1  2  3  4  5  6

if i + nums[i] >= left_most: left_most = i

i lm
6  -        good
5  6 3+2>=5 good
4  5 4+0<5  bad
3  5 3+1<5  bad
2  5 2+2<4  bad
1  5 1+4>=5 good
0  1 0+9>=1 good


[2, 3, 1, 1, 4]

i l i+nums[i]
4 -
3 4 3+1=4>=4 good
2 3 2+1=3>=3 good
1 2 1+3>=2   good
0 1 0+2>=1   good

[3, 2, 1, 0, 4]
 0  1  2  3  4
i lm i+nums[i]
4 -           good
3 4 3+0<4     bad
2 4 2+1<4     bad
1 4 1+2<4     bad
0 1 0+3<4     bad

"""

import unittest


class JumpGameTest(unittest.TestCase):
    def canJumpFrom(self, nums, pos, cache):
        if pos == len(nums) - 1: return True

        if pos in cache:
            return cache[pos]

        max_jump = nums[pos]
        reachable = False
        for i in range(pos + 1, pos + max_jump + 1):
            reachable = self.canJumpFrom(nums, i, cache)

            if i not in cache:
                cache[i] = reachable

            if reachable: break

        return reachable

    def canJump(self, nums):
        # cache = {}
        # if len(nums) == 1: return True
        # if len(nums) > 1 and nums[0] == 0: return False
        #
        # return self.canJumpFrom(nums, 0, cache)

        num_nums = len(nums)
        left_most = num_nums - 1
        good = True

        for i in reversed(range(num_nums - 1)):
            if nums[i] + i >= left_most:
                left_most = i
                good = True
            else:
                good = False

        return good

    # def test_timeout(self):
    #     self.assertFalse(self.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))

    def test_basic_true(self):
        self.assertTrue(self.canJump([2, 3, 1, 1, 4]))

    def test_basic_false(self):
        self.assertFalse(self.canJump([3, 2, 1, 0, 4]))

    def test_basic_null(self):
        self.assertTrue(self.canJump([0]))

    def test_basic_skip_over(self):
        self.assertTrue(self.canJump([2, 0, 0]))

    def test_basic_never_leave(self):
        self.assertFalse(self.canJump([0, 2, 3]))

    def test_basic_greater(self):
        self.assertTrue(self.canJump([1, 2, 3]))  # ???

    def test_basic_greater_2(self):
        self.assertTrue(self.canJump([1, 3, 2]))

    def test_basic_zero_at_tail(self):
        self.assertFalse(self.canJump([1, 0, 1, 0]))
