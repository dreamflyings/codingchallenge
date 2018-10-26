"""
https://leetcode.com/problems/utf-8-validation/description/

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.
                                                           ^^       ^        1B

Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.
                                                            ^^^ 3B

Algorithm :

For each byte:
    count # of leading 1s, convert to string
    next N-1 bytes have 2 MSB equal 10

Count # of leading 1s

11000101 >> 7 = 00000001 n = 1
11000101 >> 1 = 01100010

01100010 >> 7 = 00000001 n = 2
01100010 >> 1 = 00110001

00110001 >> 7 = 00000000 break

Example 1:

     ones  msb10 msb0  | remain'
197  2     F     F       1
130  -     T     F       0
1    -     F     T       0

Example 2:

     ones  msb10 msb0  | remain'
235  3     F     F       2
140  -     T     F       1
4    -     T     T     | 1 - error msb0 & !remain


Example 3:

248,130,130,130

248 ones = 5, next 4 must have MSB 10

     ones  msb10 msb0  | remain'
248  5     F     F       4
130  -     T     0     | 3
130  -     T     0     | 2
130  -     T     0     | 1

remain != 0 return False

Example 5:

     ones  msb10 msb0  | remain'
255  8     F     F       8


Example 6:

     ones  msb10 msb0  | remain'
145  1     T     F

Example 7:

[250,145,145,145,145]

    ones  msb10 msb0  | remain'
250 5     F     F       4
145 -     T     F       3
145 -     T     F       2
145 -     T     F       1
145 -     T     F       0

"""


class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        def countLeading1s(x):
            n = 0
            x = x & 255
            while (x >> 7) > 0:
                x = x << 1
                x = x & 255
                n += 1
            return n

        remain = 0

        for byte in data:
            ones = countLeading1s(byte)
            msb_is_10 = (byte >> 6) & 0b10
            msb_is_0 = (byte >> 7) & 0

            if remain == 0:
                if ones == 1 and msb_is_10:
                    return False
                elif ones > 4:
                    return False
                elif ones > 1:
                    remain = ones - 1
            else:
                if msb_is_0:
                    return False
                elif msb_is_10:
                    remain -= 1
                else:
                    return False

        return remain == 0
