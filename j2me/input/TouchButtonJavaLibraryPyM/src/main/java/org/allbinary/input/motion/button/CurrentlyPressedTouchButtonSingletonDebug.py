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
# package org.allbinary.input.motion.button

from __future__ import annotations

from org.allbinary.input.motion.button.CurrentlyPressedTouchButtonSingleton import CurrentlyPressedTouchButtonSingleton


class CurrentlyPressedTouchButtonSingletonDebug(CurrentlyPressedTouchButtonSingleton):
    instanceC: CurrentlyPressedTouchButtonSingletonDebug = None

    def _init_fields(self) -> None:
        self.string: str = StringUtil.getInstance().EMPTY_STRING
        self.listString: str = StringUtil.getInstance().EMPTY_STRING
        self.append: str = StringUtil.getInstance().EMPTY_STRING
        self.PRESSED_AND_FIRED: str = "pressed & fired"
        self.PRESSED_AND_NOT_FIRED: str = "pressed in button but not fired"
        self.ASSOCIATED_RELEASED_AND_FIRED: str = "assoc. rel & fired"
        self.RELEASED_AND_FIRED: str = "rel & fired 1"
        self.RELEASED_AND_FIRED_2: str = "rel & fired 2"
        self.RELEASED_AND_NOT_FIRED: str = "rel & not fired"

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CurrentlyPressedTouchButtonSingleton:
        return CurrentlyPressedTouchButtonSingletonDebug.instanceC
    

    def appendTouchButtonInput(self, append: str, touchButtonInput: TouchButtonInput) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(touchButtonInput))
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(append)
        self.append = str(stringBuffer)
        self.string = str(StringMaker().append(self.listString).append(self.append))
    

    def append(self, append: str) -> None:
        self.append = str(StringMaker().append(self.append).append(append))
        self.string = str(StringMaker().append(self.listString).append(self.append))
    

    def clearLog(self, x: int, y: int) -> None:
        self.append = str(StringMaker().append(GPoint.toStringStatic(x, y, 0)).append(CommonSeps.getInstance().SPACE))
        self.string = str(StringMaker().append(self.listString).append(self.append))
    

    def releaseAndNotFired(self) -> None:
        self.append(self.RELEASED_AND_NOT_FIRED)
    

    def releaseAndFired(self, touchButtonInput: TouchButtonInput) -> None:
        self.appendTouchButtonInput(self.RELEASED_AND_FIRED, touchButtonInput)
    

    def releaseAndFired2(self, touchButtonInput: TouchButtonInput) -> None:
        self.appendTouchButtonInput(self.RELEASED_AND_FIRED_2, touchButtonInput)
    

    def releaseAndFiredAssociated(self, touchButtonInput: TouchButtonInput) -> None:
        self.appendTouchButtonInput(self.ASSOCIATED_RELEASED_AND_FIRED, touchButtonInput)
    

    def pressedAndFired(self, touchButtonInput: TouchButtonInput) -> None:
        self.appendTouchButtonInput(self.PRESSED_AND_FIRED, touchButtonInput)
    

    def pressedAndNotFired(self, touchButtonInput: TouchButtonInput) -> None:
        self.appendTouchButtonInput(self.PRESSED_AND_NOT_FIRED, touchButtonInput)
    

    def removeAt(self, index: int) -> TouchButtonInput:
        touchButtonInput: TouchButtonInput = super().removeAt(index)
        self.listString = str(self.list_)
        self.string = str(StringMaker().append(self.listString).append(self.append))
        return touchButtonInput
    

    def remove(self, touchButtonInput: TouchButtonInput) -> bool:
        isRemoved: bool = super().remove(touchButtonInput)
        self.listString = str(self.list_)
        self.string = str(StringMaker().append(self.listString).append(self.append))
        return isRemoved
    

    def add(self, touchButtonInput: TouchButtonInput) -> None:
        super().add(touchButtonInput)
        self.listString = str(self.list_)
        self.string = str(StringMaker().append(self.listString).append(self.append))
    

    def toString(self) -> str:
        return self.string

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps


CurrentlyPressedTouchButtonSingletonDebug.instanceC = CurrentlyPressedTouchButtonSingletonDebug()

