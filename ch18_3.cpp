// ch18.3: write method to choose m integers from array of size n, each element
//         must have equal probability of being chosen (assume elements cannot
//         be repeated)

#include <iostream>
#include <vector>
#include <stdlib.h>
#include <time.h>

#include <gtest/gtest.h>

using namespace std;

/*
    I am going to use a map for this.
*/

void choose_m_from_n(vector<int> &m, vector<int> &n) {
    for (unsigned i=0; i<n; i++) {
    }
}

TEST(ch18_3, basic) {
    srand(time(NULL)); // randomize seed

    vector<int> n(4);
    for (unsigned i=0; i<n.size(); i++)
        n[i] = i;

    vector<int> m(2);

    choose_m_from_n(n, m);
}
