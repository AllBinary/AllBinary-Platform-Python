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



# Java interface
class FullScreenInterface:
    

    def isFullScreenMode(self) -> bool:
        raise NotImplementedError()
    

    def setFullScreenMode(self, mode: bool) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def stopWaiting(self) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def waitOnNotify(self, wait: int) -> None:
        raise NotImplementedError()


