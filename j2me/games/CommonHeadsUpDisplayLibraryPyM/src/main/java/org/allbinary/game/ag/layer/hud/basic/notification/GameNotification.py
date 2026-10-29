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
# package org.allbinary.game.ag.layer.hud.basic.notification

from __future__ import annotations

from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.string.StringUtil import StringUtil


class GameNotification:
    NULL_GAME_NOTIFICATION_EVENT: GameNotificationEvent = GameNotificationEvent(NullUtil.getInstance().NULL_OBJECT, StringUtil.getInstance().EMPTY_STRING, int(0), BasicColorFactory.getInstance().RED, BooleanFactory.getInstance().FALSE)

    def _init_fields(self) -> None:
        self.stringList: BasicArrayList = BasicArrayListD()
        self.timeList: BasicArrayList = BasicArrayListD()
        self.colorList: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    def add(self, string: str, seconds: int, basicColor: BasicColor) -> None:
        if not self.stringList.contains(string):
            self.stringList.add(string)
            self.timeList.add(seconds)
            self.colorList.add(basicColor)
    

    def clear(self) -> None:
        self.stringList.clear()
        self.timeList.clear()
        self.colorList.clear()
    

    def getSize(self) -> int:
        return self.stringList.size()
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


