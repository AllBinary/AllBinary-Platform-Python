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
# package org.allbinary.game.input.mapping

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.game.input.mapping.InputMapping import InputMapping


class InputToGameKeyMapping(InputMapping):
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.gameKeyFactory: GameKeyFactory = GameKeyFactory.getInstance()
        self.mappedGameKeys: list[GameKey] = [self.gameKeyFactory.UP, self.gameKeyFactory.DOWN, self.gameKeyFactory.LEFT, self.gameKeyFactory.RIGHT]
        self.platformToGameKeyMapping: list[GameKey] = [None] * (InputFactory.getInstance().MAX)
        self.negativePlatformToGameKeyMapping: list[GameKey] = [None] * (0)
    

    @staticmethod
    def getNullInstance() -> InputToGameKeyMapping:
        if InputToGameKeyMapping.instance == NullUtil.getInstance().NULL_OBJECT:
            InputToGameKeyMapping.instance = InputToGameKeyMapping()
        return InputToGameKeyMapping.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.clear()
    

    def clear(self) -> None:
        for index in range(len(self.platformToGameKeyMapping) - 1, 0 - 1, -1):
            self.platformToGameKeyMapping[index] = self.gameKeyFactory.NONE
    

    def removeAll(self) -> None:
        super().removeAll()
        self.clear()
    

    def addMapping(self, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        for index in range(inputToGameKeyMapping.getMaxMappable() - 1, 0 - 1, -1):
            input: Input = inputToGameKeyMapping.getInstance(index)
            if input != self.gameKeyFactory.NONE:
                self.addAll(input, inputToGameKeyMapping.getMappedInput(input))
    

    def addAll(self, input: Input, list_: BasicArrayList) -> None:
        for index in range(list_.size() - 1, 0 - 1, -1):
            mappedToInput: Input = list_.objectArray[index]
            self.add(input, mappedToInput)
    

    def add(self, input: Input, mappedToInput: Input) -> None:
        super().add(input, mappedToInput)
        self.set(input, mappedToInput)
    

    def remove(self, input: Input, mappedToInput: Input) -> None:
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append(StringUtil.getInstance().toString(input)).append(" == ").append(StringUtil.getInstance().toString(mappedToInput))), self, "InputToGameKeyMapping::remove")
        super().remove(input, mappedToInput)
        self.set(input, self.gameKeyFactory.NONE)
    

    def set(self, input: Input, mappedToInput: Input) -> None:
        id: int = mappedToInput.getId()
        if id >= 0 and id < len(self.platformToGameKeyMapping):
            self.platformToGameKeyMapping[id] = input
    

    def getMaxMappable(self) -> int:
        return len(self.platformToGameKeyMapping)
    

    def getReverseInstance(self, id: int) -> BasicArrayList:
        list_: BasicArrayList = BasicArrayListD()
        inputFactory: InputFactory = InputFactory.getInstance()
        for index in range(0, len(self.platformToGameKeyMapping)):
            if self.platformToGameKeyMapping[index].getId() == id:
                input: Input = inputFactory.getInstanceById(index)
                if input is not None:
                    list_.add(input)
        return list_
    

    # throws Exception
    def initGameKey(self, canvas: Canvas, gameKey: GameKey) -> None:
        key: int = canvas.getKeyCode(gameKey.getId())
        if key < 0 and -key < len(self.negativePlatformToGameKeyMapping):
            self.negativePlatformToGameKeyMapping[-key] = gameKey
        elif key > 0:
            if self.platformToGameKeyMapping[key] == self.gameKeyFactory.NONE:
                self.platformToGameKeyMapping[key] = gameKey
        else:
            PreLogUtil.putOE(str(StringMaker().append(str(gameKey)).append(CommonSeps.getInstance().COLON_SEP).appendint(key)), self, self.commonStrings.INIT, Exception())
    

    # throws Exception
    def getSmallestCanvasGameKeyCode(self, canvas: Canvas) -> int:
        nextKey: int = 0
        smallestKey: int = 0
        index = len(self.mappedGameKeys)
        while (index := index - 1) >= 0:
            nextKey = canvas.getKeyCode(self.mappedGameKeys[index].getId())
            if nextKey < smallestKey:
                smallestKey = nextKey
        return smallestKey
    

    def init(self, canvas: Canvas) -> None:
        try:
            negativePlatformToGameKeyMapping: list[GameKey] = [None] * (0)
            smallestKey: int = self.getSmallestCanvasGameKeyCode(canvas)
            if smallestKey < 0:
                smallestKey -= 1
                if smallestKey < -256:
                    smallestKey = -256
                negativePlatformToGameKeyMapping = [None] * (-smallestKey)
                index = len(negativePlatformToGameKeyMapping)
                while (index := index - 1) >= 0:
                    negativePlatformToGameKeyMapping[index] = self.gameKeyFactory.NONE
                self.negativePlatformToGameKeyMapping = negativePlatformToGameKeyMapping
            index = len(self.mappedGameKeys)
            while (index := index - 1) >= 0:
                self.initGameKey(canvas, self.mappedGameKeys[index])
        except BaseException as t:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, t)
    

    def getInstanceForCanvas(self, canvas: Canvas, id: int) -> GameKey:
        if id >= 0 and id < len(self.platformToGameKeyMapping):
            return self.platformToGameKeyMapping[id]
        elif id < 0 and -id < len(self.negativePlatformToGameKeyMapping):
            return self.negativePlatformToGameKeyMapping[-id]
        else:
            return self.gameKeyFactory.NONE
    

    def getInstance(self, id: int) -> GameKey:
        if id >= 0 and id < len(self.platformToGameKeyMapping):
            return self.platformToGameKeyMapping[id]
        elif id < 0 and -id < len(self.negativePlatformToGameKeyMapping):
            return self.negativePlatformToGameKeyMapping[-id]
        else:
            return self.gameKeyFactory.NONE
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
from org.allbinary.game.input.Input import Input
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


