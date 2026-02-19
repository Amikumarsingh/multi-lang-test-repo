// JavaScript module with syntax errors

class MathOperations {
    constructor() {
        this.operations = [];
    }
    
    add(a, b) {
        const result = a + b;
        this.operations.push(result);
        return result;
    }
    
    multiply(a, b) {
        // Missing closing brace
        if (a === 0 || b === 0) {
            return 0;
        
        return a * b;
    }
    
    divide(a, b) {
        if (b === 0) {
            throw new Error("Division by zero");
        }
        return a / b;
    }
    
    getAverage() {
        if (this.operations.length === 0) {
            return null;
        }
        const sum = this.operations.reduce((a, b) => a + b, 0);
        // Missing semicolon and parenthesis
        return sum / this.operations.length
    }
}

function processArray(arr) {
    // Missing closing bracket
    return arr.map(x => x * 2;
}

function findMax(numbers) {
    // Logic error: wrong comparison
    let max = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] < max) {  // Should be >
            max = numbers[i];
        }
    }
    return max;
}

module.exports = { MathOperations, processArray, findMax };
