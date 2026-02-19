require 'minitest/autorun'
require_relative '../ruby/calculator'

class CalculatorTest < Minitest::Test
  def test_add
    assert_equal 5, add(2, 3)
  end

  def test_subtract
    assert_equal 2, subtract(5, 3)
  end

  def test_multiply
    assert_equal 20, multiply(4, 5)
  end

  def test_divide
    assert_equal 5, divide(10, 2)
  end

  def test_power
    assert_equal 8, power(2, 3)
  end
end
