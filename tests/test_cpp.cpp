#include <cassert>
#include <string>
#include "../cpp/string_processor.cpp"

void test_reverse_string() {
    assert(reverseString("hello") == "olleh");
}

void test_to_uppercase() {
    assert(toUpperCase("hello") == "HELLO");
}

void test_count_chars() {
    assert(countChars("hello") == 5);
}

void test_concat_strings() {
    assert(concatStrings("hello", "world") == "helloworld");
}

int main() {
    test_reverse_string();
    test_to_uppercase();
    test_count_chars();
    test_concat_strings();
    return 0;
}
