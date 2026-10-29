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
# package org.allbinary.logic.visual.theme

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.allbinary.logic.visual.transform.info.CompositeTransformInfoInterface import CompositeTransformInfoInterface
from org.allbinary.logic.visual.theme.ThemeInterface import ThemeInterface


class ThemeValidation(ThemeInterface, ValidationInterface, DomNodeInterface, CompositeTransformInfoInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.transformInfoInterface: TransformInfoInterface = None
        self.styleValidationInterface: ValidationInterface = None
        self.themeName: str = None
        self.themePreviewImageName: str = None
        self.webAppAbPath: AbPath = None
        self.categoryAbPath: AbPath = None
        self.fileAbPath: AbPath = None

    def __init__(self, *args) -> None:
        if len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor3(self, transformInfoInterface: TransformInfoInterface, cssStyleValidation: CssStyleValidation, categoryThemePath: str) -> None:
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
        pathData: AbPathData = AbPathData.getInstance()
        pathUtil: PathUtil = PathUtil.getInstance()
        self.categoryAbPath = pathUtil.removeNameFromPath(categoryThemePath)
        self.themeName = pathData.getNameFromPath(categoryThemePath)
        self.styleValidationInterface = cssStyleValidation
        self.init()
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, hashMap: dict) -> None:
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
        categoryThemeAbPath: AbPath = AbPath(hashMap.get(ThemeData.getInstance().PATH), StringUtil.getInstance().EMPTY_STRING)
        pathData: AbPathData = AbPathData.getInstance()
        pathUtil: PathUtil = PathUtil.getInstance()
        self.categoryAbPath = pathUtil.removeNameFromPath(str(categoryThemeAbPath))
        self.themeName = pathData.getNameFromPath(str(categoryThemeAbPath))
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("CategoryThemePath: ")
            stringBuffer.append(str(categoryThemeAbPath))
            stringBuffer.append(" & CategoryPath: ")
            stringBuffer.append(str(self.categoryAbPath))
            stringBuffer.append(" & ThemeName: ")
            stringBuffer.append(self.themeName)
            self.logUtil.putF("Http Request Constructor", self, str(stringBuffer))
        self.init()
    

    def _constructor2(self, storeThemeCategoryInterface: StoreThemeCategoryInterface, node: Node) -> None:
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        self._init_fields()
        self.transformInfoInterface = storeThemeCategoryInterface.getTransformInfoInterface()
        self.categoryAbPath = storeThemeCategoryInterface.getPath()
        themeNameNode: Node = DomSearchHelper.getNode(ThemeData.getInstance().NAME, node.getChildNodes())
        valueNode: Node = DomSearchHelper.getNode(DomData.VALUE, themeNameNode.getChildNodes())
        self.themeName = DomNodeHelper.getTextNodeValue(valueNode)
        previewImageNameNode: Node = DomSearchHelper.getNode(ThemeData.getInstance().PREVIEW_IMAGE_NAME, node.getChildNodes())
        previewImageNameValueNode: Node = DomSearchHelper.getNode(DomData.VALUE, previewImageNameNode.getChildNodes())
        self.themePreviewImageName = DomNodeHelper.getTextNodeValue(previewImageNameValueNode)
        self.webAppAbPath = storeThemeCategoryInterface.getWebAppPath()
        self.init(storeThemeCategoryInterface)
    

    # throws Exception
    def init(self) -> None:
        categoryFactoryInterface: CategoryFactoryInterface = StoreThemeCategoryFactory(self.getTransformInfoInterface())
        categoryLoaderInterface: CategoryLoaderInterface = CategoryLoaderFactory.getInstance(categoryFactoryInterface)
        rootStoreThemeCategoryInterface: StoreThemeCategoryInterface = categoryFactoryInterface.getRootInstance()
        self.init(rootStoreThemeCategoryInterface)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def init(self, storeThemeCategoryInterface: StoreThemeCategoryInterface) -> None:
        self.fileAbPath = AbPath(str(storeThemeCategoryInterface.getRootFilePath()) + str(self.categoryAbPath), StringUtil.getInstance().EMPTY_STRING)
        self.webAppAbPath = storeThemeCategoryInterface.getWebAppPath()
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        return self.transformInfoInterface
    

    def getName(self) -> str:
        return self.themeName
    

    def getPreviewImageName(self) -> str:
        return self.themePreviewImageName
    

    def getPreviewImagePath(self) -> str:
        return str(self.webAppAbPath) + str(self.categoryAbPath)
    

    def getPath(self) -> str:
        return str(self.categoryAbPath)
    

    # throws Exception
    def getCssStyleValidation(self) -> CssStyleValidation:
        if self.styleValidationInterface is None:
            cssStyleFileAbPath: AbPath = AbPath(str(self.fileAbPath), self.themeName + str(AbPathData.getInstance().EXTENSION_SEP) + str(CategoryData.getInstance().UNCRYPTED_EXTENSION))
            cryptFileReader: CryptFileReader = CryptFileReader(CategoryData.getInstance().UNCRYPTED_EXTENSION, CategoryData.getInstance().ENCRYPTED_EXTENSION)
            document: Document = DomDocumentHelper.create(cryptFileReader.get(cssStyleFileAbPath))
            self.styleValidationInterface = CssStyleValidation(document)
        return self.styleValidationInterface
    

    def isValid(self) -> bool:
        try:
            isValid: bool = True
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.IS_VALID)
            if not StringValidationUtil.getInstance().isValidRequired(str(self.categoryAbPath), AbSqlData.MINSTRING, AbSqlData.MAXSTRING):
                isValid = False
            if not StringValidationUtil.getInstance().isValidRequired(self.themeName, AbSqlData.MINSTRING, AbSqlData.MAXSTRING):
                isValid = False
            if not self.getCssStyleValidation().isValid():
                isValid = False
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("End: " + str(isValid), self, self.commonStrings.IS_VALID)
            return isValid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Theme Validation Error")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    def getKey(self) -> object:
        return self.getName()
    

    def toVector(self) -> BasicArrayList:
        vector: BasicArrayList = BasicArrayListD()
        vector.add(self.getName())
        vector.add(self.getPath())
        vector.add(self.getPreviewImageName())
        vector.add(self.getPreviewImagePath())
        return vector
    

    def toHashMap(self) -> dict:
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        themeData: ThemeData = ThemeData.getInstance()
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(themeData.NAME, self.getName())
        hashMap.put(themeData.PATH, self.getPath())
        hashMap.put(themeData.PREVIEW_IMAGE_NAME, self.getPreviewImageName())
        hashMap.put(themeData.PREVIEW_IMAGE_PATH, self.getPreviewImagePath())
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        node: Node = ModDomHelper.createNameValueNodes(document, ThemeData.getInstance().NAME, self.toHashMap())
        domNodeInterface: DomNodeInterface = self.getCssStyleValidation()
        node.appendChild(domNodeInterface.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.category.CategoryData import CategoryData
from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
from org.allbinary.business.category.store.theme.StoreThemeCategoryFactory import StoreThemeCategoryFactory
from org.allbinary.business.category.store.theme.StoreThemeCategoryInterface import StoreThemeCategoryInterface
from org.allbinary.data.tree.category.CategoryLoaderFactory import CategoryLoaderFactory
from org.allbinary.data.tree.category.CategoryLoaderInterface import CategoryLoaderInterface
from org.allbinary.data.tree.dom.DomData import DomData
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.io.path.PathUtil import PathUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.template.customizer.includes.style.css.template.retail.CssStyleValidation import CssStyleValidation
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


