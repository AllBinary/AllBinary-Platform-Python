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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from org.allbinary.graphics.displayable.DisplayableInterface import DisplayableInterface


# Java interface
class AllBinaryGameCanvasInterface(DisplayableInterface):
    

    def getLayerManager(self) -> AllBinaryGameLayerManager:
        raise NotImplementedError()
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager


