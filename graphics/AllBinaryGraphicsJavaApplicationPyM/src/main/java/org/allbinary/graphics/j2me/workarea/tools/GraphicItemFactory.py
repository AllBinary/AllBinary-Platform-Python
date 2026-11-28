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
        if "graphicItems" not in vars(self): self.graphicItems: HashMap = None
        self.DEFAULT: GraphicsItemInterfaceFactoryInterface = SelectionToolFactory()
    

    @staticmethod
    def getInstance_j0() -> GraphicItemFactory:
        return GraphicItemFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItem import LinesGraphicItem
        from org.allbinary.graphics.j2me.workarea.tools.LinesGraphicItemFactory import LinesGraphicItemFactory
        from org.allbinary.logic.StdUtil import StdUtil
        __class__._init_fields(self)
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

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        if len(args) == 1 and True and (args[0] is None or isinstance(args[0], str)):
            return __class__.__dict__["getInstance_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["getInstance_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.log.LOGGING import LOGGING
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.w3c.dom.Node import Node
from org.allbinary.graphics.j2me.workarea.tools.SelectionToolFactory import SelectionToolFactory


def _GraphicItemFactory_instance() -> object:
    return GraphicItemFactory()

lazy_static(GraphicItemFactory, "instance", _GraphicItemFactory_instance)

