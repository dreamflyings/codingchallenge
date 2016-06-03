// ch2.1 : remove duplicated from an unsorted linked list

#include <iostream>
#include <list>
#include <map>
#include <gtest/gtest.h>

using namespace std;

void remove_dup(list<int> &l) {
    map<int, int> dup_map;
    for (auto it=l.begin(); it!=l.end();) {
        if (dup_map.count(*it) != 1) {
            dup_map[*it] = 1;
            ++it;
        }
        else {
            it = l.erase(it);
        }
    }
}

void remove_dup_nobuf(list<int> &l) {
    auto slow = l.begin();
    while (slow != l.end()) {
        auto fast = next(slow, 1); // syntax!?
        while (fast != l.end()) {
            if (*fast == *slow) {
                fast = l.erase(fast);
            }
            else
                ++fast;
        }
        ++slow;
    }
}

TEST(ch2_1, basic) {
    list<int> tc;
    list<int> ex;

    tc.push_back(2);
    tc.push_back(4);
    tc.push_back(2);

    ex.push_back(2);
    ex.push_back(4);

    remove_dup(tc);
    ASSERT_EQ(tc, ex);
}

TEST(ch2_1, basic_nobuf) {
    list<int> tc;
    list<int> ex;

    tc.push_back(2);
    tc.push_back(4);
    tc.push_back(2);

    ex.push_back(2);
    ex.push_back(4);

    remove_dup_nobuf(tc);
    ASSERT_EQ(tc, ex);
}

TEST(ch2_1, triple) {
    list<int> tc;
    list<int> ex;

    tc.push_back(2);
    tc.push_back(2);
    tc.push_back(2);

    ex.push_back(2);

    remove_dup(tc);
    ASSERT_EQ(tc, ex);
}

TEST(ch2_1, triple_nobuf) {
    list<int> tc;
    list<int> ex;

    tc.push_back(2);
    tc.push_back(2);
    tc.push_back(2);

    ex.push_back(2);

    remove_dup_nobuf(tc);
    ASSERT_EQ(tc, ex);
}

