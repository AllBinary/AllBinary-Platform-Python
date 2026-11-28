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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.paint.InitUpdatePaintable import InitUpdatePaintable


@java_inherited_overloads
class RTSLayerInfoPaintable(InitUpdatePaintable):
    def _java_defaults(self):
        vars(self).setdefault("initUpdatePaintable", None)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.paint.NullInitUpdatePaintable import NullInitUpdatePaintable
        self.initUpdatePaintable: InitUpdatePaintable = NullInitUpdatePaintable.getInstance()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def update(self) -> None:
        self.initUpdatePaintable.update()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.initUpdatePaintable.paint(graphics)
    

    def updateRTSLayerInfoInit(self, hudPaintable: InitUpdatePaintable) -> None:
        self.initUpdatePaintable = hudPaintable
    

    def updateRTSLayerInfoSelection(self, hudPaintable: SelectionHudPaintable) -> None:
        hudPaintable.updateSelectionInfo()
        self.initUpdatePaintable = hudPaintable
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.paint.NullInitUpdatePaintable import NullInitUpdatePaintable


