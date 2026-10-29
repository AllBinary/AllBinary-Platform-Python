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
# package org.allbinary.game.ag.layer.hud.basic

from __future__ import annotations

from org.allbinary.game.ag.layer.hud.basic.notification.GameNotificationHud import GameNotificationHud
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface


class PlayerGameNotificationHud(GameNotificationHud, UpdateMyFontInterface):
    class SetAndRemoveProcessor(Processor):

        def _init_fields(self) -> None:
            self.updateMeasurementProcessor: PlayerGameNotificationHud = None
        

        def __init__(self, updateMeasurementProcessor: PlayerGameNotificationHud) -> None:
            super().__init__()
            self._init_fields()
            self.updateMeasurementProcessor = updateMeasurementProcessor
        

        # throws Exception
        def process(self) -> None:
            self.updateMeasurementProcessor.setAndRemoveProcess()
    class NextUnremoveableProcessor(Processor):

        def _init_fields(self) -> None:
            self.updateMeasurementProcessor: PlayerGameNotificationHud = None
        

        def __init__(self, updateMeasurementProcessor: PlayerGameNotificationHud) -> None:
            super().__init__()
            self._init_fields()
            self.updateMeasurementProcessor = updateMeasurementProcessor
        

        # throws Exception
        def process(self) -> None:
            self.updateMeasurementProcessor.setNextUnremoveableProcess()

    def _init_fields(self) -> None:
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
        self.EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.circularIndexUtil: CircularIndexUtil = None
        self.gameNotification: GameNotification = GameNotification()
        self.permanentGameNotification: GameNotification = GameNotification()
        self.setAndRemoveProcessor: Processor = SetAndRemoveProcessor(self)
        self.nextUnremoveableProcessor: Processor = NextUnremoveableProcessor(self)
        self.processor: Processor = Processor.getInstance()
        self.PERMANENT_GAME_NOTIFICATION: str = "Permanent Game Notification: "
        self.lastString: str = StringUtil.getInstance().EMPTY_STRING
        self.string: str = self.EMPTY_STRING
        self.point: CustomGPoint = CustomGPoint.NULL_CUSTOM_POINT
        self.width: int = 0
    

    def __init__(self, location: int, direction: int, bufferZone: int, basicColor: BasicColor) -> None:
        super().__init__(location, direction, bufferZone, basicColor)
        self._init_fields()
        self.circularIndexUtil = CircularIndexUtil.createInstance(0)
        gameNotificationEventHandler: GameNotificationEventHandler = GameNotificationEventHandler.getInstance()
        gameNotificationEventHandler.removeAllListeners()
        gameNotificationEventHandler.addListenerInterface(self)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        try:
            super().updateMeasurement(graphics)
            font: Font = graphics.getFont()
            self.width = font.stringWidth(self.string)
            self.processor.process()
            self.processor = Processor.getInstance()
        except Exception as e:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.put(commonStrings.EXCEPTION, self, commonStrings.UPDATE, e)
    

    def getPoint(self, x: int, y: int) -> GPoint:
        self.point = CustomGPoint.getInstance3(0, 0)
        self.point.setX(x)
        self.point.setY(y)
        return self.point
    

    def add(self, string: str, seconds: int, basicColor: BasicColor, permanent: bool) -> None:
        if permanent:
            if self.lastString != string:
                self.lastString = string
                self.logUtil.putF(str(StringMaker().append(self.PERMANENT_GAME_NOTIFICATION).append(string)), self, self.commonStrings.ADD)
            self.permanentGameNotification.add(string, seconds, basicColor)
            self.circularIndexUtil.setSize(self.permanentGameNotification.getSize())
        else:
            self.gameNotification.add(string, seconds, basicColor)
    

    # throws Exception
    def processTick(self) -> None:
        if self.timeDelayHelper.isTime(self.gameTickTimeDelayHelper.startTime):
            gameAdState: GameAdState = GameAdStateFactory.getInstance().getCurrentInstance()
            if gameAdState.isShowingAtLocation(self.getLocation()):
                self.offsetY = -54
            else:
                self.offsetY = 0
            if self.gameNotification.getSize() > 0:
                self.setAndRemove()
            elif self.permanentGameNotification.getSize() > 0:
                self.setNextUnremoveable()
            else:
                self.string = self.EMPTY_STRING
    

    # throws Exception
    def setAndRemove(self) -> None:
        self.string = self.gameNotification.stringList.removeAt(0)
        self.processor = self.setAndRemoveProcessor
    

    # throws Exception
    def setAndRemoveProcess(self) -> None:
        self.setX((self.displayInfo.getLastWidth() - self.width) >> 1)
        self.point.setX(self.getX())
        self.point.setY(self.getY())
        time: int = self.gameNotification.timeList.removeAt(0)
        iTime: int = int(time) * 1000
        if iTime == 0:
            iTime = 500
        self.timeDelayHelper.delay = iTime
        self.setBasicColorP(self.gameNotification.colorList.removeAt(0))
    

    # throws Exception
    def setNextUnremoveable(self) -> None:
        index: int = self.circularIndexUtil.getIndex()
        self.string = self.permanentGameNotification.stringList.objectArray[index]
        self.processor = self.nextUnremoveableProcessor
    

    # throws Exception
    def setNextUnremoveableProcess(self) -> None:
        index: int = self.circularIndexUtil.getIndex()
        self.setX((self.displayInfo.getLastWidth() - self.width) >> 1)
        self.point.setX(self.getX())
        self.point.setY(self.getY())
        time: int = self.permanentGameNotification.timeList.objectArray[index]
        self.timeDelayHelper.delay = int(time) * 1000
        self.setBasicColorP(self.permanentGameNotification.colorList.objectArray[index])
        self.circularIndexUtil.next()
    

    def clear(self) -> None:
        self.gameNotification.clear()
        self.permanentGameNotification.clear()
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        super().paintString(graphics, self.string)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.business.advertisement.GameAdStateFactory import GameAdStateFactory
from org.allbinary.canvas.Processor import Processor
from org.allbinary.game.GameAdState import GameAdState
from org.allbinary.game.ag.layer.hud.basic.notification.GameNotification import GameNotification
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.graphics.CustomGPoint import CustomGPoint
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
from org.allbinary.game.ag.layer.hud.basic.SetAndRemoveProcessor import SetAndRemoveProcessor
from org.allbinary.game.ag.layer.hud.basic.NextUnremoveableProcessor import NextUnremoveableProcessor


