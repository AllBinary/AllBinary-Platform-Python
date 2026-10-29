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
# package org.allbinary.graphics.opengles

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class OpenGLConfiguration:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.opengl: bool = False
        self.type_: OpenGLFeature = OpenGLFeatureFactory.getInstance().OPENGL_AS_GAME_THREAD
        self.imageColor: OpenGLFeature = OpenGLFeatureFactory.getInstance().IMAGE_COLOR_DEPTH_4444
        self.color: OpenGLFeature = OpenGLFeatureFactory.getInstance().IMAGE_COLOR_DEPTH_4444
        self.versionSelector: OpenGLFeature = OpenGLFeatureFactory.getInstance().OPENGL_AUTO_SELECT
    

    @staticmethod
    def getInstance() -> OpenGLConfiguration:
        if OpenGLConfiguration.instance == NullUtil.getInstance().NULL_OBJECT:
            OpenGLConfiguration.instance = OpenGLConfiguration()
        return OpenGLConfiguration.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def write(self) -> None:
        pass
    

    # throws Exception
    def init(self) -> None:
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        features: Features = Features.getInstance()
        if ChangedGameFeatureListener.getInstance().isChangedFeature(MainFeatureFactory.getInstance().STATIC):
            if self.isOpenGL():
                if not features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
                    self.logUtil.putF("Turning on OpenGL", self, self.commonStrings.INIT)
                    features.addDefault(OpenGLFeatureFactory.getInstance().OPENGL)
                    self.logUtil.putF("Using OpenGL Type Feature: " + str(self.getType()), self, self.commonStrings.INIT)
                    features.addDefault(self.getType())
                    self.logUtil.putF("Using OpenGL ImageColor Feature: " + str(self.getImageColor()), self, self.commonStrings.INIT)
                    features.addDefault(self.getImageColor())
                    self.logUtil.putF("Using OpenGL Color Feature: " + str(self.getColor()), self, self.commonStrings.INIT)
                    features.addDefault(self.getColor())
                    self.logUtil.putF("Using OpenGL Version Selector Feature: " + str(self.getVersionSelector()), self, self.commonStrings.INIT)
                    features.addDefault(self.getVersionSelector())
            else:
                self.logUtil.putF("OpenGL is Off", self, self.commonStrings.INIT)
        else:
            if self.isOpenGL() and not features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
                PreLogUtil.put("OpenGL is set but not Enabled since Statics where not cleared (Reboot or Complete exit is Required)", self, self.commonStrings.INIT)
        PreLogUtil.put(str(self), self, self.commonStrings.INIT)
    

    # throws Exception
    def update(self, gameFeature: Feature, colorLocked: bool) -> None:
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        features: Features = Features.getInstance()
        openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
        modified: bool = False
        if gameFeature == openGLFeatureFactory.OPENGL:
            if features.isFeature(gameFeature):
                if not self.isOpenGL():
                    self.setOpenGL(True)
                    modified = True
            else:
                if self.isOpenGL():
                    self.setOpenGL(False)
                    modified = True
        if gameFeature == openGLFeatureFactory.OPENGL_AND_GAME_HAVE_DIFFERENT_THREADS or gameFeature == openGLFeatureFactory.OPENGL_AS_GAME_THREAD:
            if features.isFeature(gameFeature):
                if gameFeature != self.getType():
                    self.setType(gameFeature)
                    modified = True
        if gameFeature == openGLFeatureFactory.IMAGE_COLOR_DEPTH_4444 or gameFeature == openGLFeatureFactory.IMAGE_COLOR_DEPTH_565 or gameFeature == openGLFeatureFactory.IMAGE_COLOR_DEPTH_8888:
            if features.isFeature(gameFeature):
                if self.getImageColor() != gameFeature:
                    self.setImageColor(gameFeature)
                    if colorLocked:
                        if gameFeature == openGLFeatureFactory.IMAGE_COLOR_DEPTH_4444:
                            self.setColor(openGLFeatureFactory.OPENGL_COLOR_DEPTH_4444)
                        elif gameFeature == openGLFeatureFactory.IMAGE_COLOR_DEPTH_565:
                            self.setColor(openGLFeatureFactory.OPENGL_COLOR_DEPTH_565)
                        elif gameFeature == openGLFeatureFactory.IMAGE_COLOR_DEPTH_8888:
                            self.setColor(openGLFeatureFactory.OPENGL_COLOR_DEPTH_8888)
                    modified = True
        if gameFeature == openGLFeatureFactory.OPENGL_COLOR_DEPTH_4444 or gameFeature == openGLFeatureFactory.OPENGL_COLOR_DEPTH_565 or gameFeature == openGLFeatureFactory.OPENGL_COLOR_DEPTH_8888:
            if features.isFeature(gameFeature):
                if self.getColor() != gameFeature:
                    self.setColor(gameFeature)
                    modified = True
        if gameFeature == openGLFeatureFactory.OPENGL_AUTO_SELECT or gameFeature == openGLFeatureFactory.OPENGL_MINIMUM:
            if features.isFeature(gameFeature):
                self.setVersionSelector(gameFeature)
            modified = True
    

    def setOpenGL(self, opengl: bool) -> None:
        self.opengl = opengl
    

    def isOpenGL(self) -> bool:
        return self.opengl
    

    def setImageColor(self, imageColor: OpenGLFeature) -> None:
        self.imageColor = imageColor
    

    def getImageColor(self) -> OpenGLFeature:
        return self.imageColor
    

    def setColor(self, color: OpenGLFeature) -> None:
        self.color = color
    

    def getColor(self) -> OpenGLFeature:
        return self.color
    

    def setVersionSelector(self, versionSelector: OpenGLFeature) -> None:
        self.versionSelector = versionSelector
    

    def getVersionSelector(self) -> OpenGLFeature:
        return self.versionSelector
    

    def setType(self, type_: OpenGLFeature) -> None:
        self.type_ = type_
    

    def getType(self) -> OpenGLFeature:
        return self.type_
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringUtil: StringUtil = StringUtil.getInstance()
        stringBuffer.append(" isOpenGL: ")
        stringBuffer.appendboolean(self.isOpenGL())
        stringBuffer.append(" VersionSelector: ")
        stringBuffer.append(stringUtil.toString(self.getVersionSelector()))
        stringBuffer.append(" Type: ")
        stringBuffer.append(stringUtil.toString(self.getType()))
        stringBuffer.append(" Image Color: ")
        stringBuffer.append(stringUtil.toString(self.getImageColor()))
        stringBuffer.append(" Color: ")
        stringBuffer.append(stringUtil.toString(self.getColor()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.game.configuration.event.ChangedGameFeatureListener import ChangedGameFeatureListener
from org.allbinary.game.configuration.feature.Feature import Feature
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory


