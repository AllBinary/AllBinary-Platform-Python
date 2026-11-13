# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.view

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.view.EmulatorViewInterface import EmulatorViewInterface


class NullEmulatorView(EmulatorViewInterface):
    NULL_EMULATOR_VIEW: NullEmulatorView = None
    

    def setMidlet(self, midlet: MIDlet) -> None:
        from javax.microedition.midlet.MIDlet import MIDlet
        pass
    

    def onEmulatorInitComplete(self, midletActivity: object) -> None:
        pass
    

    def onSetDisplayable(self, displayable: Displayable) -> None:
        from javax.microedition.lcdui.Displayable import Displayable
        pass
# from javax.microedition.lcdui.Displayable import Displayable
# from javax.microedition.midlet.MIDlet import MIDlet


def _NullEmulatorView_NULL_EMULATOR_VIEW() -> object:
    return NullEmulatorView()

lazy_static(NullEmulatorView, "NULL_EMULATOR_VIEW", _NullEmulatorView_NULL_EMULATOR_VIEW)

