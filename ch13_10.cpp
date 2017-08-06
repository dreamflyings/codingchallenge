// ch13.10: write function in C called my2DAlloc, minimizing calls to malloc

#include <stdio.h>
#include <gtest/gtest.h>

int** my2DAlloc(int rows, int cols) {
  int hdr = rows*sizeof(int*);
  int dat = rows*cols*sizeof(int);

  int **rowptr = (int**)malloc(hdr + dat); // allocate header - array of pointers, followed by data

  int *hdrptr = (int*)(rowptr+rows); // beginning of array buffer

  for (int row=0; row<rows; row++)
    rowptr[row] = hdrptr + row*cols;

  return rowptr;
}

TEST(ch13_10, basic) {
  int **array = my2DAlloc(10, 100);
  for (unsigned r=0; r<10; r++) {
    for (unsigned c=0; c<100; c++) {
      array[r][c] = r*c;
      ASSERT_EQ(array[r][c], r*c);
    }
  }
  free(array);
}

