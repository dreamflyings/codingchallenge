// ch11.1: given two sorted vectors, where A has large enough buffer at end
//         to hold B.  write method to merge B into A in sorted order.

#include <iostream>
#include <vector>

#include <gtest/gtest.h>

using namespace std;

void sorted_merge(vector<int> &a, vector<int> &b) {
// move b into a, then sort?
}

TEST(ch11_1, basic) {
    vector<int> a = { 1, 4, 8, 10, 15 };
    vector<int> b = { 2, 5, 9, 11, 16 };
    vector<int> a_exp = { 1, 2, 4, 5, 8, 9, 10, 11, 15, 16 };
    a.resize(a.size()+b.size());
    sorted_merge(a, b);
    ASSERT_EQ(a, a_exp);
}

