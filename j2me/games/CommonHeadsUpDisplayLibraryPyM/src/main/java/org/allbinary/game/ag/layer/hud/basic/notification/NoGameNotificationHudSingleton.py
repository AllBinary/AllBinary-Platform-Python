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



class NoGameNotificationHudSingleton:
    instance: NoGameNotificationHudSingleton = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.gameNotificationHud: GameNotificationHud = GameNotificationHud.NULL_GAME_NOTIFICATION
    

    @staticmethod
    def getInstance() -> NoGameNotificationHudSingleton:
        return NoGameNotificationHudSingleton.instance
    

    def __init__(self) -> None:
        from org.allbinary.game.ag.layer.hud.basic.notification.NoGameGameNotificationHud import NoGameGameNotificationHud
        self._init_fields()
        try:
            basicHudFactory: BasicHudFactory = BasicHudFactory.getInstance()
            class NoGameGameNotificationHud(GameNotificationHud):
                

                def __init__(self) -> None:
                    super().__init__(self.basicHudFactory.TOPCENTER, self.basicHudFactory.HORIZONTAL, 2, BasicColorFactory.getInstance().RED)
                    self.updateMaxWidth = 40
                    self.updateMaxHeight = 14
            self.gameNotificationHud = NoGameGameNotificationHud()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
    

    def getGameNotificationHud(self) -> GameNotificationHud:
        return self.gameNotificationHud
from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.game.ag.layer.hud.basic.notification.GameNotificationHud import GameNotificationHud


NoGameNotificationHudSingleton.instance = NoGameNotificationHudSingleton()

