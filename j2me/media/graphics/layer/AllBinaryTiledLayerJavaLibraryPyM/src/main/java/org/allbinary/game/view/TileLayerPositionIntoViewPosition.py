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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.view.ViewPosition import ViewPosition


@java_inherited_overloads
class TileLayerPositionIntoViewPosition(ViewPosition):
    def _java_defaults(self):
        vars(self).setdefault("tiledLayer", None)

    def _init_fields(self) -> None:
        from org.allbinary.layer.NullLayer import NullLayer
        self.tiledLayer: Layer = NullLayer.getInstance()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__(0, 0, 0)
        __class__._init_fields(self)
    

    def getX(self) -> int:
        return java_super_call(super(), "getX") - self.tiledLayer.getXP()
    

    def getY(self) -> int:
        return java_super_call(super(), "getY") - self.tiledLayer.getYP()
    

    def getZ(self) -> int:
        return java_super_call(super(), "getZ") - self.tiledLayer.getZP()
    

    def setTiledLayer(self, tiledLayer: AllBinaryTiledLayer) -> None:
        from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
        self.tiledLayer = tiledLayer
# from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
# from org.allbinary.layer.Layer import Layer
# from org.allbinary.layer.NullLayer import NullLayer


