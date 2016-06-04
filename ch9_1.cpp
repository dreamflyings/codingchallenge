// ch9.1 : given staircase of n steps, count # ways child can run up stairs given
//         child can hop either 1, 2, or 3 steps

#include <iostream>
#include <list>
#include <map>
#include <gtest/gtest.h>

using namespace std;

/*
HINTS:
- child can reach n-th step from step(n-1), step(n-2), or step(n-3) ** this means sum **
- this is similar to fibonacci

f(0) == 0
f(1) == 1
f(2) == 2
f(3) == 4
f(4) == 1+2+4=7
f(4) == 2+4+7=13
*/

int count_ways(int n) {
    if (n < 0)
        return 0;
    else if (n == 0 || n == 1)
        return 1;
    else if (n == 2)
        return 2;
    else if (n == 3)
        return 4;
    else
        return count_ways(n-3) + count_ways(n-2) + count_ways(n-1);
}

TEST(ch9_1, basic) {
    ASSERT_EQ(count_ways(0), 1);
    ASSERT_EQ(count_ways(1), 1);
    ASSERT_EQ(count_ways(2), 2);
    ASSERT_EQ(count_ways(3), 4);
    ASSERT_EQ(count_ways(4), 7);
    ASSERT_EQ(count_ways(5), 13);
}

