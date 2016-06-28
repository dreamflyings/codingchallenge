// ch11.2: Write a method to sort an vector of strings so that all the anagrams
//         are next to each other

#include <iostream>
#include <vector>

#include <gtest/gtest.h>

using namespace std;

namespace ch11_2 {

void string_sort(vector<string> &v) {
    for (unsigned i=0; i<v.size(); i++) {
        cout << v[i] << endl;
    }
}

TEST(ch11_2, basic) {
    vector<string> v;
    v.push_back("hello");
    v.push_back("iceman");
    v.push_back("world");
    v.push_back("cinema");
    string_sort(v);
}

} // namespace ch11_2
