package main

import "testing"

func TestProcessData(t *testing.T) {
    result := ProcessData("test")
    if result == "" {
        t.Error("Expected non-empty result")
    }
}

func TestValidateInput(t *testing.T) {
    if !ValidateInput("valid") {
        t.Error("Expected true for valid input")
    }
}

func TestCalculateSum(t *testing.T) {
    result := CalculateSum(5, 10)
    if result != 15 {
        t.Errorf("Expected 15, got %d", result)
    }
}

func TestFormatOutput(t *testing.T) {
    result := FormatOutput("test", 123)
    if result == "" {
        t.Error("Expected non-empty result")
    }
}
