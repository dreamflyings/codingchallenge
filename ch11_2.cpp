// ch11.2: Write a method to sort an vector of strings so that all the anagrams
//         are next to each other

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <gtest/gtest.h>

using namespace std;

namespace ch11_2 {

int is_anagram(const string &a, const string &b) {
    string a_tmp = a;
    string b_tmp = b;

    std::sort(a_tmp.begin(), a_tmp.end());
    std::sort(b_tmp.begin(), b_tmp.end());
    return (a_tmp == b_tmp) ? 1 : 0;
}

// this is far from the most effective algorithm ...
void string_sort(vector<string> &v) {
    for (unsigned i=0; i<v.size()-1; i++) {
        for (unsigned j=i+1; j<v.size(); j++) {
            if (is_anagram(v[i], v[j])) {
                // swap i+1 and j
                string tmp;
                tmp = v[j];
                v[j] = v[i+1];
                v[i+1] = tmp;
            }
        }
    }
}

TEST(ch11_2, basic) {
    vector<string> v = {"hello", "iceman", "world", "cinema"};
    vector<string> exp = {"hello", "iceman", "cinema", "world"};
    string_sort(v);
    ASSERT_EQ(v, exp);
}

TEST(ch11_2, two_anagrams) {
    vector<string> v = {"a", "b", "ab", "cd", "ab", "cd"};
    vector<string> exp = {"a", "b", "ab", "ab", "cd", "cd"};
    string_sort(v);
    ASSERT_EQ(v, exp);
}

} // namespace ch11_2
