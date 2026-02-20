#include "gtest/gtest.h"
#include "gmock/gmock.h"

// Unit under test
extern "C"
{
#include "mock_UnitName.h"
}

class TesteaeUnitName : public ::testing::Test
{
public:
    void SetUp() override
    {
        RESET_FAKE(dummyFunc01);
        RESET_FAKE(dummyFunc02);
        FFF_RESET_HISTORY();

        set_UnitName_var(10);  // Reset to initial value
    }

    void TearDown() override
    {
    }
};

//--------------------------------------------------------------
// Test Cases
//--------------------------------------------------------------

//----------------------------------------------------------------------------
/** Test UnitNameFnc1 when a == 0
    
Expected behavior: Should call dummyFunc01 and return 0
*/
//----------------------------------------------------------------------------
TEST_F(TesteaeUnitName, test_UnitNameFnc1_WhenAEqualsZero)
{
    // Arrange
    int a = 0;
    int b = 5;
    
    // Act
    int result = call_UnitNameFnc1(a, b);
    
    // Assert
    EXPECT_EQ(0, result);
}

//----------------------------------------------------------------------------
/** Test UnitNameFnc1 when a != 0 and b == 0
    
Expected behavior: Should call dummyFunc02 with parameter a and return result
*/
//----------------------------------------------------------------------------
TEST_F(TesteaeUnitName, test_UnitNameFnc1_WhenBEqualsZero)
{
    // Arrange
    int a = 10;
    int b = 0;
    
    // Act
    int result = call_UnitNameFnc1(a, b);
    
    // Assert
    EXPECT_EQ(0, result);
}

//----------------------------------------------------------------------------
/** Test UnitNameFnc1 when both a and b are non-zero
    
Expected behavior: Should add a + b + ++UnitName_var and return result
Increment UnitName_var
*/
//----------------------------------------------------------------------------
TEST_F(TesteaeUnitName, test_UnitNameFnc1_WhenBothNonZero)
{
    // Arrange
    int a = 5;
    int b = 3;
    int initialVar = get_UnitName_var();  // Should be 10
    
    // Act
    int result = call_UnitNameFnc1(a, b);
    
    // Assert
    // Expected: a + b + ++UnitName_var = 5 + 3 + 11 = 19
    int expectedResult = a + b + (initialVar + 1);
    EXPECT_EQ(expectedResult, result);
    EXPECT_EQ(initialVar + 1, get_UnitName_var());  // Variable should be incremented
}

//----------------------------------------------------------------------------
/** Test UnitNameFnc1 when a == 0 and b == 0
    
Expected behavior: Should call dummyFunc01 (a == 0 takes precedence)
*/
//----------------------------------------------------------------------------
TEST_F(TesteaeUnitName, test_UnitNameFnc1_WhenBothZero)
{
    // Arrange
    int a = 0;
    int b = 0;
    
    // Act
    int result = call_UnitNameFnc1(a, b);
    
    // Assert
    EXPECT_EQ(0, result);
}

//----------------------------------------------------------------------------
/** Test UnitNameFnc1 with different b values when a is zero
    
Expected behavior: Should still call dummyFunc01 regardless of b value
*/
//----------------------------------------------------------------------------
TEST_F(TesteaeUnitName, test_UnitNameFnc1_AZeroWithDifferentB)
{
    // Arrange
    int a = 0;
    int b = 100;
    
    // Act
    int result = call_UnitNameFnc1(a, b);
    
    // Assert
    EXPECT_EQ(0, result);
}

//----------------------------------------------------------------------------
/** Test UnitNameFnc1 with negative values
    
Expected behavior: Should add negative values correctly
*/
//----------------------------------------------------------------------------
TEST_F(TesteaeUnitName, test_UnitNameFnc1_WithNegativeValues)
{
    // Arrange
    int a = -5;
    int b = -3;
    int initialVar = get_UnitName_var();  // Should be 10
    
    // Act
    int result = call_UnitNameFnc1(a, b);
    
    // Assert
    // Expected: a + b + ++UnitName_var = -5 + -3 + 11 = 3
    int expectedResult = a + b + (initialVar + 1);
    EXPECT_EQ(expectedResult, result);
    EXPECT_EQ(initialVar + 1, get_UnitName_var());
}

//----------------------------------------------------------------------------
/** Test UnitNameFnc1 with large positive values
    
Expected behavior: Should sum large values correctly
*/
//----------------------------------------------------------------------------
TEST_F(TesteaeUnitName, test_UnitNameFnc1_WithLargeValues)
{
    // Arrange
    int a = 1000;
    int b = 2000;
    int initialVar = get_UnitName_var();
    
    // Act
    int result = call_UnitNameFnc1(a, b);
    
    // Assert
    int expectedResult = a + b + (initialVar + 1);
    EXPECT_EQ(expectedResult, result);
    EXPECT_EQ(initialVar + 1, get_UnitName_var());
}


