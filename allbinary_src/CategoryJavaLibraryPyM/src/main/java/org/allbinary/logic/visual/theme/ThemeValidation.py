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

from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.allbinary.logic.visual.transform.info.CompositeTransformInfoInterface import CompositeTransformInfoInterface
from org.allbinary.logic.visual.theme.ThemeInterface import ThemeInterface


class ThemeValidation(*java_bases(ThemeInterface, ValidationInterface, DomNodeInterface, CompositeTransformInfoInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "transformInfoInterface" not in vars(self): self.transformInfoInterface: TransformInfoInterface = None
        if "styleValidationInterface" not in vars(self): self.styleValidationInterface: ValidationInterface = None
        if "themeName" not in vars(self): self.themeName: str = None
        if "themePreviewImageName" not in vars(self): self.themePreviewImageName: str = None
        if "webAppAbPath" not in vars(self): self.webAppAbPath: AbPath = None
        if "categoryAbPath" not in vars(self): self.categoryAbPath: AbPath = None
        if "fileAbPath" not in vars(self): self.fileAbPath: AbPath = None

    def __init__(self, *args) -> None:
        if len(args) == 3:
            __class__._constructor3(self, *args)
        elif len(args) == 2:
            __class__.__jconstructor2(self, *args)

    def __jconstructor2(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[0]).__mro__)) and not isinstance(args[1], (str, list, int, float)):
            __class__._constructor2_1(self, *args)
        else:
            __class__._constructor2_2(self, *args)
    

    def _constructor3(self, transformInfoInterface: TransformInfoInterface, cssStyleValidation: CssStyleValidation, categoryThemePath: str) -> None:
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.io.path.PathUtil import PathUtil
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.visual.transform.template.customizer.includes.style.css.template.retail.CssStyleValidation import CssStyleValidation
        __class__._init_fields(self)
        self.transformInfoInterface = transformInfoInterface
        pathData: AbPathData = AbPathData.getInstance()
        pathUtil: PathUtil = PathUtil.getInstance()
        self.categoryAbPath = pathUtil.removeNameFromPath(categoryThemePath)
        self.themeName = pathData.getNameFromPath(categoryThemePath)
        self.styleValidationInterface = cssStyleValidation
        self.init()
    

    def _constructor2_1(self, transformInfoInterface: TransformInfoInterface, hashMap: HashMap) -> None:
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.io.path.PathUtil import PathUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        self.transformInfoInterface = transformInfoInterface
        categoryThemeAbPath: AbPath = AbPath(hashMap.get(ThemeData.getInstance().PATH), StringUtil.getInstance().EMPTY_STRING)
        pathData: AbPathData = AbPathData.getInstance()
        pathUtil: PathUtil = PathUtil.getInstance()
        self.categoryAbPath = pathUtil.removeNameFromPath(str(categoryThemeAbPath))
        self.themeName = pathData.getNameFromPath(str(categoryThemeAbPath))
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("CategoryThemePath: ")
            stringBuffer.append(str(categoryThemeAbPath))
            stringBuffer.append(" & CategoryPath: ")
            stringBuffer.append(str(self.categoryAbPath))
            stringBuffer.append(" & ThemeName: ")
            stringBuffer.append(self.themeName)
            self.logUtil.putF("Http Request Constructor", self, str(stringBuffer))
        self.init()
    

    def _constructor2_2(self, storeThemeCategoryInterface: StoreThemeCategoryInterface, node: Node) -> None:
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        from org.allbinary.business.category.store.theme.StoreThemeCategoryInterface import StoreThemeCategoryInterface
        from org.allbinary.data.tree.dom.DomData import DomData
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.w3c.dom.Node import Node
        __class__._init_fields(self)
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
    def init_j0(self) -> None:
        from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
        from org.allbinary.business.category.store.theme.StoreThemeCategoryFactory import StoreThemeCategoryFactory
        from org.allbinary.business.category.store.theme.StoreThemeCategoryInterface import StoreThemeCategoryInterface
        from org.allbinary.data.tree.category.CategoryLoaderFactory import CategoryLoaderFactory
        from org.allbinary.data.tree.category.CategoryLoaderInterface import CategoryLoaderInterface
        categoryFactoryInterface: CategoryFactoryInterface = StoreThemeCategoryFactory(self.getTransformInfoInterface())
        categoryLoaderInterface: CategoryLoaderInterface = CategoryLoaderFactory.getInstance(categoryFactoryInterface)
        rootStoreThemeCategoryInterface: StoreThemeCategoryInterface = categoryFactoryInterface.getRootInstance()
        self.init(rootStoreThemeCategoryInterface)
    

    # throws Exception
    def init_j1(self, storeThemeCategoryInterface: StoreThemeCategoryInterface) -> None:
        from org.allbinary.business.category.store.theme.StoreThemeCategoryInterface import StoreThemeCategoryInterface
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.fileAbPath = AbPath(str(storeThemeCategoryInterface.getRootFilePath()) + str(self.categoryAbPath), StringUtil.getInstance().EMPTY_STRING)
        self.webAppAbPath = storeThemeCategoryInterface.getWebAppPath()

    def init(self, *args):
        implementation = __class__.__dict__.get("init_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().init(*args)
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
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
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.visual.transform.template.customizer.includes.style.css.template.retail.CssStyleValidation import CssStyleValidation
        from org.w3c.dom.Document import Document
        if self.styleValidationInterface is None:
            cssStyleFileAbPath: AbPath = AbPath(str(self.fileAbPath), self.themeName + str(AbPathData.getInstance().EXTENSION_SEP) + str(CategoryData.getInstance().UNCRYPTED_EXTENSION))
            cryptFileReader: CryptFileReader = CryptFileReader(CategoryData.getInstance().UNCRYPTED_EXTENSION, CategoryData.getInstance().ENCRYPTED_EXTENSION)
            document: Document = DomDocumentHelper.create(cryptFileReader.get(cssStyleFileAbPath))
            self.styleValidationInterface = CssStyleValidation(document)
        return self.styleValidationInterface
    

    def isValid(self) -> bool:
        from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            isValid: bool = True
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.IS_VALID)
            if not (StringValidationUtil.getInstance().isValidRequired(str(self.categoryAbPath), AbSqlData.MINSTRING, AbSqlData.MAXSTRING)):
                isValid = False
            if not (StringValidationUtil.getInstance().isValidRequired(self.themeName, AbSqlData.MINSTRING, AbSqlData.MAXSTRING)):
                isValid = False
            if not (java_predicate(self.getCssStyleValidation(), "isValid")):
                isValid = False
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("End: " + str(isValid), self, self.commonStrings.IS_VALID)
            return isValid
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Theme Validation Error")
            return str(stringBuffer)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    def getKey(self) -> object:
        return self.getName()
    

    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        vector: BasicArrayList = BasicArrayListD()
        vector.add(self.getName())
        vector.add(self.getPath())
        vector.add(self.getPreviewImageName())
        vector.add(self.getPreviewImagePath())
        return vector
    

    def toHashMap(self) -> HashMap:
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        themeData: ThemeData = ThemeData.getInstance()
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(themeData.NAME, self.getName())
        hashMap.put(themeData.PATH, self.getPath())
        hashMap.put(themeData.PREVIEW_IMAGE_NAME, self.getPreviewImageName())
        hashMap.put(themeData.PREVIEW_IMAGE_PATH, self.getPreviewImagePath())
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = ModDomHelper.createNameValueNodes(document, ThemeData.getInstance().NAME, self.toHashMap())
        domNodeInterface: DomNodeInterface = self.getCssStyleValidation()
        node.appendChild(domNodeInterface.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.category.CategoryData import CategoryData
# from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
# from org.allbinary.business.category.store.theme.StoreThemeCategoryFactory import StoreThemeCategoryFactory
# from org.allbinary.business.category.store.theme.StoreThemeCategoryInterface import StoreThemeCategoryInterface
# from org.allbinary.data.tree.category.CategoryLoaderFactory import CategoryLoaderFactory
# from org.allbinary.data.tree.category.CategoryLoaderInterface import CategoryLoaderInterface
# from org.allbinary.data.tree.dom.DomData import DomData
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
# from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.io.path.PathUtil import PathUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.visual.transform.template.customizer.includes.style.css.template.retail.CssStyleValidation import CssStyleValidation
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


