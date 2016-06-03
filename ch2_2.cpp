// ch2.2 : find nth to last element of linked list

#include <iostream>
#include <list>
#include <map>
#include <gtest/gtest.h>

using namespace std;

int find_nth_to_last(list<int> &l, int n) {
    auto slow = l.begin();
    auto fast = l.begin();

    for (auto i=0; i<n; i++) {
        ++fast;
        if (fast == l.end())
            return -1;
    }

    while (next(fast,1) != l.end()) {
        ++slow;
        ++fast;
    }
    return *slow;
}


TEST(ch2_2, basic) {
    list<int> tc;

    tc.push_back(1);
    tc.push_back(2);
    tc.push_back(3);
    tc.push_back(4);
    tc.push_back(5);
    tc.push_back(6);

    ASSERT_EQ(find_nth_to_last(tc, 0), 6);
    ASSERT_EQ(find_nth_to_last(tc, 1), 5);
    ASSERT_EQ(find_nth_to_last(tc, 5), 1);
    ASSERT_EQ(find_nth_to_last(tc, 7), -1);
}

