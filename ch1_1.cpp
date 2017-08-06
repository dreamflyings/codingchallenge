#include <iostream>
#include <string>
#include <gtest/gtest.h>

using namespace std;

int is_uniq(string str) {
  int seen[256];

  // GOTCHA: this seems to be required
  for (unsigned i=0; i<256; i++)
    seen[i] = 0;

  for (unsigned i=0; i<str.length(); i++) {
    int c = static_cast<int>(str[i]);
    if (seen[c] == 0)
      seen[c] = 1;
    else
      return 0;
  }
  return 1;
}

TEST(ch1_1, uniq) {
  string test_str = "abcd";
  ASSERT_EQ(is_uniq(test_str), 1);
}

TEST(ch1_1, not_uniq) {
  string test_str = "abca";
  ASSERT_EQ(is_uniq(test_str), 0);
}

TEST(ch1_1, blank) {
  string test_str = "";
  ASSERT_EQ(is_uniq(test_str), 1);
}

TEST(ch1_1, single) {
  string test_str = "!";
  ASSERT_EQ(is_uniq(test_str), 1);
}
