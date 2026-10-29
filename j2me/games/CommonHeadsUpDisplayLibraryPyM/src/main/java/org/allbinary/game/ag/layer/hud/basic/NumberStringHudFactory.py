# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.game.ag.layer.hud.basic

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class NumberStringHudFactory:
    instance: object = NullUtil.getInstance()

    def _init_fields(self) -> None:
        self.NULL_NUMBER_STRING_HUD: NumberStringHud = self.createHud()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> NumberStringHudFactory:
        if NumberStringHudFactory.instance == NullUtil.getInstance():
            NumberStringHudFactory.instance = NumberStringHudFactory()
        return NumberStringHudFactory.instance
    

    def createHud(self) -> NumberStringHud:
        from org.allbinary.game.ag.layer.hud.basic.NumberStringHud import NumberStringHud
        try:
            return NumberStringHud(StringUtil.getInstance().EMPTY_STRING, 9, BasicHudFactory.getInstance().ABSOLUTE, 1, 0, BasicColorFactory.getInstance().NULL_COLOR)
        except Exception as e:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
            raise RuntimeError()
from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


