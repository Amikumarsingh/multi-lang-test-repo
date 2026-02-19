<?php
use PHPUnit\Framework\TestCase;
require_once '../php/data_manager.php';

class DataManagerTest extends TestCase {
    public function testProcessData() {
        $result = processData("test");
        $this->assertNotEmpty($result);
    }

    public function testValidateInput() {
        $this->assertTrue(validateInput("valid"));
    }

    public function testCalculateSum() {
        $this->assertEquals(15, calculateSum(5, 10));
    }

    public function testFormatOutput() {
        $result = formatOutput("test", 123);
        $this->assertNotEmpty($result);
    }
}
?>
