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

from java.lang.JavaRuntimeStatic import lazy_static


class GraphicItemFactory:
    instance: GraphicItemFactory = None

    def _init_fields(self) -> None:
        from java.util.HashMap import HashMap
        self.graphicItems: HashMap = None
        self.DEFAULT: GraphicsItemInterfaceFactoryInterface = SelectionToolFactory()
    

    @staticmethod
    def getInstance_j0() -> GraphicItemFactory:
        return GraphicItemFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItemFactory import LinesGraphicItemFactory
        from org.allbinary.logic.StdUtil import StdUtil
        self._init_fields()
        self.graphicItems = StdUtil.getInstance().createHashMap()
        self.graphicItems.put(LinesGraphicItem.getStaticName(), LinesGraphicItemFactory())
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j1_1(self, itemName: str) -> GraphicsItemInterfaceFactoryInterface:
        graphicsItemInterfaceFactoryInterface: GraphicsItemInterfaceFactoryInterface = self.graphicItems.get(itemName)
        if graphicsItemInterfaceFactoryInterface is None:
            graphicsItemInterfaceFactoryInterface = self.DEFAULT
        return graphicsItemInterfaceFactoryInterface
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j1_2(self, graphicItemNodeList: BasicArrayList) -> HashMap:
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemBuilder import GraphicItemBuilder
        from java.util.HashMap import HashMap
        from org.allbinary.log.LOGGING import LOGGING
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.w3c.dom.Node import Node
        numberOfItems: int = graphicItemNodeList.size()
        graphicItemHashMap: HashMap = StdUtil.getInstance().createHashMap()
        if LOGGING.contains(LOGGING.MENUEVENT):
            pass
        for index in range(0, numberOfItems):
            graphicItem: GraphicItemInterface = GraphicItemBuilder.getInstance(graphicItemNodeList.get(index))
            graphicItemHashMap.put(graphicItem.getTreeNode(), graphicItem)
        return graphicItemHashMap

    def getInstance(self, *args):
        if len(args) == 1 and True and (args[0] is None or isinstance(args[0], str)):
            return self.getInstance_j1_1(*args)
        if len(args) == 1:
            return self.getInstance_j1_2(*args)
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.log.LOGGING import LOGGING
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.w3c.dom.Node import Node
from org.allbinary.graphics.j2me.workarea.tools.SelectionToolFactory import SelectionToolFactory


def _GraphicItemFactory_instance() -> object:
    return GraphicItemFactory()

lazy_static(GraphicItemFactory, "instance", _GraphicItemFactory_instance)

