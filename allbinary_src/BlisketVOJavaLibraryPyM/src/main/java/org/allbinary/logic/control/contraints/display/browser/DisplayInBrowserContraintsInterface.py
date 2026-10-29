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
# package org.allbinary.logic.control.contraints.display.browser

from __future__ import annotations



# Java interface
class DisplayInBrowserContraintsInterface:
    

    def isMountable(self) -> bool:
        raise NotImplementedError()
    

    def isFrameable(self) -> bool:
        raise NotImplementedError()
    

    def isQuickFrameable(self) -> bool:
        raise NotImplementedError()
    

    def setMountable(self, canBeMounted: bool) -> None:
        raise NotImplementedError()
    

    def setFrameable(self, canBeFramed: bool) -> None:
        raise NotImplementedError()
    

    def setQuickFrameable(self, canBeQuickFramed: bool) -> None:
        raise NotImplementedError()
    

    def setMountedLink(self, mountedLink: str) -> None:
        raise NotImplementedError()
    

    def getMountedLink(self) -> str:
        raise NotImplementedError()


