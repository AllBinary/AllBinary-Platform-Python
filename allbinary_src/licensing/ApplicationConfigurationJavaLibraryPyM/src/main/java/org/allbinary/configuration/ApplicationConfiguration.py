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
        self.FILE: str = "ReloadConfiguration.dat"
    

    @staticmethod
    def getInstance() -> ApplicationConfiguration:
        if ApplicationConfiguration.instance == NullUtil.getInstance().NULL_OBJECT:
            ApplicationConfiguration.instance = ApplicationConfiguration()
        return ApplicationConfiguration.instance
    

    def __init__(self) -> None:
        self._init_fields()
        try:
            if FileFactory.getInstance().isFile(self.FILE):
                self.read()
            else:
                self.write()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
    

    # throws Exception
    def read(self) -> None:
        fileInputStreamFactory: FileStreamFactory = FileStreamFactory.getInstance()
        fileInputStream: InputStream = fileInputStreamFactory.getFileInputStreamInstance(StringUtil.getInstance().EMPTY_STRING, self.FILE)
        dataInputStream: AbDataInputStream = AbDataInputStream(fileInputStream)
        fullScreen: int = dataInputStream.readInt()
        if fullScreen == 0:
            self.setFullscreen(False)
        elif fullScreen == 1:
            self.setFullscreen(True)
        else:
            raise Exception("Invalid FullScreen ActivityConfiguration")
        progressBarView: int = dataInputStream.readInt()
        if progressBarView == 0:
            self.setProgressBarView(False)
        elif progressBarView == 1:
            self.setProgressBarView(True)
        else:
            raise Exception("Invalid ProgressBarView ActivityConfiguration")
        showTitleBar: int = dataInputStream.readInt()
        if showTitleBar == 0:
            self.setShowTitleBar(False)
        elif showTitleBar == 1:
            self.setShowTitleBar(True)
        else:
            raise Exception("Invalid ShowTitleBar ActivityConfiguration")
        self.logUtil.putF("Read Configuration: " + str(self), self, "read")
    

    # throws Exception
    def write(self) -> None:
        closeable: Closeable = NullCloseable.NULL_CLOSEABLE
        try:
            self.logUtil.putF("Write Configuration: " + str(self), self, "write")
            fileInputStreamFactory: FileStreamFactory = FileStreamFactory.getInstance()
            fileOutputStream: OutputStream = fileInputStreamFactory.getFileOutputStreamInstance(StringUtil.getInstance().EMPTY_STRING, self.FILE)
            dataOutputStream: AbDataOutputStream = AbDataOutputStream(fileOutputStream)
            closeable = dataOutputStream
            if self.isFullscreen():
                dataOutputStream.writeInt(1)
            else:
                dataOutputStream.writeInt(0)
            if self.isProgressBarView():
                dataOutputStream.writeInt(1)
            else:
                dataOutputStream.writeInt(0)
            if self.isShowTitleBar():
                dataOutputStream.writeInt(1)
            else:
                dataOutputStream.writeInt(0)
            dataOutputStream.flush()
        except Exception as e:
            raise e
        finally:
            StreamUtil.getInstance().close(closeable)
    

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
# from java.io.Closeable import Closeable
# from java.io.InputStream import InputStream
# from java.io.OutputStream import OutputStream
from org.allbinary.game.configuration.feature.Feature import Feature
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.AbDataInputStream import AbDataInputStream
from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
from org.allbinary.logic.io.FileStreamFactory import FileStreamFactory
from org.allbinary.logic.io.NullCloseable import NullCloseable
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.FileFactory import FileFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


