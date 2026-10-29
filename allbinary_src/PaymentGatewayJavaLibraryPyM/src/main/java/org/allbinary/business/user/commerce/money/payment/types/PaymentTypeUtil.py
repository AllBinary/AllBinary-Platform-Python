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
# package org.allbinary.business.user.commerce.money.payment.types

from __future__ import annotations



class PaymentTypeUtil:
    instance: PaymentTypeUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.PAYMENTGATEWAYFILEPATHSTRING: str = None
        self.SHIPPINGMETHODSFILENAME: str = "paymentGatewayTypes.xml"
        self.defaultName: str = None
        self.paymentTypeVector: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def _static_init() -> None:
        pass
    

    @staticmethod
    def getInstance() -> PaymentTypeUtil:
        return PaymentTypeUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
        stringBuffer: StringMaker = StringMaker()
        sep: str = AbPathData.getInstance().SEPARATOR
        stringBuffer.append(sep)
        stringBuffer.append("generic")
        stringBuffer.append(sep)
        stringBuffer.append("user")
        stringBuffer.append(sep)
        stringBuffer.append("commerce")
        stringBuffer.append(sep)
        stringBuffer.append("money")
        stringBuffer.append(sep)
        stringBuffer.append("payment")
        stringBuffer.append(sep)
        stringBuffer.append("gateway")
        stringBuffer.append(sep)
        self.PAYMENTGATEWAYFILEPATHSTRING = str(stringBuffer)
    

    def add(self, paymentType: PaymentType) -> None:
        self.paymentTypeVector.add(paymentType)
    

    # throws Exception
    def get(self, paymentTypeString: str) -> PaymentType:
        size: int = self.paymentTypeVector.size()
        for i in range(0, size):
            paymentType: PaymentType = self.paymentTypeVector.get(i)
            if paymentType.getBasicPaymentType().getName().compareTo(paymentTypeString) == 0:
                return paymentType
        raise Exception("Unknown PaymentType: " + paymentTypeString)
    

    # throws Exception
    def initDefault(self, storeName: str) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PAYMENT):
            self.logUtil.putF("initDefault Payment: " + self.defaultName, self, "initDefault")
        if StringValidationUtil.getInstance().isEmpty(self.defaultName):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.URLGLOBALS.getMainPath())
            stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
            stringBuffer.append(storeName)
            stringBuffer.append(AbPathData.getInstance().SEPARATOR)
            stringBuffer.append(self.PAYMENTGATEWAYFILEPATHSTRING)
            abPath: AbPath = AbPath(str(stringBuffer), self.SHIPPINGMETHODSFILENAME)
            data: str = CryptFileReader(TransformInfoObjectConfigData.getInstance().UNCRYPTED_EXTENSION, TransformInfoObjectConfigData.getInstance().ENCRYPTED_EXTENSION).get(abPath)
            document: Document = DomDocumentHelper.create(data)
            nodeList: NodeList = document.getElementsByTagName(PaymentGatewaysData.NAME)
            for index in range(0, nodeList.getLength()):
                node: Node = nodeList.item(index)
                defaultPaymentGatewayNode: Node = DomSearchHelper.getNode(EntryData.getInstance().DEFAULT, node.getChildNodes())
                defaultPaymentGatewayNodeValue: str = DomNodeHelper.getTextNodeValue(defaultPaymentGatewayNode)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PAYMENT):
                    self.logUtil.putF("DefaultPaymentGatewayNodeValue: " + defaultPaymentGatewayNodeValue, self, "initDefault")
                if not StringValidationUtil.getInstance().isEmpty(defaultPaymentGatewayNodeValue):
                    self.defaultName = defaultPaymentGatewayNodeValue
    

    # throws Exception
    def getDefault(self, storeName: str) -> PaymentType:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PAYMENT):
            self.logUtil.putF(self.commonStrings.START, self, "getDefault")
        self.initDefault(storeName)
        if not StringValidationUtil.getInstance().isEmpty(self.defaultName):
            return self.get(self.defaultName)
        raise Exception("No Default: " + self.defaultName)
    

    def isContain(self, paymentType: PaymentType) -> bool:
        return self.paymentTypeVector.contains(paymentType)
    

    def difference(self, a_PaymentTypeVector: BasicArrayList) -> BasicArrayList:
        diff: BasicArrayList = BasicArrayListD()
        size: int = self.paymentTypeVector.size()
        for i in range(0, size):
            paymentType: PaymentType = self.paymentTypeVector.get(i)
            if not a_PaymentTypeVector.contains(paymentType):
                diff.add(paymentType)
        return diff
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewaysData import PaymentGatewaysData
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


PaymentTypeUtil.instance = PaymentTypeUtil()

PaymentTypeUtil._static_init()

