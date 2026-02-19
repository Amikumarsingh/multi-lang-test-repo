# Ruby module with various errors

class Calculator
  attr_reader :history
  
  def initialize
    @history = []
  end
  
  def add(a, b)
    result = a + b
    @history << result
    result
  end
  
  # Syntax error: missing 'end'
  def subtract(a, b)
    result = a - b
    @history << result
    result
  
  
  def multiply(a, b)
    result = a * b
    @history << result
    result
  end
  
  # Logic error: wrong condition
  def divide(a, b)
    if b = 0  # Should be == or .zero?
      raise ArgumentError, "Division by zero"
    end
    a / b
  end
  
  def average
    return nil if @history.empty?
    # Type error: integer division instead of float
    @history.sum / @history.length
  end
  
  # Syntax error: wrong method definition
  def clear
    @history.clear
  
end

class StringHelper
  # Syntax error: missing 'do' in block
  def self.reverse_words(text)
    text.split.map { |word| word.reverse }.join(' ')
  end
  
  # Logic error: wrong comparison
  def self.count_vowels(text)
    vowels = 'aeiouAEIOU'
    count = 0
    text.each_char do |char|
      count += 1 if vowels.include?(char)
    end
    count - 1  # Should return count
  end
  
  # Syntax error: missing pipe in block parameters
  def self.capitalize_words(text)
    text.split.map { word word.capitalize }.join(' ')
  end
  
  # Type error: wrong method call
  def self.truncate(text, length)
    if text.length > length
      text[0..length] + "..."
    else
      text
    end
  end
end

# Missing class definition
def process_array(arr)
  arr.map { |x| x * 2 }
end

# Syntax error: missing 'end'
def find_max(numbers)
  return nil if numbers.empty?
  max = numbers.first
  numbers.each do |num|
    max = num if num > max
  end
  max
