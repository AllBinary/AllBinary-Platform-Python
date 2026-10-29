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
# package org.allbinary.bounds

from __future__ import annotations



# Java interface
class BoundsVisitorInterface:
    

    def getX(self) -> int:
        raise NotImplementedError()
    

    def getY(self) -> int:
        raise NotImplementedError()
    

    def maxX(self) -> None:
        raise NotImplementedError()
    

    def maxY(self) -> None:
        raise NotImplementedError()
    

    def minX(self) -> None:
        raise NotImplementedError()
    

    def minY(self) -> None:
        raise NotImplementedError()


