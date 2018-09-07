// ch1.3: given two strings, with a method to decide if one is a permutation of
//        the other

/*
with permutations, order does matter when counting
with combinations, order does not matter when counting

string of length n has n! permutations

what about whitespace?
*/

#include <gtest/gtest.h>

#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

namespace ch1_3 {

int is_permutation(const string &a, const string &b) {
  if (a.size() != b.size())
    return 0;

  string a_tmp = a;
  string b_tmp = b;
  std::sort(a_tmp.begin(), a_tmp.end());
  std::sort(b_tmp.begin(), b_tmp.end());
  return (a_tmp == b_tmp) ? 1 : 0;
}

TEST(ch1_3, basic) {
  ASSERT_EQ(is_permutation("abc", "cba"), 1);
  ASSERT_EQ(is_permutation("abc", "baa"), 0);
}

} // namespace ch1_3
