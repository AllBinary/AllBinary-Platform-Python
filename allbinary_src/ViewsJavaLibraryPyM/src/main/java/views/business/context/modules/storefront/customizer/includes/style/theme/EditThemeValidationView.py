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
# package views.business.context.modules.storefront.customizer.includes.style.theme

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.modules.storefront.customizer.includes.style.theme.ThemeCustomizerView import ThemeCustomizerView


class EditThemeValidationView(ThemeCustomizerView, ValidationComponentInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    def isValid(self) -> bool:
        try:
            isValid: bool = True
            categoryFactoryInterface: CategoryFactoryInterface = StoreThemeCategoryFactory(self.getTransformInfoInterface())
            categoryLoaderInterface: CategoryLoaderInterface = CategoryLoaderFactory.getInstance(categoryFactoryInterface)
            rootStoreThemeCategoryInterface: StoreThemeCategoryInterface = categoryFactoryInterface.getRootInstance()
            storeThemeCategoryInterface: StoreThemeCategoryInterface = categoryLoaderInterface.getAll(rootStoreThemeCategoryInterface)
            self.validationInterface = StoreThemeCategoryPathValidationView(storeThemeCategoryInterface)
            isValid = self.validationInterface.isValid()
            domNodeInterface: DomNodeInterface = self.validationInterface
            document: Document = DomDocumentHelper.create()
            document.appendChild(domNodeInterface.toXmlNode(document))
            documentString: str = XmlDocumentHelper.toString(document)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.putF("Setting Data: " + documentString, self, self.commonStrings.CONSTRUCTOR)
            self.getTransformInfoInterface().setData(documentString)
            return isValid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.validationInterface.validationInfo())
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Getting Validation Info"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
from org.allbinary.business.category.CategoryInterface import CategoryInterface
from org.allbinary.business.category.store.theme.StoreThemeCategoryFactory import StoreThemeCategoryFactory
from org.allbinary.business.category.store.theme.StoreThemeCategoryInterface import StoreThemeCategoryInterface
from org.allbinary.business.category.store.theme.StoreThemeCategoryPathValidationView import StoreThemeCategoryPathValidationView
from org.allbinary.data.tree.category.CategoryLoaderFactory import CategoryLoaderFactory
from org.allbinary.data.tree.category.CategoryLoaderInterface import CategoryLoaderInterface
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


