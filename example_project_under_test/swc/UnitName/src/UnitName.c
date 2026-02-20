#include "lib.h"
#include "UnitName.h"

static int UnitName_var = 10;

int UnitNameFnc1(int a, int b) {
    int ret = 0;
    if (a == 0)
    {
        dummyFunc01();
        ret = 0;
    }
    else if (b == 0)
    {
        ret = dummyFunc02(b);
    }
    else
    {
        ret = a + b + ++UnitName_var;
    }
    return ret;
}