#!/bin/bash
cd rust
rustc calculator.rs --test -o test_calculator
./test_calculator
