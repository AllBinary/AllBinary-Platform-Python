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



class GraphicItemFactory:
    instance: GraphicItemFactory = None

    def _init_fields(self) -> None:
        self.graphicItems: dict = None
        self.DEFAULT: GraphicsItemInterfaceFactoryInterface = SelectionToolFactory()
    

    @staticmethod
    def getInstance() -> GraphicItemFactory:
        return GraphicItemFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItemFactory import LinesGraphicItemFactory
        self._init_fields()
        self.graphicItems = StdUtil.getInstance().createHashMap()
        self.graphicItems.put(LinesGraphicItem.getStaticName(), LinesGraphicItemFactory())
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, itemName: str) -> GraphicsItemInterfaceFactoryInterface:
        graphicsItemInterfaceFactoryInterface: GraphicsItemInterfaceFactoryInterface = self.graphicItems.get(itemName)
        if graphicsItemInterfaceFactoryInterface is None:
            graphicsItemInterfaceFactoryInterface = self.DEFAULT
        return graphicsItemInterfaceFactoryInterface
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, graphicItemNodeList: BasicArrayList) -> dict:
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemBuilder import GraphicItemBuilder
        numberOfItems: int = graphicItemNodeList.size()
        graphicItemHashMap: dict = StdUtil.getInstance().createHashMap()
        if self.LOGGING.contains(self.LOGGING.MENUEVENT):
            pass
        for index in range(0, numberOfItems):
            graphicItem: GraphicItemInterface = GraphicItemBuilder.getInstance(graphicItemNodeList.get(index))
            graphicItemHashMap.put(graphicItem.getTreeNode(), graphicItem)
        return graphicItemHashMap
# from java.util.HashMap import HashMap
from org.allbinary.log.LOGGING import LOGGING
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.w3c.dom.Node import Node
from org.allbinary.graphics.j2me.workarea.tools.SelectionToolFactory import SelectionToolFactory


GraphicItemFactory.instance = GraphicItemFactory()

