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

from java.lang.JavaRuntimeStatic import lazy_static
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.admin.inventory.InventoryItemView import InventoryItemView


class UpdateFileValidationView(*java_bases(InventoryItemView, ValidationComponentInterface)):
    UPDATEPRODUCT: str = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    def isValid_j0(self) -> bool:
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.business.user.commerce.inventory.item.BasicItemValidation import BasicItemValidation
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.apache.commons.fileupload.FileItem import FileItem
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            command: str = self.getRequestHashMap().get(GLOBALS2.ADMINCOMMAND)
            if command is None or ((command > UpdateFileValidationView.UPDATEPRODUCT) - (command < UpdateFileValidationView.UPDATEPRODUCT)) != 0:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Invalid AdminCommand=" + command, self, self.commonStrings.IS_VALID)
                return False
            if BasicItemValidation(self.itemInterface).isValid() == False:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("BasicItem is not valid", self, self.commonStrings.IS_VALID)
                return False
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getWeblisketSession().getStoreName())
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(URLGLOBALS.getWebappPath())
            stringBuffer.append(storeFrontInterface.getCurrentHostNamePath())
            stringBuffer.append(self.itemInterface.getCategory())
            fullCategory: str = str(stringBuffer)
            categoryFile: AbFile = AbFile.createAbFile(fullCategory)
            if not categoryFile.isDirectory():
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Category Does Not Exist: " + fullCategory, self, self.commonStrings.IS_VALID)
                return False
            inventoryEntity: InventoryEntity = InventoryEntityFactory.getInstance().getInventoryEntityInstance()
            if inventoryEntity.getItem(self.itemInterface.getId()) is None:
                return False
            anyType: object = self.getRequestHashMap().get(self.basicItemData.IMAGE)
            if HttpFileUploadUtil.getInstance().isValid(anyType):
                fileItem: FileItem = anyType
                size: int = fileItem.getSize()
                fileName: str = fileItem.getName()
                HttpFileUploadUtil.log(fileItem)
                if self.isValid(fileName, size) == False:
                    return False
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.put("Exception in validation", self, self.commonStrings.IS_VALID, e)
            return False
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    # throws Exception
    def validationInfo_j0(self) -> str:
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.business.user.commerce.inventory.item.BasicItemValidation import BasicItemValidation
        from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.apache.commons.fileupload.FileItem import FileItem
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        command: str = self.getRequestHashMap().get(GLOBALS2.ADMINCOMMAND)
        if command is None or ((command > UpdateFileValidationView.UPDATEPRODUCT) - (command < UpdateFileValidationView.UPDATEPRODUCT)) != 0:
            return CommonSeps.getInstance().SPACE
        stringBuffer.append(BasicItemValidation(self.itemInterface).validationInfo())
        storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getWeblisketSession().getStoreName())
        fullCategory: str = URLGLOBALS.getWebappPath() + storeFrontInterface.getCurrentHostNamePath() + self.itemInterface.getCategory()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Category: " + fullCategory, self, "validationInfo()")
        try:
            if InventoryEntityFactory.getInstance().getInventoryEntityInstance().getItem(self.itemInterface.getId()) is None:
                stringBuffer.append("Item does not exist.<br>")
        except MoneyException as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Existing Item With MoneyException", self, "validationInfo()")
        anyType: object = self.getRequestHashMap().get(self.basicItemData.IMAGE)
        if HttpFileUploadUtil.getInstance().isValid(anyType):
            fileItem: FileItem = anyType
            size: int = fileItem.getSize()
            fileName: str = fileItem.getName()
            fileItemFieldName: str = fileItem.getFieldName()
            self.validationInfo(stringBuffer, fileName, fileItemFieldName, size)
        return str(stringBuffer)
    

    # throws Exception
    def isValid_j2(self, fileName: str, size: int) -> bool:
        from org.allbinary.logic.io.file.FileData import FileData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        fileData: FileData = FileData.getInstance()
        if size > fileData.MINIMAGEFILESIZE:
            if size < fileData.MAXIMAGEFILESIZE:
                if not StringValidationUtil.getInstance().isValidRequired(fileName, fileData.MINLEN, fileData.MAXLEN):
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
        return True

    def isValid(self, *args):
        return getattr(self, "isValid_j" + str(len(args)))(*args)
    

    def validationInfo_j4(self, stringBuffer: StringMaker, fileName: str, fileItemFieldName: str, size: int) -> None:
        from org.allbinary.logic.io.file.FileData import FileData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        fileData: FileData = FileData.getInstance()
        if size > fileData.MINIMAGEFILESIZE:
            if ((fileItemFieldName > self.basicItemData.IMAGE) - (fileItemFieldName < self.basicItemData.IMAGE)) == 0:
                if size < fileData.MAXIMAGEFILESIZE:
                    if not StringValidationUtil.getInstance().isValidRequired(fileName, fileData.MINLEN, fileData.MAXLEN):
                        stringBuffer.append("FileName must be >")
                        stringBuffer.appendint(int(fileData.MINLEN))
                        stringBuffer.append("and <")
                        stringBuffer.appendint(int(fileData.MAXLEN))
                        stringBuffer.append("<br />")
                else:
                    stringBuffer.append("Image File Is Not The Right Size. ")
                    stringBuffer.appendint(int(fileData.MINIMAGEFILESIZE))
                    stringBuffer.append("< > ")
                    stringBuffer.appendint(int(fileData.MAXIMAGEFILESIZE))
                    stringBuffer.append("<br />")

    def validationInfo(self, *args):
        return getattr(self, "validationInfo_j" + str(len(args)))(*args)
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return super().getTransformInfoInterface()
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.business.user.commerce.inventory.item.BasicItemValidation import BasicItemValidation
# from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.FileData import FileData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.apache.commons.fileupload.FileItem import FileItem
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _UpdateFileValidationView_UPDATEPRODUCT() -> object:
    from org.allbinary.string.CommonStrings import CommonStrings
    return CommonStrings.getInstance().UPDATE

lazy_static(UpdateFileValidationView, "UPDATEPRODUCT", _UpdateFileValidationView_UPDATEPRODUCT)

