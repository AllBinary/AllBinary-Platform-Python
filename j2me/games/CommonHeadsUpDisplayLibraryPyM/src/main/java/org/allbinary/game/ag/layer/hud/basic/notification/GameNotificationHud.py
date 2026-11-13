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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.graphics.hud.BasicHud import BasicHud
from org.allbinary.game.layer.hud.event.GameNotificationListenerInterface import GameNotificationListenerInterface


class GameNotificationHud(BasicHud, GameNotificationListenerInterface):
    NULL_GAME_NOTIFICATION: GameNotificationHud = None

    def _init_fields(self) -> None:
        from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
        self.METHOD_NAME: str = "onGameNotificationEvent"
        self.lastGameNotificationEvent: GameNotificationEvent = GameNotification.NULL_GAME_NOTIFICATION_EVENT
    

    def __init__(self, location: int, direction: int, bufferZone: int, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(location, direction, bufferZone, basicColor)
        self._init_fields()
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onGameNotificationEvent(self, gameNotificationEvent: GameNotificationEvent) -> None:
        from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
        if self.lastGameNotificationEvent != gameNotificationEvent:
            self.lastGameNotificationEvent = gameNotificationEvent
            self.logUtil.putF(gameNotificationEvent.getString(), self, self.METHOD_NAME)
        self.add(gameNotificationEvent.getString(), gameNotificationEvent.getSeconds(), gameNotificationEvent.getBasicColorP(), gameNotificationEvent.getPermanent())
    

    def add(self, string: str, seconds: int, basicColor: BasicColor, permanent: bool) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        pass
    

    # throws Exception
    def processTick(self) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def clear(self) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
# from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.game.ag.layer.hud.basic.notification.GameNotification import GameNotification


def _GameNotificationHud_NULL_GAME_NOTIFICATION() -> object:
    from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
    from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
    return GameNotificationHud(BasicHudFactory.getInstance().TOPCENTER, BasicHudFactory.getInstance().HORIZONTAL, 0, BasicColorFactory.getInstance().RED)

lazy_static(GameNotificationHud, "NULL_GAME_NOTIFICATION", _GameNotificationHud_NULL_GAME_NOTIFICATION)

