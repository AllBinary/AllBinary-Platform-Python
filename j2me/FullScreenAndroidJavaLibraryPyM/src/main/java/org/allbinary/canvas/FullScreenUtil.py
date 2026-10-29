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
# package org.allbinary.canvas

from __future__ import annotations



class FullScreenUtil:
    instance: FullScreenUtil = None
    

    @staticmethod
    def getInstance() -> FullScreenUtil:
        return FullScreenUtil.instance
    

    # throws Exception
    def initOnRun(self, fullScreenInterface: Canvas, commandListener: CommandListener) -> None:
        pass
    

    def init(self, fullScreenInterface: Canvas) -> None:
        pass
    

    def isScreenChange(self, isFullScreen: bool) -> bool:
        return False
    

    def isScreenChangeCanvas(self, fullScreenInterface: Canvas) -> bool:
        return self.isScreenChange(fullScreenInterface.isFullScreenMode())
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.CommandListener import CommandListener


FullScreenUtil.instance = FullScreenUtil()

