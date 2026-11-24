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
# package views.generic.address.shipping

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class ShippingAddressesView(*java_bases(HttpStoreComponentView, DomNodeInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.request: HttpServletRequest = None
        self.streetAddressList: BasicArrayList = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        self._init_fields()
        httpTransformInfoInterface: TransformInfoHttpInterface = self.getTransformInfoInterface()
        self.request = httpTransformInfoInterface.getPageContext().getRequest()
    

    def getRequest(self) -> HttpServletRequest:
        return self.request
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            billingAddressesNode: Node = document.createElement(ShippingAddressData.MULTIPLE)
            size: int = self.streetAddressList.size()
            for index in range(0, size):
                streetAddress: StreetAddress = self.streetAddressList.get(index)
                billingAddressesNode.appendChild(streetAddress.toXmlNode(document))
            billingAddressesNode.appendChild(ModDomHelper.createNameValueNodes(document, StreetAddressData.NUMBEROFADDRESSES, str(int(self.streetAddressList.size()))))
            return billingAddressesNode
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            raise e
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    # throws Exception
    def view(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
# from org.allbinary.business.user.address.StreetAddress import StreetAddress
# from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


