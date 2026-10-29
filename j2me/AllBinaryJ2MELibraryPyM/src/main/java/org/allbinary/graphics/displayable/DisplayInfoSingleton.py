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
# package org.allbinary.graphics.displayable

from __future__ import annotations



class DisplayInfoSingleton:
    SINGLETON: DisplayInfoSingleton = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonLabels: CommonLabels = CommonLabels.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.ORIENTATION: str = "ORIENTATION"
        self.ADJUSTING_FOR_SCALING_IN_PORTRAIT: str = "Adjusting for Scaling in portrait display ratio: "
        self.ADJUSTING_FOR_SCALING_IN_LANDSCAPE: str = "Adjusting for Scaling in landscape display ratio: "
        self.last: list[int] = [0] * (4)
        self.lastHalf: list[int] = [0] * (4)
        self.full: list[int] = [0] * (4)
        self.top: int = 0
        self.left: int = 0
        self.xOffset: int = 0
        self.yOffset: int = 0
        self.scaleLargestTo: float = 0.0
        self.WIDTH: int = 0
        self.HEIGHT: int = 1
        self.CUSTOM_WIDTH: int = 2
        self.CUSTOM_HEIGHT: int = 3
        self.scalableListener: BaseScalable = BaseScalable()
        self.displayRatio: float = 0.0
        self.ratio: float = 1.0
        self.SET_LAST_SIZE_METHOD_NAME: str = "setLastSize"
        self.FULL_WIDTH: str = " FullWidth: "
        self.FULL_HEIGHT: str = " FullHeight: "
        self.LAST_WIDTH: str = "LastWidth: "
        self.LAST_HEIGHT: str = " LastHeight: "
        self.PORTRAIT: str = "Portrait"
        self.LANDSCAPE: str = "Landscape"
        self.displayChangeEvent: DisplayChangeEvent = DisplayChangeEvent(self)
        self.FIRE_METHOD_NAME: str = "fire"
        self.REASON: str = "reason: "
        self.UPDATE_FROM_ORIENTATION_CHANGE: str = "Updating from Orientation Change "
        self.list_: BasicArrayList = BasicArrayListD()
        self.DISPLAY_INFO: str = "Display Info: "
        self.FULL: str = "full"
        self.LAST: str = "last"
        self.LAST_HALF: str = "lastHalf"
    

    @staticmethod
    def getInstance() -> DisplayInfoSingleton:
        return DisplayInfoSingleton.SINGLETON
    

    def __init__(self) -> None:
        self._init_fields()
        size: int = len(self.last)
        for index in range(0, size):
            self.last[index] = 0
            self.lastHalf[index] = 0
            self.full[index] = 0
        if AndroidUtil.isAndroid():
            self.scaleLargestTo = 640.0
        else:
            self.scaleLargestTo = 1080.0
    

    def getLastHalf(self) -> list[int]:
        return self.lastHalf
    

    def getLast(self) -> list[int]:
        return self.last
    

    def getFull(self) -> list[int]:
        return self.full
    

    def getScaleLargestTo(self) -> float:
        return self.scaleLargestTo
    

    def setScaleLargestTo(self, scaleLargestTo: int) -> None:
        self.scaleLargestTo = float(scaleLargestTo)
    

    def setLastSize(self, aLastWidth: int, aLastHeight: int, reason: str) -> None:
        if self.full[self.WIDTH] != aLastWidth or self.full[self.HEIGHT] != aLastHeight:
            self.setLastSizeForce(aLastWidth, aLastHeight, reason)
    

    def setLastSizeForce(self, aLastWidth: int, aLastHeight: int, reason: str) -> None:
        stringMaker: StringMaker = StringMaker()
        self.logUtil.putF(str(stringMaker.append(CommonLabels.getInstance().START_LABEL).append(reason)), self, self.SET_LAST_SIZE_METHOD_NAME)
        aFullWidth: int = aLastWidth
        aFullHeight: int = aLastHeight
        stringMaker.delete(0, stringMaker.length())
        self.logUtil.putF(str(stringMaker.append(self.FULL_WIDTH).appendint(aFullWidth).append(self.FULL_HEIGHT).appendint(aFullHeight).append(str(self))), self, self.SET_LAST_SIZE_METHOD_NAME)
        operatingSystemInterface: GenericOperatingSystem = OperatingSystemFactory.getInstance().getOperatingSystemInstance()
        if operatingSystemInterface.isOverScan():
            aLastWidth = aLastWidth * operatingSystemInterface.getOverScanXPercent() / 100
            aLastHeight = aLastHeight * operatingSystemInterface.getOverScanYPercent() / 100
        if operatingSystemInterface.isScalable():
            if self.isPortraitWH(aLastWidth, aLastHeight):
                if float(aLastHeight) > self.scaleLargestTo:
                    self.displayRatio = self.scaleLargestTo / float(aLastHeight)
                    self.ratio = float(aLastHeight) / self.scaleLargestTo
                    stringMaker.delete(0, stringMaker.length())
                    self.logUtil.putF(str(stringMaker.append(self.ADJUSTING_FOR_SCALING_IN_PORTRAIT).appendfloat(self.displayRatio)), self, self.SET_LAST_SIZE_METHOD_NAME)
                    aLastWidth = int((float(aLastWidth) * self.displayRatio))
                    aLastHeight = int((float(aLastHeight) * self.displayRatio))
                    self.scalableListener.scale(self.ratio)
                else:
                    self.ratio = 1.0
                    self.scalableListener.scale(self.ratio)
            else:
                if float(aLastWidth) > self.scaleLargestTo:
                    self.displayRatio = self.scaleLargestTo / float(aLastWidth)
                    self.ratio = float(aLastWidth) / self.scaleLargestTo
                    stringMaker.delete(0, stringMaker.length())
                    self.logUtil.putF(str(stringMaker.append(self.ADJUSTING_FOR_SCALING_IN_LANDSCAPE).appendfloat(self.displayRatio)), self, self.SET_LAST_SIZE_METHOD_NAME)
                    aLastWidth = int((float(aLastWidth) * self.displayRatio))
                    aLastHeight = int((float(aLastHeight) * self.displayRatio))
                    self.scalableListener.scale(self.ratio)
                else:
                    self.ratio = 1.0
                    self.scalableListener.scale(self.ratio)
        stringMaker.delete(0, stringMaker.length())
        self.logUtil.putF(str(stringMaker.append(self.LAST_WIDTH).appendint(aLastWidth).append(self.LAST_HEIGHT).appendint(aLastHeight)), self, self.SET_LAST_SIZE_METHOD_NAME)
        self.xOffset = aFullWidth - aLastWidth
        self.yOffset = aFullHeight - aLastHeight
        self.left = self.scalableListener.getLeft(self.xOffset)
        self.top = self.scalableListener.getTop(self.yOffset)
        self.full[self.WIDTH] = aFullWidth
        self.full[self.HEIGHT] = aFullHeight
        self.last[self.WIDTH] = aLastWidth
        self.lastHalf[self.WIDTH] = (self.last[self.WIDTH] >> 1)
        self.last[self.HEIGHT] = aLastHeight
        self.lastHalf[self.HEIGHT] = (self.last[self.HEIGHT] >> 1)
        SWTJOGLProcessor.getInstance().setCustom(aLastWidth, aLastHeight, self.ratio)
        self.add(self.SET_LAST_SIZE_METHOD_NAME)
    

    def isPortraitWH(self, lastWidth: int, lastHeight: int) -> bool:
        if lastHeight > lastWidth:
            return True
        else:
            return False
    

    def isPortrait(self) -> bool:
        return self.isPortraitWH(self.last[self.WIDTH], self.last[self.HEIGHT])
    

    def add(self, reason: str) -> None:
        stringMaker: StringMaker = StringMaker()
        self.logUtil.putF(str(stringMaker.append(self.REASON).append(reason)), self, self.FIRE_METHOD_NAME)
        stringMaker.delete(0, stringMaker.length())
        self.logUtil.putF(self.toStringAppend(stringMaker), self, self.FIRE_METHOD_NAME)
        self.list_.add(reason)
    

    def process(self) -> None:
        try:
            if self.list_.size() > 0:
                self.processForced()
            self.list_.clear()
        except Exception as e:
            PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, self.FIRE_METHOD_NAME, e)
    

    def processForced(self) -> None:
        try:
            swtJOGLProcessor: SWTJOGLProcessor = SWTJOGLProcessor.getInstance()
            swtJOGLProcessor.clear()
            DisplayChangeEventHandler.getInstance().fireEvent(self.displayChangeEvent)
            LastDisplayChangeEventHandler.getInstance().fireEvent(self.displayChangeEvent)
            swtJOGLProcessor.onSurfaceChanged()
        except Exception as e:
            PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, self.FIRE_METHOD_NAME, e)
    

    def update(self, displayable: Displayable, reason: str) -> None:
        aLastWidth: int = displayable.getWidth()
        aLastHeight: int = displayable.getHeight()
        aFullWidth: int = aLastWidth
        aFullHeight: int = aLastHeight
        stringMaker: StringMaker = StringMaker()
        self.logUtil.putF(str(stringMaker.append(CommonLabels.getInstance().START_LABEL).append(reason).append(self.LAST_WIDTH).appendint(aLastWidth).append(self.LAST_HEIGHT).appendint(aLastHeight).append(self.commonSeps.SPACE).append(str(self))), self, self.commonStrings.UPDATE)
        if aLastWidth > 0 and aLastHeight > 0:
            features: Features = Features.getInstance()
            openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
            if not features.isDefault(openGLFeatureFactory.OPENGL) or self.last[self.WIDTH] != aLastWidth or self.last[self.HEIGHT] != aLastHeight:
                stringMaker.delete(0, stringMaker.length())
                self.logUtil.putF(str(stringMaker.append(self.UPDATE_FROM_ORIENTATION_CHANGE)), self, self.commonStrings.UPDATE)
                operatingSystemInterface: GenericOperatingSystem = OperatingSystemFactory.getInstance().getOperatingSystemInstance()
                if operatingSystemInterface.isOverScan():
                    aLastWidth = aLastWidth * operatingSystemInterface.getOverScanXPercent() / 100
                    aLastHeight = aLastHeight * operatingSystemInterface.getOverScanYPercent() / 100
                if operatingSystemInterface.isScalable():
                    if self.isPortraitWH(aLastWidth, aLastHeight):
                        if float(aLastHeight) > self.scaleLargestTo:
                            self.displayRatio = self.scaleLargestTo / float(aLastHeight)
                            self.ratio = float(aLastHeight) / self.scaleLargestTo
                            stringMaker.delete(0, stringMaker.length())
                            self.logUtil.putF(str(stringMaker.append(self.ADJUSTING_FOR_SCALING_IN_PORTRAIT).appendfloat(self.displayRatio)), self, self.commonStrings.UPDATE)
                            aLastWidth = int((float(aLastWidth) * self.displayRatio))
                            aLastHeight = int((float(aLastHeight) * self.displayRatio))
                            self.scalableListener.scale(self.ratio)
                        else:
                            self.ratio = 1.0
                            self.scalableListener.scale(self.ratio)
                    else:
                        if float(aLastWidth) > self.scaleLargestTo:
                            self.displayRatio = self.scaleLargestTo / float(aLastWidth)
                            self.ratio = float(aLastWidth) / self.scaleLargestTo
                            stringMaker.delete(0, stringMaker.length())
                            self.logUtil.putF(str(stringMaker.append(self.ADJUSTING_FOR_SCALING_IN_LANDSCAPE).appendfloat(self.displayRatio)), self, self.commonStrings.UPDATE)
                            aLastWidth = int((float(aLastWidth) * self.displayRatio))
                            aLastHeight = int((float(aLastHeight) * self.displayRatio))
                            self.scalableListener.scale(self.ratio)
                        else:
                            self.ratio = 1.0
                            self.scalableListener.scale(self.ratio)
                stringMaker.delete(0, stringMaker.length())
                self.logUtil.putF(str(stringMaker.append(self.UPDATE_FROM_ORIENTATION_CHANGE).append(self.LAST_WIDTH).appendint(aLastWidth).append(self.LAST_HEIGHT).appendint(aLastHeight)), self, self.commonStrings.UPDATE)
                self.xOffset = aFullWidth - aLastWidth
                self.yOffset = aFullHeight - aLastHeight
                self.left = self.scalableListener.getLeft(self.xOffset)
                self.top = self.scalableListener.getTop(self.yOffset)
                self.full[self.WIDTH] = aFullWidth
                self.full[self.HEIGHT] = aFullHeight
                self.last[self.WIDTH] = aLastWidth
                self.lastHalf[self.WIDTH] = (self.last[self.WIDTH] >> 1)
                self.last[self.HEIGHT] = aLastHeight
                self.lastHalf[self.HEIGHT] = (self.last[self.HEIGHT] >> 1)
                SWTJOGLProcessor.getInstance().setCustom(aLastWidth, aLastHeight, self.ratio)
                self.add(self.commonStrings.UPDATE)
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        return self.toStringAppend(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def toStringAppend(self, stringBuffer: StringMaker) -> str:
        stringBuffer.append(self.DISPLAY_INFO)
        stringBuffer.append(self.FULL)
        stringBuffer.append(self.commonLabels.WIDTH_LABEL)
        stringBuffer.appendint(self.full[self.WIDTH])
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.FULL)
        stringBuffer.append(self.commonLabels.HEIGHT_LABEL)
        stringBuffer.appendint(self.full[self.HEIGHT])
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.LAST)
        stringBuffer.append(self.commonLabels.WIDTH_LABEL)
        stringBuffer.appendint(self.last[self.WIDTH])
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.LAST)
        stringBuffer.append(self.commonLabels.HEIGHT_LABEL)
        stringBuffer.appendint(self.last[self.HEIGHT])
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.LAST_HALF)
        stringBuffer.append(self.commonLabels.WIDTH_LABEL)
        stringBuffer.appendint(self.lastHalf[self.WIDTH])
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.LAST_HALF)
        stringBuffer.append(self.commonLabels.HEIGHT_LABEL)
        stringBuffer.appendint(self.lastHalf[self.HEIGHT])
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append((self.PORTRAIT if self.isPortrait() else self.LANDSCAPE))
        return str(stringBuffer)
    

    def getTop(self) -> int:
        return self.top
    

    def getLeft(self) -> int:
        return self.left
    

    def getLastWidth(self) -> int:
        return self.last[self.WIDTH]
    

    def getLastHeight(self) -> int:
        return self.last[self.HEIGHT]
    

    def getLastHalfWidth(self) -> int:
        return self.lastHalf[self.WIDTH]
    

    def getLastHalfHeight(self) -> int:
        return self.lastHalf[self.HEIGHT]
    

    def getCustomLastWidth(self) -> int:
        return self.last[self.CUSTOM_WIDTH]
    

    def getCustomLastHeight(self) -> int:
        return self.last[self.CUSTOM_HEIGHT]
    

    def getRawLastWidth(self) -> int:
        return self.last[self.WIDTH]
    

    def getRawLastHeight(self) -> int:
        return self.last[self.HEIGHT]
    

    def setCustom(self, width: int, height: int) -> None:
        self.last[self.CUSTOM_WIDTH] = width
        self.lastHalf[self.CUSTOM_WIDTH] = (self.last[self.CUSTOM_WIDTH] >> 1)
        self.last[self.CUSTOM_HEIGHT] = height
        self.lastHalf[self.CUSTOM_HEIGHT] = (self.last[self.CUSTOM_HEIGHT] >> 1)
    

    def setScalableListener(self, scalableListener: BaseScalable) -> None:
        self.scalableListener = scalableListener
    

    def getScalableListener(self) -> ScalableListener:
        return self.scalableListener
    

    def getRatio(self) -> float:
        return self.ratio
    

    def getDisplayRatio(self) -> float:
        return self.displayRatio
    

    def setOffset(self, left: int, top: int) -> None:
        self.left = left
    

    def getxOffset(self) -> int:
        return self.xOffset
    

    def getyOffset(self) -> int:
        return self.yOffset
# from javax.microedition.lcdui.Displayable import Displayable
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
from org.allbinary.graphics.displayable.event.DisplayChangeEventHandler import DisplayChangeEventHandler
from org.allbinary.graphics.displayable.event.LastDisplayChangeEventHandler import LastDisplayChangeEventHandler
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.graphics.threed.SWTJOGLProcessor import SWTJOGLProcessor
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.graphics.displayable.BaseScalable import BaseScalable


DisplayInfoSingleton.SINGLETON = DisplayInfoSingleton()

