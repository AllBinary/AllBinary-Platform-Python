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

import threading


class CurrentDisplayableFactory:
    instance: CurrentDisplayableFactory = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.canvasStrings: CanvasStrings = CanvasStrings.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.SET_DISPLAYABLE: str = "setDisplayable"
        self.SET_RUNNABLE: str = "setRunnable"
        self.CLEAR_RUNNABLE: str = "clearRunnable"
        self.SET_USED_RUNNABLE: str = "setUsedRunnable"
        self.RUNNABLE: str = "Runnable: "
        self.RUNNABLE_WAS_ALREADY_IN_USE: str = "Runnable was already in use: "
        self.DEFAULT_CHILD_NAME_LIST: BasicArrayList = BasicArrayListD()
        self.displayable: Displayable = NullDisplayable.getInstance()
        self.openGlReadydisplayable: Displayable = NullDisplayable.getInstance()
        self.runnable: GameRunnable = NullWaitGameRunnable.getInstance()
        self.usedRunnable: GameRunnable = NullWaitGameRunnable.getInstance()
    

    @staticmethod
    def getInstance() -> CurrentDisplayableFactory:
        return CurrentDisplayableFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
        self.DEFAULT_CHILD_NAME_LIST.add(self.canvasStrings.ABOUT)
        self.DEFAULT_CHILD_NAME_LIST.add(self.canvasStrings.OPTIONS)
        self.DEFAULT_CHILD_NAME_LIST.add(GameInputMappingCanvas.NAME)
        self.DEFAULT_CHILD_NAME_LIST.add(GameInputMappingInstructionsCanvas.NAME)
        self.DEFAULT_CHILD_NAME_LIST.add(HighScoresCanvas.NAME)
    

    def setMyCanvas(self, displayable: MyCanvas) -> None:
        if isinstance(self.displayable, MyCanvas):
            if displayable.hasChild(self.displayable):
                PreLogUtil.put(str(StringMaker().append("Child Displayable is already set for: ").append(self.stringUtil.toString(displayable))), self, self.SET_DISPLAYABLE)
                return
        self.setDisplayable(displayable)
    

    def setDisplayable(self, displayable: Displayable) -> None:
        self.displayable = displayable
        self.setOpenGlReadydisplayable(displayable)
    

    def setOpenGlReadydisplayable(self, openGlReadydisplayable: Displayable) -> None:
        self.openGlReadydisplayable = openGlReadydisplayable
        self.update()
    

    def getOpenGlReadydisplayable(self) -> Displayable:
        return self.openGlReadydisplayable
    

    def setRunnable(self, runnable: GameRunnable) -> None:
        PreLogUtil.put(str(StringMaker().append(self.RUNNABLE).append(self.stringUtil.toString(runnable))), self, self.SET_RUNNABLE)
        self.runnable = runnable
        if self.usedRunnable != self.runnable:
            self.update()
        else:
            PreLogUtil.put(str(StringMaker().append(self.RUNNABLE_WAS_ALREADY_IN_USE).append(self.stringUtil.toString(runnable))), self, self.SET_RUNNABLE)
    

    def clearRunnable(self) -> None:
        PreLogUtil.put(str(StringMaker().append(self.RUNNABLE).append(self.stringUtil.toString(NullRunnable.getInstance()))), self, self.CLEAR_RUNNABLE)
        self.setUsedRunnable(NullWaitGameRunnable.getInstance())
    

    def update(self) -> None:
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        with self._lock:  # synchronized (self)
            commonSeps: CommonSeps = CommonSeps.getInstance()
            features: Features = Features.getInstance()
            stringMaker: StringMaker = StringMaker()
            stringMaker.append(self.stringUtil.toString(self.openGlReadydisplayable))
            if SWTUtil.isSWT and not features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
                PreLogUtil.put(str(stringMaker.append(commonSeps.SPACE).append(SWTUtil.SWT).append(commonSeps.SPACE).append(self.RUNNABLE).append(self.stringUtil.toString(NullRunnable.getInstance()))), self, self.commonStrings.UPDATE)
                self.setUsedRunnable(NullWaitGameRunnable.getInstance())
            elif J2MEUtil.isHTML():
                PreLogUtil.put(str(stringMaker.append(commonSeps.SPACE).append(GraphicsStrings.getInstance().HTML).append(commonSeps.SPACE).append(self.RUNNABLE).append(self.stringUtil.toString(self.runnable))), self, self.commonStrings.UPDATE)
                self.setUsedRunnable(self.runnable)
            elif isinstance(self.openGlReadydisplayable, DemoCanvas) or isinstance(self.openGlReadydisplayable, AllBinaryGameCanvas) or features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
                PreLogUtil.put(str(stringMaker.append(commonSeps.SPACE).append(str(OpenGLFeatureFactory.getInstance().OPENGL)).append(commonSeps.SPACE).append(self.RUNNABLE).append(self.stringUtil.toString(self.runnable))), self, self.commonStrings.UPDATE)
                self.setUsedRunnable(self.runnable)
            else:
                PreLogUtil.put(str(stringMaker.append(self.RUNNABLE).append(self.stringUtil.toString(NullRunnable.getInstance()))), self, self.commonStrings.UPDATE)
                self.setUsedRunnable(NullWaitGameRunnable.getInstance())
    

    def getDisplayable(self) -> Displayable:
        return self.displayable
    

    def getUsedRunnable(self) -> GameRunnable:
        return self.usedRunnable
    

    def setUsedRunnable(self, usedRunnable: GameRunnable) -> None:
        PreLogUtil.put(str(StringMaker().append(self.RUNNABLE).append(self.stringUtil.toString(self.runnable)).append(CommonSeps.getInstance().COLON_SEP).append(self.stringUtil.toString(usedRunnable))), self, self.SET_USED_RUNNABLE)
        self.usedRunnable = usedRunnable
# from javax.microedition.lcdui.Displayable import Displayable
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.game.displayable.canvas.DemoCanvas import DemoCanvas
from org.allbinary.game.displayable.canvas.GameInputMappingCanvas import GameInputMappingCanvas
from org.allbinary.game.displayable.canvas.GameInputMappingInstructionsCanvas import GameInputMappingInstructionsCanvas
from org.allbinary.game.displayable.canvas.GameRunnable import GameRunnable
from org.allbinary.game.displayable.canvas.NullDisplayable import NullDisplayable
from org.allbinary.game.displayable.canvas.NullWaitGameRunnable import NullWaitGameRunnable
from org.allbinary.game.layer.SWTUtil import SWTUtil
from org.allbinary.game.score.displayable.HighScoresCanvas import HighScoresCanvas
from org.allbinary.graphics.GraphicsStrings import GraphicsStrings
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.thread.NullRunnable import NullRunnable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


CurrentDisplayableFactory.instance = CurrentDisplayableFactory()

