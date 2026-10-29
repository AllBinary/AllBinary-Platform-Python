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
# package org.allbinary.graphics.displayable

from __future__ import annotations



# Java interface
class ScalableListener:
    

    def getRatio(self, ratio: float) -> float:
        raise NotImplementedError()
    

    def getLeft(self, xOffset: int) -> int:
        raise NotImplementedError()
    

    def getTop(self, yOffset: int) -> int:
        raise NotImplementedError()
    

    def scale(self, ratio: float) -> None:
        raise NotImplementedError()


