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
# package org.allbinary.business.context.modules.storefront.statistics

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class RealTimeStoreFrontStatisticsView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.storeFrontStatisticsInterface: StoreFrontStatisticsInterface = None
        self.userRole: UserRole = None
    

    def __init__(self, storeFrontStatisticsInterface: StoreFrontStatisticsInterface, userRole: UserRole) -> None:
        self._init_fields()
        self.storeFrontStatisticsInterface = storeFrontStatisticsInterface
        self.userRole = userRole
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.context.modules.storefront.statistics.StoreFrontStatisticsData import StoreFrontStatisticsData
        node: Node = document.createElement(StoreFrontStatisticsData.getInstance().NAME)
        storeFrontAdvertisementsStatisticsInterface: StoreFrontAdvertisementsStatisticsInterface = self.storeFrontStatisticsInterface.getAdvertisements()
        storeFrontAdvertisementsStatisticsDomNodeInterface: DomNodeInterface = StoreFrontAdvertisementsStatisticsView(storeFrontAdvertisementsStatisticsInterface)
        node.appendChild(storeFrontAdvertisementsStatisticsDomNodeInterface.toXmlNode(document))
        storeFrontInventoryStatisticsInterface: StoreFrontInventoryStatisticsInterface = self.storeFrontStatisticsInterface.getInventory()
        storeFrontInventoryStatisticsDomNodeInterface: DomNodeInterface = StoreFrontInventoryStatisticsView(storeFrontInventoryStatisticsInterface)
        node.appendChild(storeFrontInventoryStatisticsDomNodeInterface.toXmlNode(document))
        storeFrontOrdersHistoryStatisticsInterface: StoreFrontOrdersHistoryStatisticsInterface = self.storeFrontStatisticsInterface.getOrders()
        storeFrontOrdersHistoryStatisticsDomNodeInterface: DomNodeInterface = StoreFrontOrdersHistoryStatisticsView(storeFrontOrdersHistoryStatisticsInterface)
        node.appendChild(storeFrontOrdersHistoryStatisticsDomNodeInterface.toXmlNode(document))
        if self.userRole == UserRoleFactory.getInstance().ADMINISTRATOR:
            storeFrontUsersStatisticsInterface: StoreFrontUsersStatisticsInterface = self.storeFrontStatisticsInterface.getUsers()
            storeFrontUsersStatisticsDomNodeInterface: DomNodeInterface = StoreFrontUsersStatisticsView(storeFrontUsersStatisticsInterface)
            node.appendChild(storeFrontUsersStatisticsDomNodeInterface.toXmlNode(document))
        return node
from org.allbinary.business.context.modules.storefront.statistics.advertisements.StoreFrontAdvertisementsStatisticsInterface import StoreFrontAdvertisementsStatisticsInterface
from org.allbinary.business.context.modules.storefront.statistics.advertisements.StoreFrontAdvertisementsStatisticsView import StoreFrontAdvertisementsStatisticsView
from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatisticsInterface import StoreFrontInventoryStatisticsInterface
from org.allbinary.business.context.modules.storefront.statistics.inventory.StoreFrontInventoryStatisticsView import StoreFrontInventoryStatisticsView
from org.allbinary.business.context.modules.storefront.statistics.orders.history.StoreFrontOrdersHistoryStatisticsInterface import StoreFrontOrdersHistoryStatisticsInterface
from org.allbinary.business.context.modules.storefront.statistics.orders.history.StoreFrontOrdersHistoryStatisticsView import StoreFrontOrdersHistoryStatisticsView
from org.allbinary.business.context.modules.storefront.statistics.users.StoreFrontUsersStatisticsInterface import StoreFrontUsersStatisticsInterface
from org.allbinary.business.context.modules.storefront.statistics.users.StoreFrontUsersStatisticsView import StoreFrontUsersStatisticsView
from org.allbinary.business.user.role.UserRole import UserRole
from org.allbinary.business.user.role.UserRoleFactory import UserRoleFactory
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


