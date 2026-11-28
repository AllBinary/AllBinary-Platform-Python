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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import datetime
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


@java_inherited_overloads
class DateRangeOrderHistoryView(*java_bases(HttpStoreComponentView, ValidationComponentInterface, DomNodeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("VIEWALLORDERS", None)
        vars(self).setdefault("VIEWORDERSINLASTHOUR", None)
        vars(self).setdefault("VIEWORDERSINLASTDAY", None)
        vars(self).setdefault("VIEWORDERSINLASTWEEK", None)
        vars(self).setdefault("VIEWORDERSINLAST30DAYS", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("shipped", None)
        vars(self).setdefault("partiallyShipped", None)
        vars(self).setdefault("processing", None)
        vars(self).setdefault("preprocessing", None)
        vars(self).setdefault("cancelled", None)
        vars(self).setdefault("dateType", None)
        vars(self).setdefault("toDate", None)
        vars(self).setdefault("fromDate", None)
        vars(self).setdefault("fromYear", None)
        vars(self).setdefault("fromMonth", None)
        vars(self).setdefault("fromDay", None)
        vars(self).setdefault("fromHour", None)
        vars(self).setdefault("toYear", None)
        vars(self).setdefault("toMonth", None)
        vars(self).setdefault("toDay", None)
        vars(self).setdefault("toHour", None)
        vars(self).setdefault("command", None)
        vars(self).setdefault("ON", None)
        vars(self).setdefault("MAXLEN", 0)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.VIEWALLORDERS: str = "View All"
        self.VIEWORDERSINLASTHOUR: str = "Last Hour"
        self.VIEWORDERSINLASTDAY: str = "Last Day"
        self.VIEWORDERSINLASTWEEK: str = "Last Week"
        self.VIEWORDERSINLAST30DAYS: str = "30 Days"
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "shipped" not in vars(self): self.shipped: str = None
        if "partiallyShipped" not in vars(self): self.partiallyShipped: str = None
        if "processing" not in vars(self): self.processing: str = None
        if "preprocessing" not in vars(self): self.preprocessing: str = None
        if "cancelled" not in vars(self): self.cancelled: str = None
        if "dateType" not in vars(self): self.dateType: str = None
        if "toDate" not in vars(self): self.toDate: str = None
        if "fromDate" not in vars(self): self.fromDate: str = None
        if "fromYear" not in vars(self): self.fromYear: str = None
        if "fromMonth" not in vars(self): self.fromMonth: str = None
        if "fromDay" not in vars(self): self.fromDay: str = None
        if "fromHour" not in vars(self): self.fromHour: str = None
        if "toYear" not in vars(self): self.toYear: str = None
        if "toMonth" not in vars(self): self.toMonth: str = None
        if "toDay" not in vars(self): self.toDay: str = None
        if "toHour" not in vars(self): self.toHour: str = None
        if "command" not in vars(self): self.command: str = None
        self.ON: str = "on"
        self.MAXLEN: int = 15
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        __class__._init_fields(self)
        self.request = self.getPageContext().getRequest()
        self.getFormData()
    

    def getFormData(self) -> None:
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
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
        self.command = self.request.getParameter(GLOBALS2.ADMINCOMMAND)
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    # throws Exception
    def view(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            self.addDomNodeInterfaces()
            return java_super_call(super(), "view")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
    

    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
        from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Attempt to View orders in (fromDate=")
                stringBuffer.append(self.fromDate)
                stringBuffer.append(",toDate=")
                stringBuffer.append(self.toDate)
                stringBuffer.append(") and status")
                self.logUtil.putF(str(stringBuffer), self, "view")
            node: Node = document.createElement(OrderData.ORDERS)
            if self.preprocessing is not None and ((self.preprocessing > self.ON) - (self.preprocessing < self.ON)) == 0:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Adding Preprocessing Orders", self, "toXmlNode")
                orderHistoryVector: BasicArrayList = OrderHistoryEntityFactory.getInstance().getOrders(OrderHistoryData.PREPROCESSING, self.fromDate, self.toDate)
                size: int = orderHistoryVector.size()
                for index in range(0, size):
                    orderHistory: OrderHistory = orderHistoryVector.get(index)
                    node.appendChild(orderHistory.toXmlNode(document))
            if self.shipped is not None and ((self.shipped > self.ON) - (self.shipped < self.ON)) == 0:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Adding Shipped Orders", self, "toXmlNode")
                orderHistoryVector: BasicArrayList = OrderHistoryEntityFactory.getInstance().getOrders(OrderHistoryData.SHIPPED, self.fromDate, self.toDate)
                size: int = orderHistoryVector.size()
                for index in range(0, size):
                    orderHistory: OrderHistory = orderHistoryVector.get(index)
                    node.appendChild(orderHistory.toXmlNode(document))
            if self.partiallyShipped is not None and ((self.partiallyShipped > self.ON) - (self.partiallyShipped < self.ON)) == 0:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Adding Partially Shipped Orders", self, "toDomNode")
                orderHistoryVector: BasicArrayList = OrderHistoryEntityFactory.getInstance().getOrders(OrderHistoryData.PARTIALLYSHIPPED, self.fromDate, self.toDate)
                size: int = orderHistoryVector.size()
                for index in range(0, size):
                    orderHistory: OrderHistory = orderHistoryVector.get(index)
                    node.appendChild(orderHistory.toXmlNode(document))
            if self.processing is not None and ((self.processing > self.ON) - (self.processing < self.ON)) == 0:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Adding Processing Orders", self, "toXmlNode")
                orderHistoryVector: BasicArrayList = OrderHistoryEntityFactory.getInstance().getOrders(OrderHistoryData.PROCESSING, self.fromDate, self.toDate)
                size: int = orderHistoryVector.size()
                for index in range(0, size):
                    orderHistory: OrderHistory = orderHistoryVector.get(index)
                    node.appendChild(orderHistory.toXmlNode(document))
            if self.cancelled is not None and ((self.cancelled > self.ON) - (self.cancelled < self.ON)) == 0:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
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
            node.appendChild(ModDomHelper.createNameValueNodes(document, GLOBALS2.VIEWNAME, GLOBALS2.VIEW))
            return node
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            return None
    

    def isValid(self) -> bool:
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.time.TimeUtil import TimeUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Attempt to View orders in (fromDate=")
                stringBuffer.append(self.fromDate)
                stringBuffer.append(",toDate=")
                stringBuffer.append(self.toDate)
                stringBuffer.append(")")
                self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
            return isValid
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.put("Exception in validation", self, self.commonStrings.IS_VALID, e)
            return False
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    # throws Exception
    def validationInfo(self) -> str:
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Getting Validation Info"
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return java_super_call(super(), "getTransformInfoInterface")
# from java.util.Calendar import Calendar
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.business.user.commerce.inventory.order.OrderData import OrderData
# from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
# from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
# from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.time.TimeUtil import TimeUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


