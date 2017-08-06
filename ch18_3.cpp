// ch18.3: write method to choose m integers from array of size n, each element
//         must have equal probability of being chosen (assume elements cannot
//         be repeated)

#include <iostream>
#include <map>
#include <vector>
#include <stdlib.h>
#include <time.h>

#include <gtest/gtest.h>

using namespace std;

// I am using a map to avoid repeated elements. Each element should have equal
// probability of being chosen.  The solution provides a better answer, but
// it was confusing to me

void choose_m_from_n(vector<int> &m, vector<int> &n) {
  map<int, int> prev_chosen;
  int j = 0;
  for (unsigned i=0; i<m.size(); i++) {
    int which;
    do {
      which = rand() % n.size();
    } while (prev_chosen[which] != 0);
    m[j++] = n[which];
    prev_chosen[which] = 1;
  }
}

TEST(ch18_3, basic) {
  srand(time(NULL)); // randomize seed

  vector<int> n(5);
  for (unsigned i=0; i<n.size(); i++)
    n[i] = i;

  vector<int> m(4);

  choose_m_from_n(m, n);

  //--FIXME: make self checking
}
