#!/usr/bin/env python3
"""Master build engine to run all language tests"""
import subprocess
import sys

ENGINES = {
    'python': 'python build_engines/python_build.py',
    'javascript': 'node build_engines/javascript_build.js',
    'java': 'bash build_engines/java_build.sh',
    'rust': 'bash build_engines/rust_build.sh',
    'go': 'bash build_engines/go_build.sh',
    'typescript': 'node build_engines/typescript_build.js',
    'cpp': 'bash build_engines/cpp_build.sh',
    'ruby': 'ruby build_engines/ruby_build.rb',
    'php': 'php build_engines/php_build.php',
    'csharp': 'bash build_engines/csharp_build.sh',
    'kotlin': 'bash build_engines/kotlin_build.sh'
}

def run_all():
    results = {}
    for lang, cmd in ENGINES.items():
        print(f"\n{'='*60}")
        print(f"Building {lang.upper()}")
        print('='*60)
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        results[lang] = result.returncode
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    
    print(f"\n{'='*60}")
    print("BUILD SUMMARY")
    print('='*60)
    for lang, code in results.items():
        status = "✓ PASS" if code == 0 else "✗ FAIL"
        print(f"{lang:15} {status}")
    
    return 0 if all(c == 0 for c in results.values()) else 1

if __name__ == '__main__':
    sys.exit(run_all())
