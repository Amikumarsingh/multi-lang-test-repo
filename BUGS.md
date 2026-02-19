# Complete Bug Reference - 71 Bugs Across 10 Languages

## Python (12 bugs)

### calculator.py
1. Line 3: Missing colon after class definition (SYNTAX)
2. Line 15: Missing colon after if statement (SYNTAX)
3. Line 23: Missing comma in dictionary (SYNTAX)

### data_processor.py
4. Line 8: Type error - concatenating string + dict (TYPE_ERROR)
5. Line 13: Missing 're' import (IMPORT)
6. Line 17: Missing 'datetime' import (IMPORT)
7. Line 30: Wrong indentation (INDENTATION)

### string_utils.py
8. Line 10: Wrong indentation (INDENTATION)
9. Line 19: Logic error - returns count-1 (LOGIC)
10. Line 24: Extra indentation (INDENTATION)
11. Line 29: Type error - string slice index (TYPE_ERROR)
12. Line 35: Missing colon (SYNTAX)

## JavaScript (4 bugs)

### math_ops.js
13. Line 17: Missing closing brace (SYNTAX)
14. Line 34: Missing semicolon (SYNTAX)
15. Line 39: Missing closing bracket (SYNTAX)
16. Line 45: Wrong comparison operator (LOGIC)

## Java (5 bugs)

### DataManager.java
17. Line 13: Missing return type (SYNTAX)
18. Line 25: Type mismatch int/String (TYPE_ERROR)
19. Line 33: Missing HashMap import (IMPORT)
20. Line 43: Missing semicolon (SYNTAX)
21. Line 48: Wrong isEmpty condition (LOGIC)

## Rust (6 bugs)

### calculator.rs
22. Line 16: Missing return type (SYNTAX)
23. Line 19: Missing return keyword (SYNTAX)
24. Line 31: Type error - return 0 instead of 0.0 (TYPE_ERROR)
25. Line 34: Type error - i32/usize division (TYPE_ERROR)
26. Line 39: Missing semicolon (SYNTAX)
27. Line 48: Wrong comparison < instead of > (LOGIC)

## Go (6 bugs)

### data_processor.go
28. Line 15: Missing return type (SYNTAX)
29. Line 25: Wrong return type (TYPE_ERROR)
30. Line 33: Missing strings import (IMPORT)
31. Line 38: Missing opening brace (SYNTAX)
32. Line 44: Wrong isEmpty condition (LOGIC)
33. Line 53: Type error - returning string as int (TYPE_ERROR)

## TypeScript (7 bugs)

### user_manager.ts
34. Line 17: Wrong return type (TYPE_ERROR)
35. Line 22: Missing return type annotation (TYPE_ERROR)
36. Line 27: Parameter type mismatch (TYPE_ERROR)
37. Line 32: Missing closing brace (SYNTAX)
38. Line 37: Wrong comparison (LOGIC)
39. Line 42: Wrong return type (TYPE_ERROR)
40. Line 47: Missing semicolon (SYNTAX)

## C++ (7 bugs)

### string_processor.cpp
41. Line 16: Missing return type (SYNTAX)
42. Line 30: Type mismatch int/string (TYPE_ERROR)
43. Line 37: Missing semicolon (SYNTAX)
44. Line 42: Wrong isEmpty condition (LOGIC)
45. Line 47: Missing algorithm header (IMPORT)
46. Line 52: Missing closing brace (SYNTAX)
47. Line 60: Missing return type (SYNTAX)

## Ruby (6 bugs)

### calculator.rb
48. Line 16: Missing 'end' (SYNTAX)
49. Line 27: Wrong operator = instead of == (LOGIC)
50. Line 35: Integer division (TYPE_ERROR)
51. Line 40: Missing 'end' (SYNTAX)
52. Line 57: Logic error - returns count-1 (LOGIC)
53. Line 62: Missing pipe in block (SYNTAX)
54. Line 82: Missing 'end' (SYNTAX)

## PHP (6 bugs)

### data_manager.php
55. Line 12: Missing semicolon (SYNTAX)
56. Line 21: Wrong return type (TYPE_ERROR)
57. Line 26: Missing closing brace (SYNTAX)
58. Line 31: Wrong isEmpty condition (LOGIC)
59. Line 36: Missing $ before variable (SYNTAX)
60. Line 52: Missing opening brace (SYNTAX)

## C# (6 bugs)

### Calculator.cs
61. Line 18: Missing return type (SYNTAX)
62. Line 28: Wrong return type (TYPE_ERROR)
63. Line 33: Missing semicolon (SYNTAX)
64. Line 38: Wrong IsEmpty condition (LOGIC)
65. Line 44: Missing StringBuilder import (IMPORT)
66. Line 56: Missing closing brace (SYNTAX)

## Kotlin (6 bugs)

### DataProcessor.kt
67. Line 19: Wrong return type (TYPE_ERROR)
68. Line 24: Missing closing brace (SYNTAX)
69. Line 29: Wrong isEmpty condition (LOGIC)
70. Line 34: Type mismatch Int/String (TYPE_ERROR)
71. Line 47: Missing opening brace (SYNTAX)

## Summary by Error Type

- **SYNTAX**: 33 bugs (46%)
- **TYPE_ERROR**: 18 bugs (25%)
- **LOGIC**: 11 bugs (15%)
- **IMPORT**: 6 bugs (8%)
- **INDENTATION**: 3 bugs (4%)

**TOTAL: 71 BUGS**
