# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.view

from __future__ import annotations

from org.allbinary.view.ViewPositionFactoryInterface import ViewPositionFactoryInterface


class StaticTileLayerViewPositionFactory(ViewPositionFactoryInterface):
    

    # throws Exception
    def getInstance(self) -> ViewPositionBase:
        from org.allbinary.game.view.StaticTileLayerIntoPositionViewPosition import StaticTileLayerIntoPositionViewPosition
        return StaticTileLayerIntoPositionViewPosition()
from org.allbinary.view.ViewPositionBase import ViewPositionBase


