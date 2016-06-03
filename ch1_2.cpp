#include <stdio.h>
#include <stdlib.h>

#include <gtest/gtest.h>

void reverse_cstr(char *str) {
    unsigned len = strlen(str);
    for (unsigned i=0; i<len/2; i++) {
        char tmp = str[i];
        str[i] = str[len-i-1];
        str[len-i-1] = tmp;
    }
}

TEST(ch1_2, basic) {
    char test_str[] = "abcd";
    char exp_str[]  = "dcba";
    reverse_cstr(test_str);
    ASSERT_STREQ(test_str, exp_str);
}

TEST(ch1_2, odd) {
    char test_str[] = "abcde";
    char exp_str[]  = "edcba";
    reverse_cstr(test_str);
    ASSERT_STREQ(test_str, exp_str);
}

TEST(ch1_2, blank) {
    char test_str[] = "";
    char exp_str[]  = "";
    reverse_cstr(test_str);
    ASSERT_STREQ(test_str, exp_str);
}

