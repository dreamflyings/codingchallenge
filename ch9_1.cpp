// ch9.1 : write method to count # of ways a child can run up the stairs, given
//         that child can hop either 1, 2, or 3 n

#include <iostream>
#include <list>
#include <map>
#include <gtest/gtest.h>

using namespace std;

/*
try with top-down recursion

f(1) = 1
f(2) = f(1) + 1 = 2
f(3) = f(2) + 1 = 4
f(4) = f(3) + f(2) + f(1) -- **child can reach the 4th floor, from either floor 1,2,3**
f(n) = f(n-1)

Total number of ways reaching the last step is the sum of the number of ways reaching each of the last three steps.

*/

int count_ways(int n) {
    if (n < 0)
        return 0;
    else if (n == 0)
        return 1;
    else
        return count_ways(n-3) + count_ways(n-2) + count_ways(n-1);
}

TEST(ch9_1, basic) {
    ASSERT_EQ(count_ways(0), 1);
    ASSERT_EQ(count_ways(1), 1);
    ASSERT_EQ(count_ways(2), 2);
    ASSERT_EQ(count_ways(3), 4);
    ASSERT_EQ(count_ways(4), 7);
}

