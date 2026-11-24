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

from org.allbinary.game.ag.layer.hud.basic.notification.GameNotificationHud import GameNotificationHud


class NoGameGameNotificationHud(GameNotificationHud):
    

    def __init__(self) -> None:
        from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        super().__init__(BasicHudFactory.getInstance().TOPCENTER, BasicHudFactory.getInstance().HORIZONTAL, 2, BasicColorFactory.getInstance().RED)
        self.updateMaxWidth = 40
        self.updateMaxHeight = 14
# from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


