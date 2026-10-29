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

from org.allbinary.view.EmulatorViewInterface import EmulatorViewInterface


class NullEmulatorView(EmulatorViewInterface):
    NULL_EMULATOR_VIEW: NullEmulatorView = None
    

    def setMidlet(self, midlet: MIDlet) -> None:
        pass
    

    def onEmulatorInitComplete(self, midletActivity: object) -> None:
        pass
    

    def onSetDisplayable(self, displayable: Displayable) -> None:
        pass
# from javax.microedition.lcdui.Displayable import Displayable
# from javax.microedition.midlet.MIDlet import MIDlet


NullEmulatorView.NULL_EMULATOR_VIEW = NullEmulatorView()

