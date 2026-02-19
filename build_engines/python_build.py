#!/usr/bin/env python3
import subprocess
import sys

def build():
    """Run Python tests"""
    result = subprocess.run(['pytest', 'tests/', '-v'], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    return result.returncode

if __name__ == '__main__':
    sys.exit(build())
