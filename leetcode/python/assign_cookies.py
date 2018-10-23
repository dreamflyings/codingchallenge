"""
https://leetcode.com/problems/assign-cookies/description/

Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie. Each child i has a greed
factor gi, which is the minimum size of a cookie that the child will be content
with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j
to the child i, and the child i will be content. Your goal is to maximize the
number of your content children and output the maximum number.

Note:
* You may assume the greed factor is always positive.
* You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]

Output: 1

Explanation:

You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only
make the child whose greed factor is 1 content.  You need to output 1.

Example 2:
Input: [1,2], [1,2,3]

Output: 2

Explanation:

You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the
children, You need to output 2.

---

greeds = [3,2,1]

sizes = [1,1]

gi  g  si  s  h | gi' g' si' s' h'
0   3  0   1  0   1   2  0   1  0
1   2  0   1  0 | 2   1  1   1  1


s < g !happy, will never satisfy child

g >= s happy


greeds = [2, 1]
sizes =  [3, 2, 1]

gi  g  si  s  h | gi' g' si' s' h'
0   2  0   3  0

"""


class Solution:
    def findContentChildren(self, greeds, sizes):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        num_sizes = len(sizes)
        sizes.sort(reverse=True)
        print(sizes)

        num_greeds = len(greeds)
        greeds.sort(reverse=True)
        print(greeds)

        happy = 0

        gi = 0
        si = 0

        while gi < num_greeds and si < num_sizes:
            g = greeds[gi]
            s = sizes[si]

            if s >= g:
                # size greater or equal than greed
                gi += 1
                si += 1
                happy += 1
            else:
                # will never satisfy child
                gi += 1

        return happy
