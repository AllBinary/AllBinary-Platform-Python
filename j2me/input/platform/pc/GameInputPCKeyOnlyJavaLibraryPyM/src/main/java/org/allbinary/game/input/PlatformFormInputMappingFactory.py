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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class PlatformFormInputMappingFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.inputToGameKeyMapping: InputToGameKeyMapping = InputToGameKeyMapping.getNullInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PlatformFormInputMappingFactory:
        if PlatformFormInputMappingFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            PlatformFormInputMappingFactory.instance = PlatformFormInputMappingFactory()
        return PlatformFormInputMappingFactory.instance
    

    def getOrCreate(self) -> InputToGameKeyMapping:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
        try:
            if self.inputToGameKeyMapping == InputToGameKeyMapping.getNullInstance():
                pcKeyFactory: PCKeyFactory = PCKeyFactory.getInstance()
                inputToGameKeyMapping: InputToGameKeyMapping = InputToGameKeyMapping()
                gameKeyFactory: GameKeyFactory = GameKeyFactory.getInstance()
                inputToGameKeyMapping.add(gameKeyFactory.UP, pcKeyFactory.DPAD_UP)
                inputToGameKeyMapping.add(gameKeyFactory.DOWN, pcKeyFactory.DPAD_DOWN)
                inputToGameKeyMapping.add(gameKeyFactory.LEFT, pcKeyFactory.DPAD_LEFT)
                inputToGameKeyMapping.add(gameKeyFactory.RIGHT, pcKeyFactory.DPAD_RIGHT)
                inputToGameKeyMapping.add(gameKeyFactory.KEY_NUM1, pcKeyFactory.ENTER)
                self.inputToGameKeyMapping = inputToGameKeyMapping
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
        return self.inputToGameKeyMapping
from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


