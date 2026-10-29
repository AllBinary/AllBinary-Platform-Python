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

import threading
from org.allbinary.logic.NullUtil import NullUtil


class BasicTouchInputFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.SPECIAL_BUTTON_SEVEN_TESTING_ONLY: TouchButtonInput = None
        self.SPECIAL_BUTTON_EIGHT_TESTING_ONLY: TouchButtonInput = None
        self.SPECIAL_BUTTON_SIX: TouchButtonInput = None
        self.SPECIAL_BUTTON_FIVE: TouchButtonInput = None
        self.SPECIAL_BUTTON_FOUR: TouchButtonInput = None
        self.SPECIAL_BUTTON_THREE: TouchButtonInput = None
        self.SPECIAL_BUTTON_TWO: TouchButtonInput = None
        self.SPECIAL_BUTTON_ONE: TouchButtonInput = None
        self.UP: TouchButtonInput = None
        self.LEFT: TouchButtonInput = None
        self.RIGHT: TouchButtonInput = None
        self.DOWN: TouchButtonInput = None
        self.NONE: TouchButtonInput = None
        self.initialized: bool = False
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> BasicTouchInputFactory:
        if BasicTouchInputFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            BasicTouchInputFactory.instance = BasicTouchInputFactory()
        return BasicTouchInputFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput
        self._init_fields()
        MAX: int = InputFactory.getInstance().MAX
        self.SPECIAL_BUTTON_SEVEN_TESTING_ONLY = TouchButtonInput(MAX - 41, "Button 7 - Testing Only May Cross Over Key Values")
        self.SPECIAL_BUTTON_EIGHT_TESTING_ONLY = TouchButtonInput(MAX - 42, "Button 8 - Testing Only May Cross Over Key Values")
        self.SPECIAL_BUTTON_SIX = TouchButtonInput(MAX - 30, "Button 6")
        self.SPECIAL_BUTTON_FIVE = TouchButtonInput(MAX - 31, "Button 5")
        self.SPECIAL_BUTTON_FOUR = TouchButtonInput(MAX - 32, "Button 4")
        self.SPECIAL_BUTTON_THREE = TouchButtonInput(MAX - 33, "Button 3")
        self.SPECIAL_BUTTON_TWO = TouchButtonInput(MAX - 34, "Button 2")
        self.SPECIAL_BUTTON_ONE = TouchButtonInput(MAX - 35, "Button 1")
        self.UP = TouchButtonInput(MAX - 36, "Up Button")
        self.LEFT = TouchButtonInput(MAX - 37, "Left Button")
        self.RIGHT = TouchButtonInput(MAX - 38, "Right Button")
        self.DOWN = TouchButtonInput(MAX - 39, "Down Button")
        self.NONE = TouchButtonInput(MAX - 40, "No Button")
    

    def init(self, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        with self._lock:
            return self._init_unlocked(inputToGameKeyMapping)

    def _init_unlocked(self, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        if not self.initialized:
            self.initialized = True
            self.list_.add(self.UP)
            self.list_.add(self.LEFT)
            self.list_.add(self.RIGHT)
            self.list_.add(self.DOWN)
            self.list_.add(self.SPECIAL_BUTTON_TWO)
            self.list_.add(self.SPECIAL_BUTTON_FOUR)
            self.list_.add(self.SPECIAL_BUTTON_THREE)
            self.list_.add(self.SPECIAL_BUTTON_ONE)
            self.list_.add(self.SPECIAL_BUTTON_FIVE)
            self.list_.add(self.SPECIAL_BUTTON_SIX)
            self.list_.add(self.SPECIAL_BUTTON_SIX)
            self.list_.add(self.SPECIAL_BUTTON_SEVEN_TESTING_ONLY)
            self.list_.add(self.SPECIAL_BUTTON_EIGHT_TESTING_ONLY)
            self.updateAllFromList(self.list_, inputToGameKeyMapping)
    

    def updateAll(self, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        self.updateAllFromList(self.list_, inputToGameKeyMapping)
    

    def updateAllFromList(self, list_: BasicArrayList, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).appendint(list_.size())), self, "updateAll")
        touchButtonInput: TouchButtonInput = None
        for index in range(list_.size() - 1, 0 - 1, -1):
            touchButtonInput = list_.objectArray[index]
            touchButtonInput.update(inputToGameKeyMapping)
    

    def getList(self) -> BasicArrayList:
        return self.list_
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


