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

from java.lang.JavaRuntimeStatic import lazy_static


class CancelTouchButtonInputFactory:
    instance: object = None

    def _init_fields(self) -> None:
        from org.allbinary.game.input.InputFactory import InputFactory
        self.cancelInputArray: list[TouchButtonInput] = [None] * (InputFactory.getInstance().MAX)
    

    @staticmethod
    def getInstance() -> CancelTouchButtonInputFactory:
        from org.allbinary.logic.NullUtil import NullUtil
        if CancelTouchButtonInputFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            CancelTouchButtonInputFactory.instance = CancelTouchButtonInputFactory()
        return CancelTouchButtonInputFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        self._init_fields()
        basicTouchInputFactory: BasicTouchInputFactory = BasicTouchInputFactory.getInstance()
        for index in range(len(self.cancelInputArray) - 1, 0 - 1, -1):
            self.cancelInputArray[index] = basicTouchInputFactory.NONE
        self.cancelInputArray[basicTouchInputFactory.UP.getId()] = basicTouchInputFactory.DOWN
        self.cancelInputArray[basicTouchInputFactory.DOWN.getId()] = basicTouchInputFactory.UP
        self.cancelInputArray[basicTouchInputFactory.LEFT.getId()] = basicTouchInputFactory.RIGHT
        self.cancelInputArray[basicTouchInputFactory.RIGHT.getId()] = basicTouchInputFactory.LEFT
    

    def getCancel(self, touchButtonInput: TouchButtonInput) -> TouchButtonInput:
        return self.cancelInputArray[touchButtonInput.getId()]
# from org.allbinary.game.input.InputFactory import InputFactory
# from org.allbinary.logic.NullUtil import NullUtil


def _CancelTouchButtonInputFactory_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(CancelTouchButtonInputFactory, "instance", _CancelTouchButtonInputFactory_instance)

