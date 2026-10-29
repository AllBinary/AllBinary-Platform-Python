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



# Java interface
class MidletCompositeInterface:
    

    def setMidlet(self, midlet: MIDlet) -> None:
        raise NotImplementedError()
    

    def getMidlet(self) -> AllBinaryMidlet:
        raise NotImplementedError()
    

    def getDisplayable(self) -> Displayable:
        raise NotImplementedError()
# from javax.microedition.lcdui.Displayable import Displayable
# from javax.microedition.midlet.MIDlet import MIDlet


