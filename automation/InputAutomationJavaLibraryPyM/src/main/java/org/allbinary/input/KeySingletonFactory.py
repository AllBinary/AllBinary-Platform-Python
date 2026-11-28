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
# package org.allbinary.input

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class KeySingletonFactory:
    keyStringHashtable: ABHashtable[object, object] = None
    keyArray: list[int] = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def _static_init() -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        STATIC_BLOCK: str = "Static Block"
        try:
            for index in range(0, len(KeySingletonFactory.keyArray)):
                keyAsString: str = KeyEvent.getKeyText(KeySingletonFactory.keyArray[index])
                KeySingletonFactory.keyStringHashtable.put(keyAsString, KeySingletonFactory.keyArray[index])
        except Exception as e:
            logUtil.put(commonStrings.EXCEPTION, "KeySingleFactory", STATIC_BLOCK, e)
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getHashtable() -> ABHashtable[object, object]:
        from org.allbinary.util.ABHashtable import ABHashtable
        return KeySingletonFactory.keyStringHashtable
    

    @staticmethod
    def getInstance(index: int) -> int:
        return str(index)
    

    @staticmethod
    def getArray() -> list[int]:
        return KeySingletonFactory.keyArray
# from java.awt.event.KeyEvent import KeyEvent
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.ABHashtable import ABHashtable


def _KeySingletonFactory_keyStringHashtable() -> object:
    from org.allbinary.logic.StdUtil import StdUtil
    from org.allbinary.util.ABHashtable import ABHashtable
    return StdUtil.getInstance().createHashtable()

lazy_static(KeySingletonFactory, "keyStringHashtable", _KeySingletonFactory_keyStringHashtable)

def _KeySingletonFactory_keyArray() -> object:
    return [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 144, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 61440, 61441, 61442, 61443, 61444, 61445, 61446, 61447, 61448, 61449, 61450, 61451, 30, 107, 65481, 256, 240, 18, 65406, 150, 151, 512, 192, 92, 8, 65368, 161, 162, 3, 20, 514, 12, 93, 258, 513, 44, 65312, 525, 17, 28, 65485, 65489, 134, 136, 129, 133, 138, 139, 130, 135, 137, 128, 141, 132, 140, 143, 131, 142, 110, 127, 111, 515, 40, 35, 10, 61, 27, 516, 517, 24, 65488, 243, 160, 244, 156, 242, 36, 263, 155, 518, 260, 259, 261, 21, 262, 25, 241, 225, 226, 227, 224, 37, 519, 153, 157, 45, 31, 106, 29, 520, 91, 34, 33, 65487, 19, 46, 521, 257, 154, 65482, 222, 152, 39, 522, 145, 59, 108, 108, 16, 47, 32, 65480, 109, 9, 0, 523, 65483, 38, 524]

lazy_static(KeySingletonFactory, "keyArray", _KeySingletonFactory_keyArray)

KeySingletonFactory._static_init()

