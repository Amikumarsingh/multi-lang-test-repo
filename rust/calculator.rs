// Rust module with various errors

use std::collections::HashMap;
// Missing: use std::fmt;

pub struct Calculator {
    history: Vec<i32>,
}

impl Calculator {
    pub fn new() -> Self {
        Calculator {
            history: Vec::new()
        }
    }
    
    // Missing return type - syntax error
    pub fn add(&mut self, a: i32, b: i32) {
        let result = a + b;
        self.history.push(result);
        result  // Missing 'return' keyword or should be in expression
    }
    
    pub fn divide(&self, a: i32, b: i32) -> Result<i32, String> {
        if b == 0 {
            return Err("Division by zero".to_string());
        }
        Ok(a / b)
    }
    
    // Type error: mismatched types
    pub fn get_average(&self) -> f64 {
        if self.history.is_empty() {
            return 0;  // Should return 0.0 (f64)
        }
        let sum: i32 = self.history.iter().sum();
        sum / self.history.len()  // Type error: i32 / usize
    }
    
    // Syntax error: missing semicolon
    pub fn clear(&mut self) {
        self.history.clear()
    }
}

// Logic error: wrong comparison
pub fn find_max(numbers: &[i32]) -> Option<i32> {
    if numbers.is_empty() {
        return None;
    }
    let mut max = numbers[0];
    for &num in numbers.iter() {
        if num < max {  // Should be >
            max = num;
        }
    }
    Some(max)
}

// Missing Display trait implementation
pub fn format_number(n: i32) -> String {
    format!("Number: {}", n)
}
