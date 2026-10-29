# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.graphics.paint.InitUpdatePaintable import InitUpdatePaintable


class RTSLayerInfoPaintable(InitUpdatePaintable):

    def _init_fields(self) -> None:
        self.initUpdatePaintable: InitUpdatePaintable = NullInitUpdatePaintable.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def update(self) -> None:
        self.initUpdatePaintable.update()
    

    def paint(self, graphics: Graphics) -> None:
        self.initUpdatePaintable.paint(graphics)
    

    def updateRTSLayerInfoInit(self, hudPaintable: InitUpdatePaintable) -> None:
        self.initUpdatePaintable = hudPaintable
    

    def updateRTSLayerInfoSelection(self, hudPaintable: SelectionHudPaintable) -> None:
        hudPaintable.updateSelectionInfo()
        self.initUpdatePaintable = hudPaintable
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.paint.NullInitUpdatePaintable import NullInitUpdatePaintable


