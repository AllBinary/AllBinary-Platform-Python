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
# package org.allbinary.game.layer.hud.event

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class GameNotificationEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.string: str = StringUtil.getInstance().EMPTY_STRING
        self.seconds: int = None
        self.basicColor: BasicColor = BasicColorFactory.getInstance().BLACK
        self.removeable: bool = None
    

    def __init__(self, anyType: object, string: str, seconds: int, basicColor: BasicColor, permanent: bool) -> None:
        super().__init__(anyType)
        self._init_fields()
        self.setString(string)
        self.seconds = seconds
        self.setBasicColorP(basicColor)
        self.removeable = permanent
    

    def getString(self) -> str:
        return self.string
    

    def getSeconds(self) -> int:
        return self.seconds
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
    

    def getPermanent(self) -> bool:
        return self.removeable
    

    def setString(self, string: str) -> None:
        self.string = string
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.string.StringUtil import StringUtil


