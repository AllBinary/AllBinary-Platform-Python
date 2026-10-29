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
        self.SPECIAL_BUTTON_SIX: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 30, "Button 6")
        self.SPECIAL_BUTTON_FIVE: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 31, "Button 5")
        self.SPECIAL_BUTTON_FOUR: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 32, "Button 4")
        self.SPECIAL_BUTTON_THREE: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 33, "Button 3")
        self.SPECIAL_BUTTON_TWO: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 34, "Button 2")
        self.SPECIAL_BUTTON_ONE: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 35, "Button 1")
        self.UP: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 36, "Up Button")
        self.LEFT: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 37, "Left Button")
        self.RIGHT: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 38, "Right Button")
        self.DOWN: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 39, "Down Button")
        self.NONE: TouchButtonInput = TouchButtonInput(InputFactory.getInstance().MAX - 40, "No Button")
        self.initialized: bool = False
        self.list_: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicTouchInputFactory:
        if BasicTouchInputFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            BasicTouchInputFactory.instance = BasicTouchInputFactory()
        return BasicTouchInputFactory.instance
    

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
            self.updateAllList(self.list_, inputToGameKeyMapping)
    

    def updateAll(self, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        self.updateAllList(self.getList(), inputToGameKeyMapping)
    

    def updateAllList(self, list_: BasicArrayList, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START).appendint(list_.size())), self, "updateAll")
        for index in range(list_.size() - 1, 0 - 1, -1):
            touchButtonInput: TouchButtonInput = list_.get(index)
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
from org.allbinary.input.motion.button.TouchButtonInput import TouchButtonInput


