// Kotlin class with various errors

package com.example

import java.util.*

class DataProcessor {
    private val items = mutableListOf<String>()
    
    // Missing return type - syntax error
    fun addItem(item: String) {
        items.add(item)
    }
    
    fun getItem(index: Int): String? {
        return if (index in items.indices) {
            items[index]
        } else {
            null
        }
    }
    
    // Type error: wrong return type
    fun getCount(): String {
        return items.size  // Should return Int
    }
    
    // Syntax error: missing closing brace
    fun getAllItems(): List<String> {
        return items.toList()
    
    
    // Logic error: wrong condition
    fun isEmpty(): Boolean {
        return items.size > 0  // Should be == 0 or use items.isEmpty()
    }
    
    // Type error: incompatible types
    fun concatenate(): Int {
        var result = ""
        for (item in items) {
            result += "$item "
        }
        return result  // Returns String but expects Int
    }
    
    // Syntax error: missing colon
    fun clear() {
        items.clear()
    }
}

// Type mismatch in function
fun processStrings(strings: List<String>): Int {
    return strings.map { it.uppercase() }  // Returns List but expects Int
}

// Syntax error: missing opening brace
fun findMax(numbers: List<Int>): Int? 
    if (numbers.isEmpty()) return null
    var max = numbers[0]
    for (num in numbers) {
        if (num > max) {
            max = num
        }
    }
    return max
}

// Logic error: wrong comparison
fun findMin(numbers: List<Int>): Int? {
    if (numbers.isEmpty()) return null
    var min = numbers[0]
    for (num in numbers) {
        if (num > min) {  // Should be <
            min = num
        }
    }
    return min
}
