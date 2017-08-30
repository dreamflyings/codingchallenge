// ch11.6: given an MxN matrix in which each row and col is sorted in ascending order, write a method to find an element

#include <iostream>
#include <vector>
#include <stdio.h>
#include <gtest/gtest.h>

using namespace std;

namespace ch11_6 {

typedef vector<vector<int>> Matrix;

int find_elem(const Matrix &m, int row, int col, int nrows, int ncols, int elem) {
  if (nrows != ncols)
    throw std::runtime_error("nrows != ncols");

  for (int d=0; d<ncols; d++) {
    if (m[d][d] == elem) {
      //printf("found0 %0d %0d\n", d, d);
      return 1;
    }

    if (elem > m[d][d])
      continue;
    else {
      // search left
      int i = d-1;
      while (i >= 0) {
        if (m[i][d] == elem) {
          //printf("found1 %0d %0d\n", i, d);
          return 1;
        }
        i--;
      }

      // search up
      int j = d-1;
      while (j >= 0) {
        if (m[d][j] == elem) {
          //printf("found2 %0d %0d\n", d, j);
          return 1;
        }
        j--;
      }
    }
  }

  return 0; // not found
}

TEST(ch11_6, basic) {
  Matrix m(3,  vector<int>(3)); // nrows, ncols
  m[0][0] = 10;
  m[0][1] = 100;
  m[0][2] = 1000;
  m[1][0] = 20;
  m[1][1] = 200;
  m[1][2] = 2000;
  m[2][0] = 30;
  m[2][1] = 300;
  m[2][2] = 3000;
  EXPECT_EQ(find_elem(m, 0, 0, 3, 3, 2000), 1);
  EXPECT_EQ(find_elem(m, 0, 0, 3, 3, 3000), 1);
  EXPECT_EQ(find_elem(m, 0, 0, 3, 3, 10),   1);
  EXPECT_EQ(find_elem(m, 0, 0, 3, 3, 11),   0);
  EXPECT_EQ(find_elem(m, 0, 0, 3, 3, 300),  1);
}

}
