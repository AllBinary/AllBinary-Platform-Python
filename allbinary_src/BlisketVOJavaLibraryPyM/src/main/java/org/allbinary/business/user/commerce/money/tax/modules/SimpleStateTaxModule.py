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
# package org.allbinary.business.user.commerce.money.tax.modules

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.business.user.commerce.money.tax.modules.TaxModuleInterface import TaxModuleInterface


class SimpleStateTaxModule(TaxModuleInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "streetAddress" not in vars(self): self.streetAddress: StreetAddress = None
        if "storeFrontInterface" not in vars(self): self.storeFrontInterface: StoreFrontInterface = None
        self.ALL: str = CommonPhoneStrings.getInstance().STAR
        self.STATETAXPATH: str = "/generic/taxes/"
        self.STATETAXFILE: str = "stateTaxation.xml"
        if "document" not in vars(self): self.document: Document = None
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def getTaxRate(self, streetAddress: StreetAddress, storeFrontInterface: StoreFrontInterface) -> float:
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.commerce.money.tax.components.TaxData import TaxData
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        self.streetAddress = streetAddress
        self.storeFrontInterface = storeFrontInterface
        fileAbPath: AbPath = AbPath(str(URLGLOBALS.getMainPath() + FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH) + self.storeFrontInterface.getName() + self.STATETAXPATH, self.STATETAXFILE)
        data: str = CryptFileReader(TransformInfoObjectConfigData.getInstance().UNCRYPTED_EXTENSION, TransformInfoObjectConfigData.getInstance().ENCRYPTED_EXTENSION).get(fileAbPath)
        self.document = DomDocumentHelper.create(data)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAX):
            self.logUtil.putF("Tax Doc: " + XmlDocumentHelper.toString(self.document), self, "getTaxRate")
        state: str = self.streetAddress.getState()
        country: str = self.streetAddress.getCountry()
        state = state.upper()
        nodeList: NodeList = self.document.getElementsByTagName(TaxData.NAME)
        for index in range(0, nodeList.getLength()):
            node: Node = nodeList.item(index)
            taxNodeChildren: NodeList = node.getChildNodes()
            streetAddressNode: Node = DomSearchHelper.getNode(StreetAddressData.NAME, taxNodeChildren)
            taxableStreetAddress: StreetAddress = StreetAddress(streetAddressNode)
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if not (stringValidationUtil.isEmpty(country)) and not (stringValidationUtil.isEmpty(taxableStreetAddress.getCountry())) and ((country > taxableStreetAddress.getCountry()) - (country < taxableStreetAddress.getCountry())) == 0:
                if state is not None and taxableStreetAddress.getState() is not None and ((state > taxableStreetAddress.getState()) - (state < taxableStreetAddress.getState())) == 0:
                    rateNode: Node = DomSearchHelper.getNode(TaxData.RATE, taxNodeChildren)
                    taxRate: str = DomNodeHelper.getTextNodeValue(rateNode)
                    taxRateFloat: float = float(float(float(taxRate)) * .01)
                    return taxRateFloat
        return float(0)
    

    def isValid(self, streetAddress: StreetAddress, storeFrontInterface: StoreFrontInterface) -> bool:
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.business.user.commerce.money.tax.components.TaxData import TaxData
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            self.streetAddress = streetAddress
            self.storeFrontInterface = storeFrontInterface
            fileAbPath: AbPath = AbPath(str(URLGLOBALS.getMainPath() + FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH) + self.storeFrontInterface.getName() + self.STATETAXPATH, self.STATETAXFILE)
            data: str = CryptFileReader(TransformInfoObjectConfigData.getInstance().UNCRYPTED_EXTENSION, TransformInfoObjectConfigData.getInstance().ENCRYPTED_EXTENSION).get(fileAbPath)
            self.document = DomDocumentHelper.create(data)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAX):
                self.logUtil.putF("Tax Doc: " + XmlDocumentHelper.toString(self.document), self, self.commonStrings.IS_VALID)
            country: str = self.streetAddress.getCountry()
            rootNode: Node = self.document.getElementsByTagName(TransformInfoObjectConfigData.getInstance().NAME).item(0)
            nodeList: NodeList = self.document.getElementsByTagName(TaxData.NAME)
            for index in range(0, nodeList.getLength()):
                node: Node = nodeList.item(index)
                taxNodeChildren: NodeList = node.getChildNodes()
                streetAddressNode: Node = DomSearchHelper.getNode(StreetAddressData.NAME, taxNodeChildren)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAX):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("StreetAddress Node: ")
                    stringBuffer.append(streetAddressNode.getNodeName())
                    stringBuffer.append(" Value: ")
                    stringBuffer.append(streetAddressNode.getNodeValue())
                    stringBuffer.append(" Number Of Children: ")
                    stringBuffer.appendint(int(streetAddressNode.getChildNodes().getLength()))
                    self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
                taxableStreetAddress: StreetAddress = StreetAddress(streetAddressNode)
                stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
                if not (stringValidationUtil.isEmpty(country)) and not (stringValidationUtil.isEmpty(taxableStreetAddress.getCountry())) and taxableStreetAddress.getCountry().compareTo(self.ALL) == 0:
                    return True
                if not (stringValidationUtil.isEmpty(country)) and not (stringValidationUtil.isEmpty(taxableStreetAddress.getCountry())) and ((country > taxableStreetAddress.getCountry()) - (country < taxableStreetAddress.getCountry())) == 0:
                    state: str = self.streetAddress.getState()
                    if state is not None:
                        return True
            return False
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate", self, self.commonStrings.IS_VALID, e)
            return False
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.address.StreetAddress import StreetAddress
# from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
# from org.allbinary.business.user.commerce.money.tax.components.TaxData import TaxData
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
# from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


