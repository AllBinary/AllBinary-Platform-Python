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

from org.allbinary.logic.NullUtil import NullUtil


class CancelTouchButtonInputFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.cancelInputArray: list[TouchButtonInput] = [None] * (InputFactory.getInstance().MAX)
    

    @staticmethod
    def getInstance() -> CancelTouchButtonInputFactory:
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
from org.allbinary.game.input.InputFactory import InputFactory


