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
# package views.generic.address.billing

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class BillingAddressesView(HttpStoreComponentView, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.request: HttpServletRequest = None
        self.streetAddresses: BasicArrayList = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        httpTransformInfoInterface: TransformInfoHttpInterface = self.getTransformInfoInterface()
        self.request = httpTransformInfoInterface.getPageContext().getRequest()
    

    def getRequest(self) -> HttpServletRequest:
        return self.request
    

    def toXmlNode(self, document: Document) -> Node:
        try:
            billingAddressesNode: Node = document.createElement(BillingAddressData.MULTIPLE)
            size: int = self.streetAddresses.size()
            for index in range(0, size):
                streetAddress: StreetAddress = self.streetAddresses.get(index)
                billingAddressesNode.appendChild(streetAddress.toXmlNode(document))
            billingAddressesNode.appendChild(ModDomHelper.createNameValueNodes(document, StreetAddressData.NUMBEROFADDRESSES, str(int(self.streetAddresses.size()))))
            return billingAddressesNode
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            return None
    

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
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


