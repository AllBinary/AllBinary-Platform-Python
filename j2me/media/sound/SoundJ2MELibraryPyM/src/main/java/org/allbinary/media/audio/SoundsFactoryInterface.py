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
# package org.allbinary.media.audio

from __future__ import annotations



# Java interface
class SoundsFactoryInterface:
    

    def init(self) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def getSoundInterfaceArray(self) -> list[Sound]:
        raise NotImplementedError()
    

    def setInitialized(self, initialized: bool) -> None:
        raise NotImplementedError()
    

    def isInitialized(self) -> bool:
        raise NotImplementedError()


