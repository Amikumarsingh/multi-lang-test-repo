const assert = require('assert');
const { add, multiply, divide, factorial } = require('../javascript/math_ops');

describe('Math Operations', () => {
    it('should add two numbers', () => {
        assert.strictEqual(add(2, 3), 5);
    });

    it('should multiply two numbers', () => {
        assert.strictEqual(multiply(4, 5), 20);
    });

    it('should divide two numbers', () => {
        assert.strictEqual(divide(10, 2), 5);
    });

    it('should calculate factorial', () => {
        assert.strictEqual(factorial(5), 120);
    });
});
