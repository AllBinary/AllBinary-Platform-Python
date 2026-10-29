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

from org.allbinary.game.graphics.hud.BasicHud import BasicHud
from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
from org.allbinary.game.layer.hud.event.GameNotificationListenerInterface import GameNotificationListenerInterface
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


class GameNotificationHud(BasicHud, GameNotificationListenerInterface):
    NULL_GAME_NOTIFICATION: GameNotificationHud = None

    def _init_fields(self) -> None:
        self.METHOD_NAME: str = "onGameNotificationEvent"
        self.lastGameNotificationEvent: GameNotificationEvent = GameNotification.NULL_GAME_NOTIFICATION_EVENT
    

    def __init__(self, location: int, direction: int, bufferZone: int, basicColor: BasicColor) -> None:
        super().__init__(location, direction, bufferZone, basicColor)
        self._init_fields()
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onGameNotificationEvent(self, gameNotificationEvent: GameNotificationEvent) -> None:
        if self.lastGameNotificationEvent != gameNotificationEvent:
            self.lastGameNotificationEvent = gameNotificationEvent
            self.logUtil.putF(gameNotificationEvent.getString(), self, self.METHOD_NAME)
        self.add(gameNotificationEvent.getString(), gameNotificationEvent.getSeconds(), gameNotificationEvent.getBasicColorP(), gameNotificationEvent.getPermanent())
    

    def add(self, string: str, seconds: int, basicColor: BasicColor, permanent: bool) -> None:
        pass
    

    # throws Exception
    def processTick(self) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def clear(self) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.game.ag.layer.hud.basic.notification.GameNotification import GameNotification


GameNotificationHud.NULL_GAME_NOTIFICATION = GameNotificationHud(BasicHudFactory.getInstance().TOPCENTER, BasicHudFactory.getInstance().HORIZONTAL, 0, BasicColorFactory.getInstance().RED)

