"""Python module with various error types"""

class Calculator
    """Calculator class with syntax error - missing colon"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(result)
        return result
    
    def divide(self, a, b):
        if b == 0
            raise ValueError("Division by zero")  # Missing colon
        return a / b
    
    def get_stats(self):
        if not self.history:
            return None
        return {
            'count': len(self.history),
            'sum': sum(self.history)
            'avg': sum(self.history) / len(self.history)  # Missing comma
        }
