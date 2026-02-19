using Xunit;

public class CalculatorTests
{
    [Fact]
    public void TestAdd()
    {
        Assert.Equal(5, Calculator.Add(2, 3));
    }

    [Fact]
    public void TestSubtract()
    {
        Assert.Equal(2, Calculator.Subtract(5, 3));
    }

    [Fact]
    public void TestMultiply()
    {
        Assert.Equal(20, Calculator.Multiply(4, 5));
    }

    [Fact]
    public void TestDivide()
    {
        Assert.Equal(5, Calculator.Divide(10, 2));
    }
}
