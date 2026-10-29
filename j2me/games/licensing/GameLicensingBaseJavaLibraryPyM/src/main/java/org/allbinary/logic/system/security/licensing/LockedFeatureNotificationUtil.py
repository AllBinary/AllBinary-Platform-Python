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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations



class LockedFeatureNotificationUtil:
    instance: LockedFeatureNotificationUtil = None

    def _init_fields(self) -> None:
        self.gameNotificationEvent: GameNotificationEvent = GameNotificationEvent(self, LicenseStrings.getInstance().LOCKED, SmallIntegerSingletonFactory.getInstance().getAt(3), BasicColorFactory.getInstance().RED, BooleanFactory.getInstance().FALSE)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> LockedFeatureNotificationUtil:
        return LockedFeatureNotificationUtil.instance
    

    # throws Exception
    def fire(self) -> None:
        PrimaryPlayerQueueFactory.getInstance().add(ErrorSound.getInstance())
        GameNotificationEventHandler.getInstance().fireEvent(self.gameNotificationEvent)
    

    # throws Exception
    def fireWithColor(self, basicColor: BasicColor) -> None:
        PrimaryPlayerQueueFactory.getInstance().add(ErrorSound.getInstance())
        self.gameNotificationEvent.setBasicColorP(basicColor)
        GameNotificationEventHandler.getInstance().fireEvent(self.gameNotificationEvent)
from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.media.audio.ErrorSound import ErrorSound
from org.allbinary.media.audio.PrimaryPlayerQueueFactory import PrimaryPlayerQueueFactory
from org.allbinary.logic.system.security.licensing.LicenseStrings import LicenseStrings


LockedFeatureNotificationUtil.instance = LockedFeatureNotificationUtil()

