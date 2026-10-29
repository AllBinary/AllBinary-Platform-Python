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
# package views.admin.orderhistory

from __future__ import annotations

import datetime
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class DateRangeOrderHistoryView(HttpStoreComponentView, ValidationComponentInterface, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.VIEWALLORDERS: str = "View All"
        self.VIEWORDERSINLASTHOUR: str = "Last Hour"
        self.VIEWORDERSINLASTDAY: str = "Last Day"
        self.VIEWORDERSINLASTWEEK: str = "Last Week"
        self.VIEWORDERSINLAST30DAYS: str = "30 Days"
        self.request: HttpServletRequest = None
        self.shipped: str = None
        self.partiallyShipped: str = None
        self.processing: str = None
        self.preprocessing: str = None
        self.cancelled: str = None
        self.dateType: str = None
        self.toDate: str = None
        self.fromDate: str = None
        self.fromYear: str = None
        self.fromMonth: str = None
        self.fromDay: str = None
        self.fromHour: str = None
        self.toYear: str = None
        self.toMonth: str = None
        self.toDay: str = None
        self.toHour: str = None
        self.command: str = None
        self.ON: str = "on"
        self.MAXLEN: int = 15
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.request = self.getPageContext().getRequest()
        self.getFormData()
    

    def getFormData(self) -> None:
        self.dateType = self.request.getParameter(OrderHistoryData.DATETYPE)
        self.preprocessing = self.request.getParameter(OrderHistoryData.PREPROCESSINGNAME)
        self.shipped = self.request.getParameter(OrderHistoryData.SHIPPEDNAME)
        self.partiallyShipped = self.request.getParameter(OrderHistoryData.PARTIALLYSHIPPEDNAME)
        self.processing = self.request.getParameter(OrderHistoryData.PROCESSINGNAME)
        self.cancelled = self.request.getParameter(OrderHistoryData.CANCELLEDNAME)
        self.fromYear = self.request.getParameter(OrderHistoryData.FROMYEAR)
        self.fromMonth = self.request.getParameter(OrderHistoryData.FROMMONTH)
        self.fromDay = self.request.getParameter(OrderHistoryData.FROMDAY)
        self.fromHour = self.request.getParameter(OrderHistoryData.FROMHOUR)
        self.toYear = self.request.getParameter(OrderHistoryData.TOYEAR)
        self.toMonth = self.request.getParameter(OrderHistoryData.TOMONTH)
        self.toDay = self.request.getParameter(OrderHistoryData.TODAY)
        self.toHour = self.request.getParameter(OrderHistoryData.TOHOUR)
        self.command = self.request.getParameter(self.GLOBALS2.ADMINCOMMAND)
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    # throws Exception
    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
    

    def toXmlNode(self, document: Document) -> Node:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Attempt to View orders in (fromDate=")
                stringBuffer.append(self.fromDate)
                stringBuffer.append(",toDate=")
                stringBuffer.append(self.toDate)
                stringBuffer.append(") and status")
                self.logUtil.putF(str(stringBuffer), self, "view")
            node: Node = document.createElement(OrderData.ORDERS)
            if self.preprocessing is not None and ((self.preprocessing > self.ON) - (self.preprocessing < self.ON)) == 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Adding Preprocessing Orders", self, "toXmlNode")
                orderHistoryVector: BasicArrayList = OrderHistoryEntityFactory.getInstance().getOrders(OrderHistoryData.PREPROCESSING, self.fromDate, self.toDate)
                size: int = orderHistoryVector.size()
                for index in range(0, size):
                    orderHistory: OrderHistory = orderHistoryVector.get(index)
                    node.appendChild(orderHistory.toXmlNode(document))
            if self.shipped is not None and ((self.shipped > self.ON) - (self.shipped < self.ON)) == 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Adding Shipped Orders", self, "toXmlNode")
                orderHistoryVector: BasicArrayList = OrderHistoryEntityFactory.getInstance().getOrders(OrderHistoryData.SHIPPED, self.fromDate, self.toDate)
                size: int = orderHistoryVector.size()
                for index in range(0, size):
                    orderHistory: OrderHistory = orderHistoryVector.get(index)
                    node.appendChild(orderHistory.toXmlNode(document))
            if self.partiallyShipped is not None and ((self.partiallyShipped > self.ON) - (self.partiallyShipped < self.ON)) == 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Adding Partially Shipped Orders", self, "toDomNode")
                orderHistoryVector: BasicArrayList = OrderHistoryEntityFactory.getInstance().getOrders(OrderHistoryData.PARTIALLYSHIPPED, self.fromDate, self.toDate)
                size: int = orderHistoryVector.size()
                for index in range(0, size):
                    orderHistory: OrderHistory = orderHistoryVector.get(index)
                    node.appendChild(orderHistory.toXmlNode(document))
            if self.processing is not None and ((self.processing > self.ON) - (self.processing < self.ON)) == 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Adding Processing Orders", self, "toXmlNode")
                orderHistoryVector: BasicArrayList = OrderHistoryEntityFactory.getInstance().getOrders(OrderHistoryData.PROCESSING, self.fromDate, self.toDate)
                size: int = orderHistoryVector.size()
                for index in range(0, size):
                    orderHistory: OrderHistory = orderHistoryVector.get(index)
                    node.appendChild(orderHistory.toXmlNode(document))
            if self.cancelled is not None and ((self.cancelled > self.ON) - (self.cancelled < self.ON)) == 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Adding Cancelled Orders", self, "view")
                orderHistoryVector: BasicArrayList = OrderHistoryEntityFactory.getInstance().getOrders(OrderHistoryData.CANCELLED, self.fromDate, self.toDate)
                size: int = orderHistoryVector.size()
                for index in range(0, size):
                    orderHistory: OrderHistory = orderHistoryVector.get(index)
                    node.appendChild(orderHistory.toXmlNode(document))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.PREPROCESSINGNAME, OrderHistoryData.PREPROCESSING))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.PROCESSINGNAME, OrderHistoryData.PROCESSING))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.CANCELLEDNAME, OrderHistoryData.CANCELLED))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.PARTIALLYSHIPPEDNAME, OrderHistoryData.PARTIALLYSHIPPED))
            node.appendChild(ModDomHelper.createNameValueNodes(document, OrderHistoryData.SHIPPEDNAME, OrderHistoryData.SHIPPED))
            node.appendChild(ModDomHelper.createNameValueNodes(document, self.GLOBALS2.VIEWNAME, self.GLOBALS2.VIEW))
            return node
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            return None
    

    def isValid(self) -> bool:
        try:
            isValid: bool = True
            if self.dateType is None or (((self.dateType > OrderHistoryData.TYPELONG) - (self.dateType < OrderHistoryData.TYPELONG)) != 0 and ((self.dateType > OrderHistoryData.TYPECAESAR) - (self.dateType < OrderHistoryData.TYPECAESAR)) != 0):
                isValid = False
            if self.dateType is not None:
                if ((self.dateType > OrderHistoryData.TYPELONG) - (self.dateType < OrderHistoryData.TYPELONG)) == 0:
                    calendar: datetime.datetime = datetime.datetime.now()
                    currentTime: int = calendar.getTimeInMillis()
                    rangeDate: str = StringUtil.getInstance().EMPTY_STRING
                    if ((self.command > self.VIEWORDERSINLASTHOUR) - (self.command < self.VIEWORDERSINLASTHOUR)) == 0:
                        oneHour: int = 60 * 60 * 1000
                        rangeDate = str(int(oneHour))
                    elif ((self.command > self.VIEWORDERSINLASTDAY) - (self.command < self.VIEWORDERSINLASTDAY)) == 0:
                        oneDay: int = 24 * 60 * 60 * 1000
                        rangeDate = str(int(oneDay))
                    elif ((self.command > self.VIEWORDERSINLASTWEEK) - (self.command < self.VIEWORDERSINLASTWEEK)) == 0:
                        oneWeek: int = 7 * 24 * 60 * 60 * 1000
                        rangeDate = str(int(oneWeek))
                    elif ((self.command > self.VIEWORDERSINLAST30DAYS) - (self.command < self.VIEWORDERSINLAST30DAYS)) == 0:
                        thirtyDays: int = 30 * 24 * 60 * 60 * 1000
                        rangeDate = str(int(thirtyDays))
                    elif ((self.command > self.VIEWALLORDERS) - (self.command < self.VIEWALLORDERS)) == 0:
                        rangeDate = str(int(currentTime))
                    rangeDateLong: int = int(int(rangeDate))
                    self.fromDate = str(int(currentTime - rangeDateLong))
                    time: str = str(str(int(currentTime)))
                    self.toDate = time
                elif ((self.dateType > OrderHistoryData.TYPECAESAR) - (self.dateType < OrderHistoryData.TYPECAESAR)) == 0:
                    calendar: datetime.datetime = datetime.datetime.now()
                    TimeUtil.getInstance().setCalendar(calendar, self.fromYear, self.fromMonth, self.fromDay, self.fromHour)
                    self.fromDate = str(int(calendar.getTimeInMillis()))
                    TimeUtil.getInstance().setCalendar(calendar, self.toYear, self.toMonth, self.toDay, self.toHour)
                    self.toDate = str(int(calendar.getTimeInMillis()))
                if StringValidationUtil.getInstance().isEmpty(self.toDate) or len(self.toDate) > self.MAXLEN:
                    isValid = False
                if StringValidationUtil.getInstance().isEmpty(self.fromDate) or len(self.fromDate) > self.MAXLEN:
                    isValid = False
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Attempt to View orders in (fromDate=")
                stringBuffer.append(self.fromDate)
                stringBuffer.append(",toDate=")
                stringBuffer.append(self.toDate)
                stringBuffer.append(")")
                self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
            return isValid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.put("Exception in validation", self, self.commonStrings.IS_VALID, e)
            return False
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def validationInfo(self) -> str:
        try:
            result: StringMaker = StringMaker()
            if self.dateType is None or (((self.dateType > OrderHistoryData.TYPELONG) - (self.dateType < OrderHistoryData.TYPELONG)) != 0 and ((self.dateType > OrderHistoryData.TYPECAESAR) - (self.dateType < OrderHistoryData.TYPECAESAR)) != 0):
                result.append("DATETYPE not recognized")
            if StringValidationUtil.getInstance().isEmpty(self.toDate) or len(self.toDate) > self.MAXLEN:
                result.append("Invalid To Date")
            if StringValidationUtil.getInstance().isEmpty(self.fromDate) or len(self.fromDate) > self.MAXLEN:
                result.append("Invalid From Date")
            return str(result)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Getting Validation Info"
# from java.util.Calendar import Calendar
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.globals.GLOBALS2 import GLOBALS2
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.time.TimeUtil import TimeUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


