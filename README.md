# Multi-Language Test Repository for VicRaptors

A comprehensive test repository with intentional bugs across **10 programming languages** to test the robustness of the autonomous CI/CD repair system.

## 🎯 Purpose

This repository contains intentional errors across Python, JavaScript, Java, Rust, Go, TypeScript, C++, Ruby, PHP, C#, and Kotlin to ensure the VicRaptors system can:
- Handle multiple programming languages
- Detect various error types (syntax, import, type, logic, indentation)
- Prioritize fixes across different languages
- Generate language-specific repairs

## 📁 Structure

```
multi_lang_test_repo/
├── python/          (3 files, 12 bugs)
├── javascript/      (1 file, 4 bugs)
├── java/            (1 file, 5 bugs)
├── rust/            (1 file, 6 bugs)
├── go/              (1 file, 6 bugs)
├── typescript/      (1 file, 7 bugs)
├── cpp/             (1 file, 7 bugs)
├── ruby/            (1 file, 6 bugs)
├── php/             (1 file, 6 bugs)
├── csharp/          (1 file, 6 bugs)
├── kotlin/          (1 file, 6 bugs)
└── tests/           (Python tests)
```

## 🐛 Bug Summary by Language

| Language   | Files | Bugs | Error Types |
|------------|-------|------|-------------|
| Python     | 3     | 12   | SYNTAX(4), IMPORT(2), TYPE_ERROR(2), LOGIC(1), INDENTATION(3) |
| JavaScript | 1     | 4    | SYNTAX(3), LOGIC(1) |
| Java       | 1     | 5    | SYNTAX(2), IMPORT(1), TYPE_ERROR(1), LOGIC(1) |
| Rust       | 1     | 6    | SYNTAX(2), TYPE_ERROR(3), LOGIC(1) |
| Go         | 1     | 6    | SYNTAX(2), IMPORT(1), TYPE_ERROR(2), LOGIC(1) |
| TypeScript | 1     | 7    | SYNTAX(2), TYPE_ERROR(4), LOGIC(1) |
| C++        | 1     | 7    | SYNTAX(4), IMPORT(1), TYPE_ERROR(1), LOGIC(1) |
| Ruby       | 1     | 6    | SYNTAX(4), LOGIC(1), TYPE_ERROR(1) |
| PHP        | 1     | 6    | SYNTAX(4), TYPE_ERROR(1), LOGIC(1) |
| C#         | 1     | 6    | SYNTAX(3), IMPORT(1), TYPE_ERROR(1), LOGIC(1) |
| Kotlin     | 1     | 6    | SYNTAX(3), TYPE_ERROR(2), LOGIC(1) |
| **TOTAL**  | **15**| **71** | **SYNTAX(33), TYPE_ERROR(18), LOGIC(11), IMPORT(6), INDENTATION(3)** |

## 📊 Detailed Bug List

### Python (12 bugs)
- **calculator.py**: 3 syntax errors (missing colons, missing comma)
- **data_processor.py**: 2 import errors, 1 type error, 1 indentation error
- **string_utils.py**: 2 indentation, 1 syntax, 1 type, 1 logic error

### JavaScript (4 bugs)
- **math_ops.js**: 3 syntax errors (missing braces, semicolons), 1 logic error

### Java (5 bugs)
- **DataManager.java**: 2 syntax, 1 import, 1 type, 1 logic error

### Rust (6 bugs)
- **calculator.rs**: 2 syntax, 3 type errors, 1 logic error

### Go (6 bugs)
- **data_processor.go**: 2 syntax, 1 import, 2 type, 1 logic error

### TypeScript (7 bugs)
- **user_manager.ts**: 2 syntax, 4 type errors, 1 logic error

### C++ (7 bugs)
- **string_processor.cpp**: 4 syntax, 1 import, 1 type, 1 logic error

### Ruby (6 bugs)
- **calculator.rb**: 4 syntax, 1 logic, 1 type error

### PHP (6 bugs)
- **data_manager.php**: 4 syntax, 1 type, 1 logic error

### C# (6 bugs)
- **Calculator.cs**: 3 syntax, 1 import, 1 type, 1 logic error

### Kotlin (6 bugs)
- **DataProcessor.kt**: 3 syntax, 2 type, 1 logic error

## 🧪 Testing

### Python Tests
```bash
pytest tests/ -v
```

Expected: All tests will fail due to syntax/import errors preventing module loading.

## 🚀 Running with VicRaptors

```bash
# Initialize as git repo
cd multi_lang_test_repo
git init
git add .
git commit -m "Multi-language test repo with 71 bugs across 10 languages"

# Push to GitHub (optional)
git remote add origin https://github.com/YOUR_USERNAME/multi-lang-test.git
git push -u origin main

# Run VicRaptors system
cd ..
python main.py
# Enter: https://github.com/YOUR_USERNAME/multi-lang-test.git
```

## ✅ Expected System Behavior

1. **Stage 0**: Detect test failures (Python tests)
2. **Agent 1**: 
   - Normalize bug types across all languages
   - Group failures by root cause
   - Prioritize based on impact
3. **Agent 2**: 
   - Generate language-specific fixes
   - Apply minimal patches
   - Handle syntax/import/type/logic errors

## 🎓 Learning Objectives

This test repository validates:
- ✅ Multi-language error detection (10 languages)
- ✅ Cross-language prioritization
- ✅ Language-specific fix generation
- ✅ Robust error classification (71 bugs)
- ✅ Syntax variations across languages
- ✅ Type system differences
- ✅ Import/dependency handling

## 📝 Language Coverage

- **Compiled**: Java, Rust, Go, C++, C#, Kotlin
- **Interpreted**: Python, JavaScript, TypeScript, Ruby, PHP
- **Statically Typed**: Java, Rust, Go, TypeScript, C++, C#, Kotlin
- **Dynamically Typed**: Python, JavaScript, Ruby, PHP

This comprehensive test suite ensures your agent can handle real-world polyglot repositories! 🚀
