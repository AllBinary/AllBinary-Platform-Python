# Generated Code Do Not Modify
# package org.allbinary.configuration

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class ApplicationConfiguration:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.fullscreen: bool = True
        self.showTitleBar: bool = False
        self.progressBarView: bool = False
    

    @staticmethod
    def getInstance() -> ApplicationConfiguration:
        if ApplicationConfiguration.instance == NullUtil.getInstance().NULL_OBJECT:
            ApplicationConfiguration.instance = ApplicationConfiguration()
        return ApplicationConfiguration.instance
    

    def __init__(self) -> None:
        self._init_fields()
        try:
            self.read()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
    

    # throws Exception
    def read(self) -> None:
        self.setFullscreen(True)
        self.setProgressBarView(False)
        self.setShowTitleBar(False)
        self.logUtil.putF("Read Configuration: " + str(self), self, "read")
    

    # throws Exception
    def write(self) -> None:
        pass
    

    # throws Exception
    def update(self, gameFeature: Feature) -> None:
        if gameFeature == MainFeatureFactory.getInstance().FULL_SCREEN:
            features: Features = Features.getInstance()
            if features.isFeature(gameFeature):
                if not self.isFullscreen():
                    self.setFullscreen(True)
                    self.write()
            else:
                if self.isFullscreen():
                    self.setFullscreen(False)
                    self.write()
    

    def setFullscreen(self, fullscreen: bool) -> None:
        self.fullscreen = fullscreen
    

    def isFullscreen(self) -> bool:
        return self.fullscreen
    

    def setShowTitleBar(self, showTitleBar: bool) -> None:
        self.showTitleBar = showTitleBar
    

    def isShowTitleBar(self) -> bool:
        return self.showTitleBar
    

    def setProgressBarView(self, progressBarView: bool) -> None:
        self.progressBarView = progressBarView
    

    def isProgressBarView(self) -> bool:
        return self.progressBarView
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("isFullscreen: ")
        stringBuffer.appendboolean(self.isFullscreen())
        stringBuffer.append(" isProgressBarView: ")
        stringBuffer.appendboolean(self.isProgressBarView())
        stringBuffer.append(" isShowTitleBar: ")
        stringBuffer.appendboolean(self.isShowTitleBar())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.game.configuration.feature.Feature import Feature
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings


