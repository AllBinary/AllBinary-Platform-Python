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
# package org.allbinary.business.user.commerce.inventory.item.download

from __future__ import annotations

import datetime
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class DownloadableItemView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.downloadableItem: DownloadableItem = None
    

    def __init__(self, downloadableItem: DownloadableItem) -> None:
        self._init_fields()
        self.downloadableItem = downloadableItem
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGING):
            self.logUtil.putF(self.commonStrings.START, self, "toXmlNode")
        hashMap: dict = self.downloadableItem.toHashMap()
        totalTime: int = int(self.downloadableItem.getValidTime())
        calendar: datetime.datetime = datetime.datetime.now()
        year: int = calendar.get(Calendar.YEAR)
        month: int = calendar.get(Calendar.MONTH)
        day: int = calendar.get(Calendar.DAY_OF_MONTH)
        hour: int = calendar.get(Calendar.HOUR)
        minute: int = calendar.get(Calendar.MINUTE)
        second: int = calendar.get(Calendar.SECOND)
        calendar.setTimeInMillis(calendar.getTimeInMillis() + totalTime)
        yearDelta: int = calendar.get(Calendar.YEAR)
        monthDelta: int = calendar.get(Calendar.MONTH)
        dayDelta: int = calendar.get(Calendar.DAY_OF_MONTH)
        hourDelta: int = calendar.get(Calendar.HOUR)
        minuteDelta: int = calendar.get(Calendar.MINUTE)
        secondDelta: int = calendar.get(Calendar.SECOND)
        hashMap.put(DownloadItemData.VALID_TIME_YEARS, str(yearDelta - year))
        hashMap.put(DownloadItemData.VALID_TIME_MONTHS, str(monthDelta - month))
        hashMap.put(DownloadItemData.VALID_TIME_DAYS, str(dayDelta - day))
        hashMap.put(DownloadItemData.VALID_TIME_HOURS, str(hourDelta - hour))
        hashMap.put(DownloadItemData.VALID_TIME_MINUTES, str(minuteDelta - minute))
        hashMap.put(DownloadItemData.VALID_TIME_SECONDS, str(secondDelta - second))
        keySet: Set = hashMap.keySet()
        node: Node = document.createElement(DownloadItemData.NAME)
        stringUtil: StringUtil = StringUtil.getInstance()
        nameArray: list[object] = keySet.toArray()
        size: int = len(nameArray)
        for index in range(0, size):
            name: str = nameArray[index]
            value: str = hashMap.get(name)
            value = stringUtil.getNonNull(value)
            node.appendChild(ModDomHelper.createNameValueNodes(document, name, value))
        return node
    

    def toXmlDoc(self) -> Document:
        return None
    

    def view(self) -> str:
        return None
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


