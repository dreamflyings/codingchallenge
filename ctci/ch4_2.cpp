// ch4.2: Given a directed graph, design an adj_list_tgorithm to find out whether there is a route between two nodes.

#include <iostream>
#include <array>
#include <vector>

#include <gtest/gtest.h>

using namespace std;

namespace ch4_2 {

typedef array<vector<int>, 4> adj_list_t; // adjacency list

int dfs(const adj_list_t &a, array<int, 4> &v, int n, int f) {
  if (n == f)
    return 1;

  v[n] = 1; // mark done as visited

  for (unsigned i=0; i<a[n].size(); i++) {
    int nn = a[n][i];
    if (v[nn] == 0) // next node is not visited
      return dfs(a, v, nn, f);
  }

  return 0;
}

TEST(ch4_2, basic) {
  adj_list_t a;
  array<int, 4> v;
  a[0].push_back(1); // 0 -> 1
  a[1].push_back(2); // 1 -> 2
  a[2].push_back(3); // 2 -> 3
  a[3].push_back(0); // 3 -> 0

  ASSERT_TRUE(dfs(a, v, 0, 0));
  ASSERT_TRUE(dfs(a, v, 0, 3));
  ASSERT_FALSE(dfs(a, v, 3, 0));
}

}
