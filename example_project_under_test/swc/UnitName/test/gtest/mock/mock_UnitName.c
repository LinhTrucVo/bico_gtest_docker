//--------------------------------------------------------------
// Include Files
//--------------------------------------------------------------
#include "mock_UnitName.h"

// Include the .c file to get access to static variables and functions
#include "UnitName.c"

//--------------------------------------------------------------
// Mock function definitions
//--------------------------------------------------------------

// Required for FFF
DEFINE_FFF_GLOBALS;

DEFINE_FAKE_VOID_FUNC(dummyFunc01);

DEFINE_FAKE_VALUE_FUNC(int, dummyFunc02, int);

//--------------------------------------------------------------
// Static variable getter function definitions
//--------------------------------------------------------------

int get_UnitName_var(void)
{
    return UnitName_var;
}

void set_UnitName_var(int value)
{
    UnitName_var = value;
}

//--------------------------------------------------------------
// Static function wrapper definitions
//--------------------------------------------------------------

int call_UnitNameFnc1(int a, int b)
{
    return UnitNameFnc1(a, b);
}
