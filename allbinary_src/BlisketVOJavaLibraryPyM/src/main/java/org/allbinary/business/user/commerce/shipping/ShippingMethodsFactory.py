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
# package org.allbinary.business.user.commerce.shipping

from __future__ import annotations



class ShippingMethodsFactory:
    SHIPPINGMETHODSFILEPATHSTRING: str = None
    SHIPPINGMETHODSFILENAME: str = "shippingMethods.xml"

    def _init_fields(self) -> None:
        self.defaultShippingMethodInterface: ShippingInterface = None
        self.document: Document = None
        self.shippingVector: BasicArrayList = None
    

    @staticmethod
    def _static_init() -> None:
        stringBuffer: StringMaker = StringMaker()
        sep: str = AbPathData.getInstance().SEPARATOR
        stringBuffer.append(sep)
        stringBuffer.append("generic")
        stringBuffer.append(sep)
        stringBuffer.append("shipping")
        stringBuffer.append(sep)
        ShippingMethodsFactory.SHIPPINGMETHODSFILEPATHSTRING = str(stringBuffer)
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, storeFrontInterface: StoreFrontInterface) -> None:
        from org.allbinary.business.user.commerce.shipping.ShippingMethodsData import ShippingMethodsData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        self._init_fields()
        stringBuffer: StringMaker = StringMaker()
        sep: str = AbPathData.getInstance().SEPARATOR
        stringBuffer.append(self.URLGLOBALS.getMainPath())
        stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
        stringBuffer.append(storeFrontInterface.getName())
        stringBuffer.append(sep)
        stringBuffer.append(ShippingMethodsFactory.SHIPPINGMETHODSFILEPATHSTRING)
        abPath: AbPath = AbPath(str(stringBuffer), self.SHIPPINGMETHODSFILENAME)
        data: str = CryptFileReader(TransformInfoObjectConfigData.getInstance().UNCRYPTED_EXTENSION, TransformInfoObjectConfigData.getInstance().ENCRYPTED_EXTENSION).get(abPath)
        self.document = DomDocumentHelper.create(data)
        self.shippingVector = BasicArrayListD()
        nodeList: NodeList = self.document.getElementsByTagName(ShippingMethodsData.NAME)
        for index in range(0, nodeList.getLength()):
            node: Node = nodeList.item(index)
            shippingMethodNodeChildren: NodeList = node.getChildNodes()
            shippingMethodNameNode: Node = DomSearchHelper.getNode(ShippingMethodData.NAME, shippingMethodNodeChildren)
            classNameNode: Node = DomSearchHelper.getNode(DynamicObjectData.NAME, shippingMethodNameNode.getChildNodes())
            shippingMethodClassName: str = DomNodeHelper.getTextNodeValue(classNameNode)
            shippingMethodInterface: ShippingInterface = AbeFactory.getInstance().getInstance(abeClientInformation, shippingMethodClassName)
            self.shippingVector.add(shippingMethodInterface)
            defaultShippingMethodNameNode: Node = DomSearchHelper.getNode(ShippingMethodData.DEFAULT, shippingMethodNameNode.getChildNodes())
            defaultShippingMethodNameNodeValue: str = DomNodeHelper.getTextNodeValue(defaultShippingMethodNameNode)
            if defaultShippingMethodNameNodeValue is not None and ((defaultShippingMethodNameNodeValue > ShippingMethodData.DEFAULT) - (defaultShippingMethodNameNodeValue < ShippingMethodData.DEFAULT)) == 0:
                self.defaultShippingMethodInterface = shippingMethodInterface
        if self.shippingVector.size() < 1:
            self.defaultShippingMethodInterface = BasicWeightShippingModuleView()
            self.shippingVector.add(self.defaultShippingMethodInterface)
            self.shippingVector.add(NoShippingModuleView())
    

    # throws Exception
    def getInstance(self) -> BasicArrayList:
        return self.shippingVector
    

    def getDefaultInstance(self) -> ShippingInterface:
        return self.defaultShippingMethodInterface
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.DynamicObjectData import DynamicObjectData
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.shipping.modules.BasicWeightShippingModuleView import BasicWeightShippingModuleView
from org.allbinary.business.user.commerce.shipping.modules.NoShippingModuleView import NoShippingModuleView
from org.allbinary.business.user.commerce.shipping.modules.ShippingInterface import ShippingInterface
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


ShippingMethodsFactory._static_init()

