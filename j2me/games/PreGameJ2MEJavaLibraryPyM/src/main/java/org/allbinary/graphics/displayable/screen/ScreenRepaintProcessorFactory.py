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
# package org.allbinary.graphics.displayable.screen

from __future__ import annotations



class ScreenRepaintProcessorFactory:
    instance: ScreenRepaintProcessorFactory = None
    

    @staticmethod
    def getInstance() -> ScreenRepaintProcessorFactory:
        return ScreenRepaintProcessorFactory.instance
    

    def __init__(self) -> None:
        pass
    

    def create(self, displayable: Displayable) -> Processor:
        from org.allbinary.graphics.displayable.screen.ScreenRepaintProcessor import ScreenRepaintProcessor
        if not J2MEUtil.isJ2ME():
            return ScreenRepaintProcessor(displayable)
        else:
            return Processor.getInstance()
# from javax.microedition.lcdui.Displayable import Displayable
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.canvas.Processor import Processor


ScreenRepaintProcessorFactory.instance = ScreenRepaintProcessorFactory()

