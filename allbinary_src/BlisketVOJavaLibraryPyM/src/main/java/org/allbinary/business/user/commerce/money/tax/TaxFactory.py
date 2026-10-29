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
# package org.allbinary.business.user.commerce.money.tax

from __future__ import annotations



class TaxFactory:
    instance: TaxFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.TAXATIONFILENAME: str = "taxationMethod.xml"
    

    @staticmethod
    def getInstance() -> TaxFactory:
        return TaxFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, storeFrontInterface: StoreFrontInterface) -> TaxModuleInterface:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.URLGLOBALS.getMainPath())
        stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
        stringBuffer.append(storeFrontInterface.getName())
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        stringBuffer.append("generic")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        stringBuffer.append("taxes")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        abPath: AbPath = AbPath(str(stringBuffer), self.TAXATIONFILENAME)
        transformInfoObjectConfigData: TransformInfoObjectConfigData = TransformInfoObjectConfigData.getInstance()
        data: str = CryptFileReader(transformInfoObjectConfigData.UNCRYPTED_EXTENSION, transformInfoObjectConfigData.ENCRYPTED_EXTENSION).get(abPath)
        document: Document = DomDocumentHelper.create(data)
        taxNameNodeList: NodeList = document.getElementsByTagName(TaxData.NAME)
        for index in range(0, taxNameNodeList.getLength()):
            node: Node = taxNameNodeList.item(index)
            nodeList: NodeList = node.getChildNodes()
            if nodeList is not None:
                classNameNode: Node = DomSearchHelper.getNode(DynamicObjectData.NAME, nodeList)
                if classNameNode is not None:
                    className: str = DomNodeHelper.getTextNodeValue(classNameNode)
                    return AbeFactory.getInstance().getInstance(abeClientInformation, className)
                else:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAX):
                        self.logUtil.putF("Class Node Null", self, self.commonStrings.GET_INSTANCE)
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAX):
                    self.logUtil.putF("Tax Name Node Node Children", self, self.commonStrings.GET_INSTANCE)
        return SimpleStateTaxModule()
from org.allbinary.business.DynamicObjectData import DynamicObjectData
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.money.tax.components.TaxData import TaxData
from org.allbinary.business.user.commerce.money.tax.modules.SimpleStateTaxModule import SimpleStateTaxModule
from org.allbinary.business.user.commerce.money.tax.modules.TaxModuleInterface import TaxModuleInterface
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


TaxFactory.instance = TaxFactory()

