// ch3.2: Design a vals that has push, pop, and min (returns min element)
//        functions that all operate in O(1) time.

#include <gtest/gtest.h>

using namespace std;

namespace ch3_2 {

class Stack
{
    public:
        Stack();
        virtual ~Stack();

        void push(int x);
        int pop();
        int min();
    private:
        int vals[10];
        int mins[10];
        int v;
        int m;
};

Stack::Stack() {
    v = -1;
    m = -1;
}

Stack::~Stack() {
}

void Stack::push(int x) {
    if (v >= 10)
        throw std::runtime_error("overflow");

    vals[++v] = x;

    if (x <= mins[m] || m == -1)
        mins[++m] = x;
}

int Stack::pop() {
    if (v < 0)
        throw std::runtime_error("underflow");

    int p = vals[v--];

    if (p == mins[m])
        m--;

    return p;
}

int Stack::min() {
    return mins[m];
}

TEST(ch3_2, push_pop) {
    Stack s;
    s.push(3);
    s.push(2);
    ASSERT_EQ(s.pop(), 2);
}

TEST(ch3_2, push_min_pop) {
    Stack s;
    s.push(3);
    ASSERT_EQ(s.min(), 3);
    ASSERT_EQ(s.pop(), 3);
}

TEST(ch3_2, push_2x_min) {
    Stack s;
    s.push(1);
    s.push(1);
    ASSERT_EQ(s.pop(), 1);
    ASSERT_EQ(s.min(), 1);
    s.push(2);
    ASSERT_EQ(s.min(), 1);
    ASSERT_EQ(s.pop(), 2);
    ASSERT_EQ(s.min(), 1);
}

} // namespace ch3_2
