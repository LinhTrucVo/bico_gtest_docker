//----------------------------------------------------------------------------
// Unit Test file for the simple_calculator module.
//----------------------------------------------------------------------------

#include "gtest/gtest.h"
#include "gmock/gmock.h"

// Unit under test
extern "C"
{
#include "mock_simple_calculator.h"
}

//------------------------------------------------------------------------------
// Test Fixture Class
//------------------------------------------------------------------------------
class SimpleCalculatorTest : public ::testing::Test 
{
protected:
    void SetUp() override 
    {
        // Reset all fake functions before each test
        FFF_RESET_HISTORY();
    }

    void TearDown() override 
    {
        // Clean up after each test if needed
    }
};

//------------------------------------------------------------------------------
// Test Cases for add() function
//------------------------------------------------------------------------------
TEST_F(SimpleCalculatorTest, Add_PositiveNumbers_ReturnsCorrectSum)
{
    // Arrange
    int a = 5;
    int b = 3;
    int expected = 8;

    // Act
    int result = add(a, b);

    // Assert
    EXPECT_EQ(result, expected);
}

TEST_F(SimpleCalculatorTest, Add_MixedNumbers_ReturnsCorrectSum)
{
    // Arrange
    int a = 10;
    int b = -3;
    int expected = 7;

    // Act
    int result = add(a, b);

    // Assert
    EXPECT_EQ(result, expected);
}

//------------------------------------------------------------------------------
// Test Cases for subtract() function
//------------------------------------------------------------------------------
TEST_F(SimpleCalculatorTest, Subtract_PositiveNumbers_ReturnsCorrectDifference)
{
    // Arrange
    int a = 10;
    int b = 3;
    int expected = 7;

    // Act
    int result = subtract(a, b);

    // Assert
    EXPECT_EQ(result, expected);
}

TEST_F(SimpleCalculatorTest, Subtract_ResultNegative_ReturnsCorrectDifference)
{
    // Arrange
    int a = 3;
    int b = 10;
    int expected = -7;

    // Act
    int result = subtract(a, b);

    // Assert
    EXPECT_EQ(result, expected);
}

//------------------------------------------------------------------------------
// Test Cases for multiply() function
//------------------------------------------------------------------------------
TEST_F(SimpleCalculatorTest, Multiply_PositiveNumbers_ReturnsCorrectProduct)
{
    // Arrange
    int a = 4;
    int b = 5;
    int expected = 20;

    // Act
    int result = multiply(a, b);

    // Assert
    EXPECT_EQ(result, expected);
}

TEST_F(SimpleCalculatorTest, Multiply_WithZero_ReturnsZero)
{
    // Arrange
    int a = 5;
    int b = 0;
    int expected = 0;

    // Act
    int result = multiply(a, b);

    // Assert
    EXPECT_EQ(result, expected);
}

//------------------------------------------------------------------------------
// Test Cases for divide() function
//------------------------------------------------------------------------------
TEST_F(SimpleCalculatorTest, Divide_PositiveNumbers_ReturnsCorrectQuotient)
{
    // Arrange
    int a = 20;
    int b = 4;
    int expected = 1;

    // Act
    int result = divide(a, b);

    // Assert
    EXPECT_EQ(result, expected);
}

TEST_F(SimpleCalculatorTest, Divide_ByZero_ReturnsZero)
{
    // Arrange
    int a = 10;
    int b = 0;
    int expected = 0;  // Based on implementation that returns 0 for division by zero

    // Act
    int result = divide(a, b);

    // Assert
    EXPECT_EQ(result, expected);
}