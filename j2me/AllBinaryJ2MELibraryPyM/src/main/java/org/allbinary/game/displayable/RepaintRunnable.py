# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.displayable

from __future__ import annotations

from org.allbinary.thread.ARunnable import ARunnable


class RepaintRunnable(ARunnable):

    def _init_fields(self) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        self.canvas: Canvas = None
    

    def __init__(self, canvas: Canvas) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        super().__init__()
        self._init_fields()
        self.canvas = canvas
    

    def run(self) -> None:
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            self.canvas.repaint()
            DisplayInfoSingleton.getInstance().process()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil: LogUtil = LogUtil.getInstance()
            logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
# from javax.microedition.lcdui.Canvas import Canvas
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings


