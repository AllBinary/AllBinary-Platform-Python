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

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from org.allbinary.string.CommonLabels import CommonLabels
from views.admin.inventory.InventoryItemView import InventoryItemView


class AddFileValidationView(InventoryItemView, ValidationComponentInterface):
    ADDPRODUCT: str = "Add Product"
    NEXTSTEP: str = str(CommonLabels.getInstance().NEXT) + " Step"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    def isValid(self) -> bool:
        try:
            command: str = self.getRequestHashMap().get(self.GLOBALS2.ADMINCOMMAND)
            if StringValidationUtil.getInstance().isEmpty(command) or (((command > AddFileValidationView.ADDPRODUCT) - (command < AddFileValidationView.ADDPRODUCT)) != 0 and ((command > AddFileValidationView.NEXTSTEP) - (command < AddFileValidationView.NEXTSTEP)) != 0):
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
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
            if basicItemValidation.isValid() == False:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF(basicItemValidation.validationInfo(), self, self.commonStrings.IS_VALID)
                return False
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getWeblisketSession().getStoreName())
            self.itemInterface.setCategory(storeFrontInterface.getCategoryPath() + self.itemInterface.getCategory())
            fullCategory: str = str(StringMaker().append(self.URLGLOBALS.getWebappPath()).append(storeFrontInterface.getCurrentHostNamePath()).append(self.itemInterface.getCategory()))
            categoryFile: AbFile = AbFile.createAbFile(fullCategory)
            if not categoryFile.isDirectory():
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Category Does Not Exist: " + fullCategory, self, self.commonStrings.IS_VALID)
                return False
            if InventoryEntityFactory.getInstance().getInventoryEntityInstance().getItem(self.itemInterface.getId()) is not None:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
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
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Exception in validation", self, self.commonStrings.IS_VALID, e)
            return False
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            command: str = self.getRequestHashMap().get(self.GLOBALS2.ADMINCOMMAND)
            if StringValidationUtil.getInstance().isEmpty(command) or (((command > AddFileValidationView.ADDPRODUCT) - (command < AddFileValidationView.ADDPRODUCT)) != 0 and ((command > AddFileValidationView.NEXTSTEP) - (command < AddFileValidationView.NEXTSTEP)) != 0):
                return StringUtil.getInstance().EMPTY_STRING
            basicItemValidation: BasicItemValidation = BasicItemValidation(self.itemInterface)
            if basicItemValidation.isValid() == False:
                stringBuffer.append(basicItemValidation.validationInfo())
                stringBuffer.append("<br/>")
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getWeblisketSession().getStoreName())
            fullCategory: str = str(StringMaker().append(self.URLGLOBALS.getWebappPath()).append(storeFrontInterface.getCurrentHostNamePath()).append(self.itemInterface.getCategory()))
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Category: " + fullCategory, self, "validationInfo()")
            categoryFile: AbFile = AbFile.createAbFile(fullCategory)
            if not categoryFile.isDirectory():
                stringBuffer.append("Category ")
                stringBuffer.append(self.itemInterface.getCategory())
                stringBuffer.append(" does not exist.<br />")
            try:
                if InventoryEntityFactory.getInstance().getInventoryEntityInstance().getItem(self.itemInterface.getId()) is not None:
                    stringBuffer.append("Id is already in use. Refresh the page for a valid id.<br/>")
            except MoneyException as e:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
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
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Getting Validation Info"
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def isValid(self, fileName: str, size: int) -> bool:
        fileData: FileData = FileData.getInstance()
        if size > fileData.MINIMAGEFILESIZE:
            if size < fileData.MAXIMAGEFILESIZE:
                if not StringValidationUtil.getInstance().isValidRequired(fileName, fileData.MINLEN, fileData.MAXLEN):
                    return False
                else:
                    pathData: AbPathData = AbPathData.getInstance()
                    extension: str = pathData.getExtension(fileName)
                    uploadMedia: UploadMediaSingleton = UploadMediaSingleton.getInstance()
                    if not uploadMedia.isWriterSupported(extension) and not uploadMedia.isReaderSupported(extension):
                        return False
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("File Size To Large: ")
                    stringBuffer.appendlong(size)
                    stringBuffer.append(">")
                    stringBuffer.appendint(int(fileData.MAXIMAGEFILESIZE))
                    self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
                return False
            self.processImageFiles()
        else:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("File Size To Small: ")
                stringBuffer.appendlong(size)
                stringBuffer.append(">")
                stringBuffer.appendint(int(fileData.MINIMAGEFILESIZE))
                self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
            return False
        return True
    

    # Java overloaded method: Python keeps the last definition
    def validationInfo(self, stringBuffer: StringMaker, fileName: str, fileItemFieldName: str, size: int) -> None:
        fileData: FileData = FileData.getInstance()
        if size > fileData.MINIMAGEFILESIZE:
            if ((fileItemFieldName > self.basicItemData.IMAGE) - (fileItemFieldName < self.basicItemData.IMAGE)) == 0:
                if size < fileData.MAXIMAGEFILESIZE:
                    if not StringValidationUtil.getInstance().isValidRequired(fileName, fileData.MINLEN, fileData.MAXLEN):
                        stringBuffer.append("FileName must be >")
                        stringBuffer.appendint(int(fileData.MINLEN))
                        stringBuffer.append(" and <")
                        stringBuffer.appendint(int(fileData.MAXLEN))
                        stringBuffer.append("<br/>")
                    else:
                        pathData: AbPathData = AbPathData.getInstance()
                        extension: str = pathData.getExtension(fileName)
                        uploadMedia: UploadMediaSingleton = UploadMediaSingleton.getInstance()
                        if not uploadMedia.isWriterSupported(extension) and not uploadMedia.isReaderSupported(extension):
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
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.business.user.commerce.inventory.item.BasicItemValidation import BasicItemValidation
from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
from org.allbinary.globals.GLOBALS2 import GLOBALS2
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
from org.allbinary.logic.communication.http.file.upload.media.UploadMediaSingleton import UploadMediaSingleton
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FileData import FileData
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.apache.commons.fileupload.FileItem import FileItem
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


