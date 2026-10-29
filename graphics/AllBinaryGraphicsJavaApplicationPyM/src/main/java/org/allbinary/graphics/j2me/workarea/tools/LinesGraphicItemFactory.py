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
# package org.allbinary.graphics.j2me.workarea.tools

from __future__ import annotations

from org.allbinary.graphics.j2me.workarea.tools.GraphicsItemInterfaceFactoryInterface import GraphicsItemInterfaceFactoryInterface


class LinesGraphicItemFactory(GraphicsItemInterfaceFactoryInterface):
    

    def getInstance(self, canvasJPanel: CanvasJPanel) -> GraphicItemInterface:
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
        return LinesGraphicItem()
from org.allbinary.graphics.j2me.workarea.canvas.CanvasJPanel import CanvasJPanel


