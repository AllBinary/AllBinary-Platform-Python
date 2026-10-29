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



class GraphicItemBuilder:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(node: Node) -> GraphicItemInterface:
        from org.allbinary.graphics.j2me.workarea.tools.PointsDomUtil import PointsDomUtil
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
        graphicItemName: str = node.getNodeName()
        if ((graphicItemName > PointsDomUtil.getInstance().LINES) - (graphicItemName < PointsDomUtil.getInstance().LINES)) == 0:
            return LinesGraphicItem(node)
        else:
            raise Exception("Graphic Item Does Not Exist: " + graphicItemName)
from org.w3c.dom.Node import Node


