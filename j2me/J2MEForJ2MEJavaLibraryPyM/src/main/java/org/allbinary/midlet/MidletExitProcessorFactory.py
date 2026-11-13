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

from java.lang.JavaRuntimeStatic import lazy_static


class MidletExitProcessorFactory:
    instance: MidletExitProcessorFactory = None
    

    @staticmethod
    def getInstance() -> MidletExitProcessorFactory:
        return MidletExitProcessorFactory.instance
    

    def getExitInstance(self, midlet: MIDlet) -> Processor:
        from org.allbinary.midlet.MidletExitProcessor import MidletExitProcessor
        from javax.microedition.midlet.MIDlet import MIDlet
        from org.allbinary.AppletUtil import AppletUtil
        from org.allbinary.J2MEUtil import J2MEUtil
        from org.allbinary.canvas.Processor import Processor
        if AppletUtil.isAppletLoader(midlet) or J2MEUtil.isJ2ME():
            return Processor.getInstance()
        else:
            return MidletExitProcessor(midlet)
# from javax.microedition.midlet.MIDlet import MIDlet
# from org.allbinary.AppletUtil import AppletUtil
# from org.allbinary.J2MEUtil import J2MEUtil
# from org.allbinary.canvas.Processor import Processor


def _MidletExitProcessorFactory_instance() -> object:
    return MidletExitProcessorFactory()

lazy_static(MidletExitProcessorFactory, "instance", _MidletExitProcessorFactory_instance)

