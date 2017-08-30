// ch4.2: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

#include <iostream>
#include <vector>

#include <gtest/gtest.h>

using namespace std;

namespace ch4_2 {

void add_edge(vector<int> &adj[])
{
  cout << "here" << endl;
}

TEST(ch4_2, basic) {
  vector<int> adj[10];

  add_edge(adj);
 
  ASSERT_EQ(1, 1);
}

}
