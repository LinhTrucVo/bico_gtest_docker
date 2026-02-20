#ifndef MOCK_EAEUNITNAME_H
#define MOCK_EAEUNITNAME_H

//--------------------------------------------------------------
// Include Files
//--------------------------------------------------------------
#include "fff.h"

//--------------------------------------------------------------
// Mock function declarations
//--------------------------------------------------------------
DECLARE_FAKE_VOID_FUNC(dummyFunc01);

DECLARE_FAKE_VALUE_FUNC(int, dummyFunc02, int);

//--------------------------------------------------------------
// Static variable getter function declarations
//--------------------------------------------------------------

int get_UnitName_var(void);

void set_UnitName_var(int value);

//--------------------------------------------------------------
// Static function wrapper declarations
//--------------------------------------------------------------

int call_UnitNameFnc1(int a, int b);

#endif // MOCK_EAEUNITNAME_H
