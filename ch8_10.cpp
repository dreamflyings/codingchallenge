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
class HashCell
{
    public:
        HashCell();
        virtual ~HashCell();
    private:
        K k;
        V v;
};

template <typename K, typename V>
HashCell<K, V>::HashCell() {
}

template <typename K, typename V>
HashCell<K, V>::~HashCell() {
}

template <typename K, typename V>
class HashTable
{
    public:
        HashTable();
        virtual ~HashTable();
        V get(K);
        void put(K, V);
    private:
        const int MAX_SIZE = 256;
        vector<list<HashCell<K, V>>> cell_lists;
};

template <typename K, typename V>
HashTable<K, V>::HashTable() {
}

template <typename K, typename V>
HashTable<K, V>::~HashTable() {
}

template <typename K, typename V>
V HashTable<K, V>::get(K k) {
}

template <typename K, typename V>
void HashTable<K, V>::put(K k, V v) {
}

TEST(ch8_10, basic) {
    HashTable<int, string> h;
    ASSERT_EQ(1, 1);
}

} // namespace ch8_10
