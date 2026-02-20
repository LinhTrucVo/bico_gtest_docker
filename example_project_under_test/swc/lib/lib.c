#include "lib.h"

//--------------------------------------------------------------
// Static variable for dummyFunc01
//--------------------------------------------------------------
static uint8_t dummy_counter = 0;

//--------------------------------------------------------------
// Function implementations
//--------------------------------------------------------------

void dummyFunc01(void)
{
    dummy_counter++;
}

int dummyFunc02(int value)
{
    return value * value;
}
