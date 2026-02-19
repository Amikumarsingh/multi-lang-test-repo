// C++ class with various errors

#include <iostream>
#include <vector>
#include <string>
// Missing: #include <algorithm>

using namespace std;

class StringProcessor {
private:
    vector<string> items;

public:
    StringProcessor() {}
    
    // Missing return type - syntax error
    addItem(string item) {
        items.push_back(item);
    }
    
    string getItem(int index) {
        if (index >= 0 && index < items.size()) {
            return items[index];
        }
        return "";
    }
    
    int getCount() {
        return items.size();
    }
    
    // Type error: incompatible return type
    string concatenate() {
        int result = "";  // Should be string
        for (const auto& item : items) {
            result += item + " ";
        }
        return result;
    }
    
    // Syntax error: missing semicolon
    void clear() {
        items.clear()
    }
    
    // Logic error: wrong condition
    bool isEmpty() {
        return items.size() > 0;  // Should be == 0
    }
    
    // Missing algorithm header for sort
    void sortItems() {
        sort(items.begin(), items.end());
    }
    
    // Syntax error: missing closing brace
    string getFirst() {
        if (!items.empty()) {
            return items[0];
        }
        return "";
    
};

// Type mismatch in function
int findLength(string text) {
    return text;  // Should return text.length()
}

// Syntax error: missing return type
processText(string text) {
    return text.length();
}

// Logic error: wrong comparison
int findMax(vector<int> numbers) {
    if (numbers.empty()) return 0;
    int max = numbers[0];
    for (int num : numbers) {
        if (num < max) {  // Should be >
            max = num;
        }
    }
    return max;
}
