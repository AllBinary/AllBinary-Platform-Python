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
# package org.allbinary.business.context.modules.storefront

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class StoreFrontView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.storeFrontInterface: StoreFrontInterface = None
    

    def __init__(self, storeFrontInterface: StoreFrontInterface) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF("Constructing: StoreFrontView for: " + storeFrontInterface.getName(), self, commonStrings.GET_INSTANCE)
        self.storeFrontInterface = storeFrontInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        hashMap: dict = self.storeFrontInterface.toHashMap()
        storeFrontData: StoreFrontData = StoreFrontData.getInstance()
        hashMap.put(storeFrontData.CURRENTHOMEHOSTNAME, self.storeFrontInterface.getCurrentHomeHostName())
        hashMap.put(storeFrontData.CURRENTHOMEHOSTNAMEPATH, self.storeFrontInterface.getCurrentHomeHostNamePath())
        hashMap.put(storeFrontData.CURRENTHOSTNAME, self.storeFrontInterface.getCurrentHostName())
        hashMap.put(storeFrontData.CURRENTHOSTNAMEPATH, self.storeFrontInterface.getCurrentHostNamePath())
        hashMap.put(BasketData.NAME, self.storeFrontInterface.getBasketName())
        node: Node = ModDomHelper.createNameValueNodes(document, storeFrontData.NAME, hashMap)
        return node
# from java.util.HashMap import HashMap
from org.allbinary.business.user.commerce.inventory.basket.BasketData import BasketData
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


