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
# package org.allbinary.midlet

from __future__ import annotations



class MidletExitProcessorFactory:
    instance: MidletExitProcessorFactory = None
    

    @staticmethod
    def getInstance() -> MidletExitProcessorFactory:
        return MidletExitProcessorFactory.instance
    

    def getExitInstance(self, midlet: MIDlet) -> Processor:
        from org.allbinary.midlet.MidletExitProcessor import MidletExitProcessor
        if AppletUtil.isAppletLoader(midlet) or J2MEUtil.isJ2ME():
            return Processor.getInstance()
        else:
            return MidletExitProcessor(midlet)
# from javax.microedition.midlet.MIDlet import MIDlet
from org.allbinary.AppletUtil import AppletUtil
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.canvas.Processor import Processor


MidletExitProcessorFactory.instance = MidletExitProcessorFactory()

