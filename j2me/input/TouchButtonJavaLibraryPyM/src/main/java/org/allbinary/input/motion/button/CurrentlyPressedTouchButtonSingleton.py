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



class CurrentlyPressedTouchButtonSingleton:
    instance: CurrentlyPressedTouchButtonSingleton = None

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> CurrentlyPressedTouchButtonSingleton:
        return CurrentlyPressedTouchButtonSingleton.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def size(self) -> int:
        return self.list_.size()
    

    def removeAt(self, index: int) -> TouchButtonInput:
        return self.list_.removeAt(index)
    

    def remove(self, touchButtonInput: TouchButtonInput) -> bool:
        return self.list_.remove(touchButtonInput)
    

    def get(self, index: int) -> TouchButtonInput:
        return self.list_.objectArray[index]
    

    def contains(self, touchButtonInput: TouchButtonInput) -> bool:
        return self.list_.contains(touchButtonInput)
    

    def add(self, touchButtonInput: TouchButtonInput) -> None:
        self.list_.add(touchButtonInput)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


CurrentlyPressedTouchButtonSingleton.instance = CurrentlyPressedTouchButtonSingleton()

