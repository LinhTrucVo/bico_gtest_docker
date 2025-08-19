//----------------------------------------------------------------------------
// Mock function definitions for the simple_calculator module.
//----------------------------------------------------------------------------

//============================================================================
// Include Files
//============================================================================
#include "mock_simple_calculator.h"
// Include the .c file to get access to static variables and functions (if any)
// For simple_calculator, we include it to demonstrate the pattern
#include "simple_calculator.c"

//============================================================================
// Mock function definitions
//============================================================================
// Required for FFF
DEFINE_FFF_GLOBALS;

// For simple_calculator, we don't need to mock external dependencies
// since it's a simple module without external calls

//============================================================================
// Static variable getter function definitions (if needed)
//============================================================================
// For simple_calculator, there are no static variables to expose

//============================================================================
// Static function wrapper definitions (if needed)
//============================================================================
// For simple_calculator, all functions are public, so no wrappers needed