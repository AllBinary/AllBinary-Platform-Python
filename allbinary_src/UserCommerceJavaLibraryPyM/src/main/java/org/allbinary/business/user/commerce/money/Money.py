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



class Money:

    def _init_fields(self) -> None:
        self.units: int = None
        self.DEFAULT_CURRENCY: str = "USD"

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, money: Money) -> None:
        self._init_fields()
        self.units = int(money.getUnits())
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.units = int(0)
    

    def _constructor1(self, usDollarStr: str) -> None:
        self._init_fields()
        if usDollarStr is not None and StringValidationUtil.getInstance().isNumber(usDollarStr):
            self.units = int(self.convertUsdToUnits(usDollarStr))
    

    def _constructor1(self, units: int) -> None:
        self._init_fields()
        self.units = int(units)
    

    def isValid(self) -> bool:
        if self.units is not None and int(self.units) > 0 and int(self.units) < 9223372036854775807:
            return True
        else:
            return False
    

    def add(self, moreMoney: Money) -> None:
        self.add(str(moreMoney))
    

    # Java overloaded method: Python keeps the last definition
    def add(self, usDollarStr: str) -> None:
        self.units = int(int(self.units) + self.convertUsdToUnits(usDollarStr))
    

    def subtract(self, usDollarStr: str) -> None:
        self.units = int(int(self.units) - self.convertUsdToUnits(usDollarStr))
    

    def multiply(self, multiplier: float) -> None:
        self.units = int(int(float(int(self.units) * float(multiplier))))
    

    # Java overloaded method: Python keeps the last definition
    def multiply(self, multiplier: int) -> None:
        self.units = int(int(self.units) * multiplier)
    

    def convertUnitsTo(self, currency: str) -> str:
        stringBuffer: StringMaker = StringMaker()
        if ((currency > self.DEFAULT_CURRENCY) - (currency < self.DEFAULT_CURRENCY)) == 0:
            dollar: int = int(self.units) / 100
            cents: int = int(self.units) - (dollar * 100)
            stringBuffer.append(str(int(dollar)))
            stringBuffer.append(AbPathData.getInstance().EXTENSION_SEP)
            if cents < 10:
                stringBuffer.append(CommonPhoneStrings.getInstance().ZERO)
            stringBuffer.append(str(int(cents)))
        return str(stringBuffer)
    

    def convertUsdToUnits(self, usDollarStr: str) -> int:
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
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings


