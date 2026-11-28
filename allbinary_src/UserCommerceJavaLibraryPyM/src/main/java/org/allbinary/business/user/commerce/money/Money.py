#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.business.user.commerce.money

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide


class Money:

    def _init_fields(self) -> None:
        if "units" not in vars(self): self.units: int = None
        self.DEFAULT_CURRENCY: str = "USD"

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)
        elif len(args) == 0:
            __class__._constructor0(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "Money" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        elif True and (args[0] is None or isinstance(args[0], str)):
            __class__._constructor1_2(self, *args)
        else:
            __class__._constructor1_3(self, *args)
    

    def _constructor1_1(self, money: Money) -> None:
        __class__._init_fields(self)
        self.units = int(money.getUnits())
    

    def _constructor0(self) -> None:
        __class__._init_fields(self)
        self.units = int(0)
    

    def _constructor1_2(self, usDollarStr: str) -> None:
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        __class__._init_fields(self)
        if usDollarStr is not None and StringValidationUtil.getInstance().isNumber(usDollarStr):
            self.units = int(self.convertUsdToUnits(usDollarStr))
    

    def _constructor1_3(self, units: int) -> None:
        __class__._init_fields(self)
        self.units = int(units)
    

    def isValid(self) -> bool:
        if self.units is not None and int(self.units) > 0 and int(self.units) < 9223372036854775807:
            return True
        else:
            return False
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def add_j1_1(self, moreMoney: Money) -> None:
        self.add(str(moreMoney))
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def add_j1_2(self, usDollarStr: str) -> None:
        self.units = int(int(self.units) + self.convertUsdToUnits(usDollarStr))

    def add(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "Money" for base in type(args[0]).__mro__)):
            return __class__.__dict__["add_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["add_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("add_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().add(*args)
    

    def subtract(self, usDollarStr: str) -> None:
        self.units = int(int(self.units) - self.convertUsdToUnits(usDollarStr))
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def multiply_j1_1(self, multiplier: float) -> None:
        self.units = int(int(float(int(self.units) * float(multiplier))))
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def multiply_j1_2(self, multiplier: int) -> None:
        self.units = int(int(self.units) * multiplier)

    def multiply(self, *args):
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return __class__.__dict__["multiply_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["multiply_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("multiply_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().multiply(*args)
    

    def convertUnitsTo(self, currency: str) -> str:
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        stringBuffer: StringMaker = StringMaker()
        if ((currency > self.DEFAULT_CURRENCY) - (currency < self.DEFAULT_CURRENCY)) == 0:
            dollar: int = java_divide(int(self.units), 100)
            
            cents: int = int(self.units) - (dollar * 100)
            stringBuffer.append(str(int(dollar)))
            stringBuffer.append(AbPathData.getInstance().EXTENSION_SEP)
            if cents < 10:
                stringBuffer.append(CommonPhoneStrings.getInstance().ZERO)
            stringBuffer.append(str(int(cents)))
        return str(stringBuffer)
    

    def convertUsdToUnits(self, usDollarStr: str) -> int:
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringUtil import StringUtil
        localUnit: int = 0
        index: int = usDollarStr.find(AbPathData.getInstance().EXTENSION_SEP)
        stringUtil: StringUtil = StringUtil.getInstance()
        dollarStr: str = stringUtil.EMPTY_STRING
        centsStr: str = stringUtil.EMPTY_STRING
        if index < 1:
            dollarStr = str(usDollarStr)
            centsStr = "00"
        else:
            dollarStr = str(usDollarStr[0:index])
            centsStr = str(usDollarStr[index + 1:])
        localUnit = int(int(int(int(dollarStr)) * 100))
        localUnit += int(int(centsStr))
        return localUnit
    

    def getUnits(self) -> int:
        return int(self.units)
    

    def getUnitsLong(self) -> int:
        return self.units
    

    def toString(self) -> str:
        return str(self.convertUnitsTo(self.DEFAULT_CURRENCY))

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings


