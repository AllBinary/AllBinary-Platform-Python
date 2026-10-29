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
# package views.business.context.modules.storefront.customizer.bodies.generic

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class GenericBodyCustomizerView(HttpStoreComponentView, DomNodeInterface):
    NAME: str = "None"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.body: GenericBodyValidation = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    # throws Exception
    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self.body)
        self.addDomNodeInterface(self)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        pageName: str = TransformTemplateCustomizerUtil.getInstance().getPageNameHack(self.getTransformInfoInterface().getName(), self.getWeblisketSession().getStoreName())
        if StringValidationUtil.getInstance().isEmpty(pageName):
            pageName = GenericBodyCustomizerView.NAME
        return ModDomHelper.createNameValueNodes(document, PageData.getInstance().NAME, pageName)
    

    # throws Exception
    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            success: str = XmlDocumentHelper.toString(self.getDoc())
            result: str = StoreTransformer(self.abeClientInformation, self.getTransformInfoInterface()).translate(success)
            return StringEscapeUtils.unescapeHtml3(result)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
from org.allbinary.business.page.PageData import PageData
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.StoreTransformer import StoreTransformer
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.template.customizer.bodies.GenericBodyValidation import GenericBodyValidation
from org.allbinary.logic.visual.transform.template.util.TransformTemplateCustomizerUtil import TransformTemplateCustomizerUtil
from org.apache.commons.lang3.StringEscapeUtils import StringEscapeUtils
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


