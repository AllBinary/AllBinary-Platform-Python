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
# package views.admin.inventory

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import lazy_static
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.admin.inventory.InventoryItemView import InventoryItemView


@java_inherited_overloads
class AddFileValidationView(*java_bases(InventoryItemView, ValidationComponentInterface)):
    ADDPRODUCT: str = "Add Product"
    NEXTSTEP: str = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("basicItemData", None)

    def _init_fields(self) -> None:
        from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        __class__._init_fields(self)
    

    def isValid_j0(self) -> bool:
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.business.user.commerce.inventory.item.BasicItemValidation import BasicItemValidation
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.apache.commons.fileupload.FileItem import FileItem
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            command: str = self.getRequestHashMap().get(GLOBALS2.ADMINCOMMAND)
            if StringValidationUtil.getInstance().isEmpty(command) or (((command > AddFileValidationView.ADDPRODUCT) - (command < AddFileValidationView.ADDPRODUCT)) != 0 and ((command > AddFileValidationView.NEXTSTEP) - (command < AddFileValidationView.NEXTSTEP)) != 0):
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("Invalid AdminCommand: ")
                    stringBuffer.append(command)
                    stringBuffer.append(" must be: ")
                    stringBuffer.append(AddFileValidationView.ADDPRODUCT)
                    stringBuffer.append(" or ")
                    stringBuffer.append(AddFileValidationView.NEXTSTEP)
                    self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
                return False
            basicItemValidation: BasicItemValidation = BasicItemValidation(self.itemInterface)
            if java_predicate(basicItemValidation, "isValid") == False:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF(basicItemValidation.validationInfo(), self, self.commonStrings.IS_VALID)
                return False
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getWeblisketSession().getStoreName())
            self.itemInterface.setCategory(storeFrontInterface.getCategoryPath() + self.itemInterface.getCategory())
            fullCategory: str = str(StringMaker().append(URLGLOBALS.getWebappPath()).append(storeFrontInterface.getCurrentHostNamePath()).append(self.itemInterface.getCategory()))
            categoryFile: AbFile = AbFile.createAbFile(fullCategory)
            if not (java_predicate(categoryFile, "isDirectory")):
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Category Does Not Exist: " + fullCategory, self, self.commonStrings.IS_VALID)
                return False
            if InventoryEntityFactory.getInstance().getInventoryEntityInstance().getItem(self.itemInterface.getId()) is not None:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Item Already Exists", self, self.commonStrings.IS_VALID)
                return False
            imageFileItemObject: object = self.getRequestHashMap().get(self.basicItemData.IMAGE)
            if HttpFileUploadUtil.getInstance().isValid(imageFileItemObject):
                fileItem: FileItem = imageFileItemObject
                fileName: str = fileItem.getName()
                size: int = fileItem.getSize()
                HttpFileUploadUtil.log(fileItem)
                if self.isValid(fileName, size) == False:
                    return False
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Exception in validation", self, self.commonStrings.IS_VALID, e)
            return False
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    def validationInfo_j0(self) -> str:
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.business.user.commerce.inventory.item.BasicItemValidation import BasicItemValidation
        from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.apache.commons.fileupload.FileItem import FileItem
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            command: str = self.getRequestHashMap().get(GLOBALS2.ADMINCOMMAND)
            if StringValidationUtil.getInstance().isEmpty(command) or (((command > AddFileValidationView.ADDPRODUCT) - (command < AddFileValidationView.ADDPRODUCT)) != 0 and ((command > AddFileValidationView.NEXTSTEP) - (command < AddFileValidationView.NEXTSTEP)) != 0):
                return StringUtil.getInstance().EMPTY_STRING
            basicItemValidation: BasicItemValidation = BasicItemValidation(self.itemInterface)
            if java_predicate(basicItemValidation, "isValid") == False:
                stringBuffer.append(basicItemValidation.validationInfo())
                stringBuffer.append("<br/>")
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getWeblisketSession().getStoreName())
            fullCategory: str = str(StringMaker().append(URLGLOBALS.getWebappPath()).append(storeFrontInterface.getCurrentHostNamePath()).append(self.itemInterface.getCategory()))
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Category: " + fullCategory, self, "validationInfo()")
            categoryFile: AbFile = AbFile.createAbFile(fullCategory)
            if not (java_predicate(categoryFile, "isDirectory")):
                stringBuffer.append("Category ")
                stringBuffer.append(self.itemInterface.getCategory())
                stringBuffer.append(" does not exist.<br />")
            try:
                if InventoryEntityFactory.getInstance().getInventoryEntityInstance().getItem(self.itemInterface.getId()) is not None:
                    stringBuffer.append("Id is already in use. Refresh the page for a valid id.<br/>")
            except MoneyException as e:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Existing Item With MoneyException", self, "validationInfo()")
            anyType: object = self.getRequestHashMap().get(self.basicItemData.IMAGE)
            if HttpFileUploadUtil.getInstance().isValid(anyType):
                fileItem: FileItem = anyType
                fileName: str = fileItem.getName()
                fileItemFieldName: str = fileItem.getFieldName()
                size: int = fileItem.getSize()
                self.validationInfo(stringBuffer, fileName, fileItemFieldName, size)
            return str(stringBuffer)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Getting Validation Info"
    

    # throws Exception
    def isValid_j2(self, fileName: str, size: int) -> bool:
        from org.allbinary.logic.communication.http.file.upload.media.UploadMediaSingleton import UploadMediaSingleton
        from org.allbinary.logic.io.file.FileData import FileData
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        fileData: FileData = FileData.getInstance()
        if size > fileData.MINIMAGEFILESIZE:
            if size < fileData.MAXIMAGEFILESIZE:
                if not (StringValidationUtil.getInstance().isValidRequired(fileName, fileData.MINLEN, fileData.MAXLEN)):
                    return False
                else:
                    pathData: AbPathData = AbPathData.getInstance()
                    extension: str = pathData.getExtension(fileName)
                    uploadMedia: UploadMediaSingleton = UploadMediaSingleton.getInstance()
                    if not (uploadMedia.isWriterSupported(extension)) and not (uploadMedia.isReaderSupported(extension)):
                        return False
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("File Size To Large: ")
                    stringBuffer.appendlong(size)
                    stringBuffer.append(">")
                    stringBuffer.appendint(int(fileData.MAXIMAGEFILESIZE))
                    self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
                return False
            self.processImageFiles()
        else:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("File Size To Small: ")
                stringBuffer.appendlong(size)
                stringBuffer.append(">")
                stringBuffer.appendint(int(fileData.MINIMAGEFILESIZE))
                self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
            return False
        return True

    def isValid(self, *args):
        implementation = __class__.__dict__.get("isValid_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().isValid(*args)
    

    def validationInfo_j4(self, stringBuffer: StringMaker, fileName: str, fileItemFieldName: str, size: int) -> None:
        from org.allbinary.logic.communication.http.file.upload.media.UploadMediaSingleton import UploadMediaSingleton
        from org.allbinary.logic.io.file.FileData import FileData
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        fileData: FileData = FileData.getInstance()
        if size > fileData.MINIMAGEFILESIZE:
            if ((fileItemFieldName > self.basicItemData.IMAGE) - (fileItemFieldName < self.basicItemData.IMAGE)) == 0:
                if size < fileData.MAXIMAGEFILESIZE:
                    if not (StringValidationUtil.getInstance().isValidRequired(fileName, fileData.MINLEN, fileData.MAXLEN)):
                        stringBuffer.append("FileName must be >")
                        stringBuffer.appendint(int(fileData.MINLEN))
                        stringBuffer.append(" and <")
                        stringBuffer.appendint(int(fileData.MAXLEN))
                        stringBuffer.append("<br/>")
                    else:
                        pathData: AbPathData = AbPathData.getInstance()
                        extension: str = pathData.getExtension(fileName)
                        uploadMedia: UploadMediaSingleton = UploadMediaSingleton.getInstance()
                        if not (uploadMedia.isWriterSupported(extension)) and not (uploadMedia.isReaderSupported(extension)):
                            stringBuffer.append("Image type: ")
                            stringBuffer.append(extension)
                            stringBuffer.append(" not supported.<br />")
                else:
                    stringBuffer.append("Image File Is To Large. ")
                    stringBuffer.appendint(int(fileData.MINIMAGEFILESIZE))
                    stringBuffer.append(" < > ")
                    stringBuffer.appendint(int(fileData.MAXIMAGEFILESIZE))
                    stringBuffer.append("<br/>")
        else:
            stringBuffer.append("Image File Is To Small. ")
            stringBuffer.appendint(int(fileData.MINIMAGEFILESIZE))
            stringBuffer.append(" < > ")
            stringBuffer.appendint(int(fileData.MAXIMAGEFILESIZE))
            stringBuffer.append("<br/>")

    def validationInfo(self, *args):
        implementation = __class__.__dict__.get("validationInfo_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().validationInfo(*args)
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return java_super_call(super(), "getTransformInfoInterface")
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.business.user.commerce.inventory.item.BasicItemValidation import BasicItemValidation
# from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
# from org.allbinary.logic.communication.http.file.upload.media.UploadMediaSingleton import UploadMediaSingleton
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.FileData import FileData
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.apache.commons.fileupload.FileItem import FileItem
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _AddFileValidationView_NEXTSTEP() -> object:
    from org.allbinary.string.CommonLabels import CommonLabels
    return str(CommonLabels.getInstance().NEXT) + " Step"

lazy_static(AddFileValidationView, "NEXTSTEP", _AddFileValidationView_NEXTSTEP)

