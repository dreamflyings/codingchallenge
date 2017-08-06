// ch4.1: Implement a function to check if a binary tree is balanced. Binary
//        tree define such that the heights of the two subtress of any node
//        never differ by more than one.

#include <stdio.h>

#include <sys/param.h> // for MAX

#include <gtest/gtest.h>

namespace ch4_1 {

class Node {
 public:
  Node *l;
  Node *r;;
};


int get_height(Node *node) {
  int l;
  int r;

  if (node == NULL)
    return 0;

  l = get_height(node->l);
  if (l == -1)
    return -1;

  r = get_height(node->r);

  if (r == -1)
    return -1;

  if (abs(r - l) > 1) // this checks whether subtrees are balanced
    return -1;
  else
    return MAX(l, r)+1; // key: returns height of current subtree
}

int check_balanced(Node *node) {
  return (get_height(node) == -1) ? 0 : 1;
}

TEST(ch4_1, height_2) {
  Node *a = new Node();
  a->l = new Node();
  a->r = new Node();
  ASSERT_EQ(check_balanced(a), 1);
}

TEST(ch4_1, height_1) {
  Node *a = new Node();
  ASSERT_EQ(check_balanced(a), 1);
}

TEST(ch4_1, unbalanced) {
  Node *a = new Node();
  a->l = new Node();
  a->r = new Node();
  a->l->l = new Node();
  a->l->r = new Node();
  a->l->l->l = new Node();
  a->l->l->r = new Node();

  ASSERT_EQ(check_balanced(a), 0);
}

}
