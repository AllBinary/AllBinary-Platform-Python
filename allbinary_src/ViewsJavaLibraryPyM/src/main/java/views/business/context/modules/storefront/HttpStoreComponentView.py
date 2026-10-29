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
# package views.business.context.modules.storefront

from __future__ import annotations

from views.HttpComponentView import HttpComponentView


class HttpStoreComponentView(HttpComponentView):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("View Name: " + transformInfoInterface.getName(), self, self.commonStrings.CONSTRUCTOR)
        self.setTransformDocumentInterface(TransformStoreDocumentFactory.getInstance(self.getPageContext(), self.getWeblisketSession()))
    

    # throws Exception
    def view(self) -> str:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, "view")
            self.toXmlDoc()
            success: str = XmlDocumentHelper.toString(self.getDoc())
            result: str = StoreTransformer(self.abeClientInformation, self.getTransformInfoInterface()).translate(success)
            return result
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view", e)
            raise e
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.StoreTransformer import StoreTransformer
from org.allbinary.logic.visual.transform.data.TransformStoreDocumentFactory import TransformStoreDocumentFactory
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonStrings import CommonStrings


