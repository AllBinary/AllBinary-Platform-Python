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
# package org.allbinary.business.context.modules.storefront.statistics.inventory

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class StoreFrontInventoryStatisticsView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.storeFrontInventoryStatisticsInterface: StoreFrontInventoryStatisticsInterface = None
    

    def __init__(self, storeFrontInventoryStatisticsInterface: StoreFrontInventoryStatisticsInterface) -> None:
        self._init_fields()
        self.storeFrontInventoryStatisticsInterface = storeFrontInventoryStatisticsInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatisticsData import StoreFrontInventoryStatisticsData
        hashMap: dict = self.storeFrontInventoryStatisticsInterface.toHashMap()
        node: Node = ModDomHelper.createNameValueNodes(document, StoreFrontInventoryStatisticsData.getInstance().NAME, hashMap)
        return node
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


