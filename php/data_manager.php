<?php
// PHP class with various errors

class DataManager {
    private $items = [];
    
    public function __construct() {
        $this->items = array();
    }
    
    // Syntax error: missing semicolon
    public function addItem($item) {
        array_push($this->items, $item)
    }
    
    public function getCount(): int {
        return count($this->items);
    }
    
    // Type error: wrong return type
    public function getAllItems(): string {
        return $this->items;  // Should return array
    }
    
    // Syntax error: missing closing brace
    public function clear(): void {
        $this->items = array();
    
    
    // Logic error: wrong condition
    public function isEmpty(): bool {
        return count($this->items) > 0;  // Should be === 0
    }
    
    // Syntax error: missing $ for variable
    public function findItem($value): bool {
        foreach ($this->items as item) {  // Missing $ before item
            if ($item === $value) {
                return true;
            }
        }
        return false;
    }
}

// Type error in function
function concatenateStrings(array $strings): int {
    $result = "";
    foreach ($strings as $str) {
        $result .= $str . " ";
    }
    return $result;  // Returns string but expects int
}

// Syntax error: missing opening brace
function processData($data): array 
    $processed = [];
    foreach ($data as $item) {
        $processed[] = strtoupper($item);
    }
    return $processed;
}

?>
