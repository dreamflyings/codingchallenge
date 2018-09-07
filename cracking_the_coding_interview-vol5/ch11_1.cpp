// ch11.1: given two sorted vectors, where A has large enough buffer at end
//         to hold B.  write method to merge B into A in sorted order.

#include <iostream>
#include <vector>

#include <gtest/gtest.h>

using namespace std;

void sorted_merge(vector<int> &a, vector<int> &b, int a_len, int b_len) {
  int k = a_len+b_len-1;
  int i = a_len-1;
  int j = b_len-1;

  while (k >= 0) {
    if (a[i] >= b[j]) {
      a[k] = a[i];
      i--;
    } else {
      a[k] = b[j];
      j--;
    }
    k--;
  }
}

TEST(ch11_1, basic) {
  vector<int> a = { 1, 4, 8, 10, 15 };
  vector<int> b = { 2, 5, 9, 11, 16 };
  vector<int> a_exp = { 1, 2, 4, 5, 8, 9, 10, 11, 15, 16 };
  a.resize(a.size()+b.size());
  sorted_merge(a, b, 5, 5);
  ASSERT_EQ(a, a_exp);
}

TEST(ch11_1, empty) {
  vector<int> a = { };
  vector<int> b = { 2, 5, 9, 11, 16 };
  vector<int> a_exp = { 2, 5, 9, 11, 16 };
  a.resize(a.size()+b.size());
  sorted_merge(a, b, 0, 5);
  ASSERT_EQ(a, a_exp);
}

TEST(ch11_1, diff_size) {
  vector<int> a = { 1, 4, 8, 10, 15 };
  vector<int> b = { 16 };
  vector<int> a_exp = { 1, 4, 8, 10, 15, 16 };
  a.resize(a.size()+b.size());
  sorted_merge(a, b, 5, 1);
  ASSERT_EQ(a, a_exp);
}

