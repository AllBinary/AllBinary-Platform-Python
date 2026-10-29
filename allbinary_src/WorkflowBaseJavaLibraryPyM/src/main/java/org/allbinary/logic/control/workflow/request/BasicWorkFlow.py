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
# package org.allbinary.logic.control.workflow.request

from __future__ import annotations

import datetime


class BasicWorkFlow:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.workFlowDoc: Document = None
        self.workFlowName: str = None
        self.storeName: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.workFlowName = StringUtil.getInstance().EMPTY_STRING
        self.workFlowDoc = DomDocumentHelper.create()
        workFlowNode: Node = self.workFlowDoc.createElement(WorkFlowData.getInstance().WORKFLOW)
        self.workFlowDoc.appendChild(workFlowNode)
    

    def _constructor2(self, hashMap: dict, pageContext: PageContext) -> None:
        self._init_fields()
        weblisketSession: WeblisketSession = WeblisketSession(hashMap, pageContext)
        self.storeName = weblisketSession.getStoreName()
        requestHashMap: dict = RequestParams(pageContext).toHashMap()
        self.workFlowName = requestHashMap.get(WorkFlowData.getInstance().NAME)
        self.workFlowDoc = DomDocumentHelper.create(requestHashMap.get(WorkFlowData.getInstance().DATA))
    

    def _constructor1(self, hashMap: dict) -> None:
        self._init_fields()
        self.workFlowName = hashMap.get(WorkFlowData.getInstance().NAME)
        self.storeName = hashMap.get(StoreFrontData.getInstance().NAME)
        self.workFlowDoc = DomDocumentHelper.create(hashMap.get(WorkFlowData.getInstance().DATA))
    

    def getName(self) -> str:
        return self.workFlowName
    

    def getStoreName(self) -> str:
        return self.storeName
    

    def getKey(self) -> object:
        return self.getName()
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        values: BasicArrayList = BasicArrayListD()
        values.add(self.workFlowName)
        values.add(self.storeName)
        values.add(XmlDocumentHelper.toString(self.workFlowDoc))
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        values.add(time)
        values.add(time)
        return values
    

    # throws Exception
    def toHashMap(self) -> dict:
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(WorkFlowData.getInstance().NAME, self.workFlowName)
        hashMap.put(StoreFrontData.getInstance().NAME, self.storeName)
        hashMap.put(WorkFlowData.getInstance().DATA, XmlDocumentHelper.toString(self.workFlowDoc))
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        hashMap.put(EntryData.getInstance().LASTMODIFIED, time)
        return hashMap
    

    def toXmlNode(self, document: Document) -> Node:
        try:
            hashMap: dict = self.toHashMap()
            keySet: Set = hashMap.keySet()
            node: Node = document.createElement(WorkFlowData.getInstance().WORKFLOW)
            nameArray: list[object] = keySet.toArray()
            size: int = len(nameArray)
            for index in range(0, size):
                name: str = nameArray[index]
                value: str = hashMap.get(name)
                node.appendChild(ModDomHelper.createNameValueNodes(document, name, value))
            return node
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "toXmlNode()", e)
            return None
    

    def toXmlDoc(self) -> Document:
        try:
            return self.workFlowDoc
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "toXmlDoc()", e)
            return None
    

    def isValid(self) -> bool:
        try:
            returnBoolean: bool = True
            if self.workFlowName is None:
                returnBoolean = False
            return returnBoolean
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            if self.workFlowName is None:
                stringBuffer.append("No WorkFlow name specified.")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Getting Validation Info"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


