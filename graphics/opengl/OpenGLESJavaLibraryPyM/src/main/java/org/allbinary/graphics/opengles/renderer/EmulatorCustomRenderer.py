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
# package org.allbinary.graphics.opengles.renderer

from __future__ import annotations

import time
import threading


class EmulatorCustomRenderer:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.renderStrings: RendererStrings = RendererStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    def onSurfaceCreated(self, gl: GL10, eglConfig: EGLConfig) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.renderStrings.ON_SURFACE_CREATED)
        initEmulatorFactory: InitEmulatorFactory = InitEmulatorFactory.getInstance()
        if not initEmulatorFactory.isInitEmulator():
            try:
                WAIT_FOR_EMULATOR: str = "Waiting on Emulator Initialization"
                while not initEmulatorFactory.isInitEmulator():
                    PreLogUtil.put(WAIT_FOR_EMULATOR, self, self.renderStrings.ON_SURFACE_CREATED)
                    time.sleep((180) / 1000)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.renderStrings.ON_SURFACE_CREATED, e)
# from javax.microedition.khronos.egl.EGLConfig import EGLConfig
# from javax.microedition.khronos.opengles.GL10 import GL10
from org.allbinary.emulator.InitEmulatorFactory import InitEmulatorFactory
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.graphics.opengles.renderer.RendererStrings import RendererStrings


