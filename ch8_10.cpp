// ch8.10: Design a hash table that uses chaining (linked lists) to handle
//         collisions

#include <iostream>
#include <vector>
#include <list>
#include <string>

#include <gtest/gtest.h>

using namespace std;

namespace ch8_10 {

template <typename K, typename V>
class HashCell {
 public:
  HashCell() { }
  HashCell(K _k, V _v) : k(_k), v(_v) { }
  virtual ~HashCell() { }
  //private: //--FIXME: should be private
  K k;
  V v;
};

template <typename K, typename V>
class HashTable {
 public:
  HashTable();
  virtual ~HashTable() { }
  V get(K);
  void put(K, V);
 private:
  const int MAX_SIZE = 256;
  vector<list<HashCell<K, V>*>> cell_lists;
};

template <typename K, typename V>
HashTable<K, V>::HashTable() {
  cell_lists.resize(MAX_SIZE);
}

template <typename K, typename V>
V HashTable<K, V>::get(K k) {
  int hash_key = std::hash<K>()(k);
  list<HashCell<K, V>*> *l = &cell_lists[hash_key];
  typename list<HashCell<K, V>*>::const_iterator it;
  for (it=l->begin(); it != l->end(); ++it) {
    HashCell<K, V> *c = *it;
    if (c->k == k)
      return c->v;
  }
  return NULL; //--FIXME: throw exception?
}

template <typename K, typename V>
void HashTable<K, V>::put(K k, V v) {
  int hash_key = std::hash<K>()(k);
  list<HashCell<K, V>*> *l = &cell_lists[hash_key];
  typename list<HashCell<K, V>*>::const_iterator it;

  HashCell<K, V> *cell = new HashCell<K, V>(k, v); //--FIXME: use smart pointer?

  // check for duplicates first
  for (it=l->begin(); it != l->end(); ++it) {
    HashCell<K, V> *c = *it;
    if (c->k == k)
      l->erase(it++);
    break;
  }

  l->push_back(cell);
}

TEST(ch8_10, put_get) {
  HashTable<int, string> h;
  h.put(10, "hello");
  ASSERT_EQ(h.get(10), "hello");
}

TEST(ch8_10, put_get_2) {
  HashTable<int, string> h;
  h.put(10, "hello");
  h.put(10, "world");
  ASSERT_EQ(h.get(10), "world");
}

} // namespace ch8_10
