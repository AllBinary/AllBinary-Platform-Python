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
# package org.allbinary.graphics.canvas.transition.progress

from __future__ import annotations

from org.allbinary.graphics.displayable.event.DisplayChangeEventListener import DisplayChangeEventListener
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas


class AndroidBasicTitleProgressBar(ProgressCanvas, DisplayChangeEventListener):
    RESOURCE: str = "ProgressImage"
    background: int = 0

    def _init_fields(self) -> None:
        self.showTitleProgressBarRunnable: ARunnable = NullRunnable.getInstance()
        self.dismissTitleProgressBarRunnable: ARunnable = NullRunnable.getInstance()
        self.titleProgressDialogPortionSetProgressRunnable: ARunnable = NullRunnable.getInstance()
        self.titleProgressDialogSetProgressRunnable: ARunnable = NullRunnable.getInstance()
        self.midletActivity: Activity = AndroidUtil.NULL_ACTIVITY
        self.portion: int = 0
        self.IMAGE: list[Image] = [None] * (4)
        self.image: Image = NullImage.NULL_IMAGE
        self.animation: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
    

    def __init__(self, title: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(title, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
        self.init()
        DisplayChangeEventHandler.getInstance().addListenerInterface(self)
        size: int = len(self.IMAGE)
        for index in range(0, size):
            self.IMAGE[index] = NullImage.NULL_IMAGE
    

    def init(self) -> None:
        try:
            if AndroidBasicTitleProgressBar.background != 0:
                ResourceUtil.getInstance().addResource(AndroidBasicTitleProgressBar.RESOURCE, int(AndroidBasicTitleProgressBar.background))
                GameFeatureImageCacheFactory.init()
                self.image = ImageCacheFactory.getInstance().getWithKey(AndroidBasicTitleProgressBar.RESOURCE)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
    

    def initActivity(self, activity: Activity) -> None:
        from org.allbinary.graphics.canvas.transition.progress.ShowTitleProgressBarRunnable import ShowTitleProgressBarRunnable
        from org.allbinary.graphics.canvas.transition.progress.DismissTitleProgressBarRunnable import DismissTitleProgressBarRunnable
        from org.allbinary.graphics.canvas.transition.progress.TitleProgressBarSetProgressRunnable import TitleProgressBarSetProgressRunnable
        from org.allbinary.graphics.canvas.transition.progress.TitleProgressBarPortionSetProgressRunnable import TitleProgressBarPortionSetProgressRunnable
        try:
            if self.midletActivity != activity:
                self.midletActivity = activity
                self.showTitleProgressBarRunnable = ShowTitleProgressBarRunnable(self.midletActivity, self)
                self.dismissTitleProgressBarRunnable = DismissTitleProgressBarRunnable(self.midletActivity, self)
                self.titleProgressDialogSetProgressRunnable = TitleProgressBarSetProgressRunnable(self.midletActivity, self)
                self.titleProgressDialogPortionSetProgressRunnable = TitleProgressBarPortionSetProgressRunnable(self.midletActivity, self)
                self.loadProgressImages()
            self.updateCurrent()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
    

    def updateCurrent(self) -> None:
        try:
            if not self.isBackground():
                self.animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
            elif AndroidBasicTitleProgressBar.background != 0:
                displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
                currentImage: Image = None
                if displayInfo.isPortrait():
                    currentImage = self.getImage(0)
                else:
                    currentImage = self.getImage(2)
                if currentImage is None:
                    self.animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
                else:
                    self.animation = ImageAnimation(currentImage, AnimationBehavior.getInstance())
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.UPDATE, e)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onDisplayChangeEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        try:
            self.loadProgressImages()
            self.updateCurrent()
        except Exception as e:
            self.logUtil.putF(self.commonStrings.EXCEPTION_LABEL + ExceptionUtil.getInstance().getStackTrace(e), self, self.canvasStrings.ON_DISPLAY_CHANGE_EVENT)
            self.animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
    

    def loadProgressImages(self) -> None:
        try:
            displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
            lastWidth: int = displayInfo.getLastWidth()
            lastHeight: int = displayInfo.getLastHeight()
            if displayInfo.isPortraitWH(lastWidth, lastHeight):
                self.setImages(0, lastWidth, lastHeight)
            else:
                self.setImages(2, lastWidth, lastHeight)
        except ValueError as e:
            self.logUtil.putF("IllegalArgumentException " + str(ExceptionUtil.getInstance().getStackTrace(e)), self, "loadProgressImages")
            self.animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        except Exception as e:
            self.logUtil.putF(self.commonStrings.EXCEPTION_LABEL + ExceptionUtil.getInstance().getStackTrace(e), self, "loadProgressImages")
            self.animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
    

    def isInitialized(self) -> bool:
        if self.midletActivity != AndroidUtil.NULL_ACTIVITY:
            return True
        else:
            return False
    

    def start(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.START_METHOD_NAME)
            super().start()
            self.midletActivity.runOnUiThread(self.showTitleProgressBarRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.START_METHOD_NAME, e)
    

    def end(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.END_METHOD_NAME)
            self.midletActivity.runOnUiThread(self.dismissTitleProgressBarRunnable)
            super().end()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.END_METHOD_NAME, e)
    

    def addEarlyPortion(self, value: int, text: str, index: int) -> None:
        try:
            self.portion = value
            super().addEarlyPortion(value, text, index)
            if self.midletActivity != AndroidUtil.NULL_ACTIVITY:
                self.midletActivity.runOnUiThread(self.titleProgressDialogPortionSetProgressRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.ADD_PORTION, e)
    

    def addPortion(self, value: int, text: str, index: int) -> None:
        try:
            self.portion = value
            super().addPortion(value, text, index)
            self.midletActivity.runOnUiThread(self.titleProgressDialogPortionSetProgressRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.ADD_PORTION, e)
    

    def addNormalPortion(self, value: int, text: str) -> None:
        try:
            self.portion = value
            super().addNormalPortion(value, text)
            self.midletActivity.runOnUiThread(self.titleProgressDialogPortionSetProgressRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.ADD_PORTION, e)
    

    def setValue(self, value: int) -> None:
        try:
            super().setValue(value)
            self.midletActivity.runOnUiThread(self.titleProgressDialogSetProgressRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "setValue", e)
    

    def waitUntilDisplayed(self) -> None:
        pass
    

    # throws Exception
    def setImages(self, index: int, lastWidth: int, lastHeight: int) -> None:
        image: Image = self.image
        if image != NullImage.NULL_IMAGE:
            if Features.getInstance().isFeature(MainFeatureFactory.getInstance().FULL_SCREEN):
                if self.IMAGE[index] == NullImage.NULL_IMAGE:
                    self.IMAGE[index] = ImageScaleUtil.getInstance().createImage2(ImageCacheFactory.getInstance(), image, float(lastWidth), float(image.getWidth()), float(lastHeight) - 20.0, float(image.getHeight()), False)
            else:
                nextIndex: int = index + 1
                if self.IMAGE[nextIndex] == NullImage.NULL_IMAGE:
                    self.IMAGE[nextIndex] = ImageScaleUtil.getInstance().createImage2(ImageCacheFactory.getInstance(), image, float(lastWidth), float(image.getWidth()), float(lastHeight) - 28.0, float(image.getHeight()), False)
    

    # throws Exception
    def initOpenGL(self, graphics: Graphics) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.INIT)
        self.image = GameFeatureImageCacheFactory.getInstance().getWithKey(AndroidBasicTitleProgressBar.RESOURCE)
        preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
        size: int = len(self.IMAGE)
        for index in range(0, size):
            if self.IMAGE[index] != NullImage.NULL_IMAGE:
                self.IMAGE[index] = preResourceImageUtil.encapsulate(self.IMAGE[index])
        self.updateCurrent()
    

    # throws Exception
    def update(self, graphics: Graphics) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.UPDATE)
        self.initOpenGL(graphics)
        self.image = GameFeatureImageCacheFactory.getInstance().getWithKey(AndroidBasicTitleProgressBar.RESOURCE)
        preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
        size: int = len(self.IMAGE)
        for index in range(0, size):
            if self.IMAGE[index] != NullImage.NULL_IMAGE:
                preResourceImageUtil.update(graphics, self.IMAGE[index])
    

    # throws Exception
    def getImage(self, index: int) -> Image:
        image: Image = NullImage.NULL_IMAGE
        if Features.getInstance().isFeature(MainFeatureFactory.getInstance().FULL_SCREEN):
            image = self.IMAGE[index]
        else:
            image = self.IMAGE[index + 1]
        return image
    

    def paint2(self, graphics: Graphics) -> None:
        try:
            self.animation.paintXY(graphics, 0, 20)
            super().paint2(graphics)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.canvasStrings.PAINT, e)
    

    @staticmethod
    def setBackgroundResource(background: int) -> None:
        AndroidBasicTitleProgressBar.background = background
    

    def setBackground(self, background: bool) -> None:
        super().setBackground(background)
        self.updateCurrent()
    

    def setPortion(self, portion: int) -> None:
        self.portion = portion
    

    def getPortion(self) -> int:
        return self.portion
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from android.app.Activity import Activity
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.java.exception.ExceptionUtil import ExceptionUtil
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
from org.allbinary.graphics.displayable.event.DisplayChangeEventHandler import DisplayChangeEventHandler
from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
from org.allbinary.media.image.ImageScaleUtil import ImageScaleUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.animation.image.ImageAnimation import ImageAnimation
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.thread.ARunnable import ARunnable
from org.allbinary.thread.NullRunnable import NullRunnable


