"""String utilities with various errors"""

def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def capitalize_words(text):
    """Capitalize words with indentation error"""
    words = text.split()
    result = []
    for word in words:
      result.append(word.capitalize())  # Wrong indentation
    return ' '.join(result)

def count_vowels(text):
    """Count vowels with logic error"""
    vowels = 'aeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    # Logic error: returns wrong value
    return count - 1  # Should return count

def is_palindrome(s):
    """Check palindrome"""
    clean = s.lower().replace(' ', '')
      return clean == clean[::-1]  # Extra indentation

def truncate(text, length):
    """Truncate text with type error"""
    if len(text) > length:
        # Type error: can't slice with string
        return text[:'10'] + '...'  # Should be text[:10]
    return text

def merge_strings(*args):
    """Merge strings"""
    result = ''
    for arg in args
        result += arg  # Missing colon
    return result
