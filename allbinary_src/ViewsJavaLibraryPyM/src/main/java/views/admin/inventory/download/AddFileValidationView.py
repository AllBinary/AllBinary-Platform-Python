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
# package views.admin.inventory.download

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.admin.inventory.download.DownloadableInventoryItemView import DownloadableInventoryItemView


@java_inherited_overloads
class AddFileValidationView(*java_bases(DownloadableInventoryItemView, ValidationComponentInterface)):
    ADDPRODUCT: str = "Finish"
    ADDANOTHERDOWNLOADABLE: str = "Add Another"
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
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.business.user.commerce.inventory.item.BasicItemValidation import BasicItemValidation
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItemValidation import DownloadableItemValidation
        from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
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
            command: str = self.getRequestHashMap().get(GLOBALS2.ADMINCOMMAND)
            if StringValidationUtil.getInstance().isEmpty(command) or (((command > AddFileValidationView.ADDPRODUCT) - (command < AddFileValidationView.ADDPRODUCT)) != 0 and ((command > AddFileValidationView.ADDANOTHERDOWNLOADABLE) - (command < AddFileValidationView.ADDANOTHERDOWNLOADABLE)) != 0):
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Invalid AdminCommand=" + command, self, self.commonStrings.IS_VALID)
                return False
            try:
                inventoryEntity: InventoryEntity = InventoryEntityFactory.getInstance().getInventoryEntityInstance()
                self.itemInterface = inventoryEntity.getItem(self.id)
            except MoneyException as e:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.put("Existing Item With MoneyException", self, self.commonStrings.IS_VALID, e)
            if self.itemInterface is None:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Item Does Not Exist", self, self.commonStrings.IS_VALID)
                return False
            if java_predicate(BasicItemValidation(self.itemInterface), "isValid") == False:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("BasicItem is not valid", self, self.commonStrings.IS_VALID)
                return False
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getWeblisketSession().getStoreName())
            fullCategory: str = str(StringMaker().append(URLGLOBALS.getWebappPath()).append(storeFrontInterface.getCurrentHostNamePath()).append(self.itemInterface.getCategory()))
            categoryFile: AbFile = AbFile.createAbFile(fullCategory)
            if not (java_predicate(categoryFile, "isDirectory")):
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("Category Does Not Exist: " + fullCategory, self, self.commonStrings.IS_VALID)
                return False
            downloadableFileObject: object = self.getRequestHashMap().get(DownloadItemData.FILE)
            if HttpFileUploadUtil.getInstance().isValid(downloadableFileObject):
                fileItem: FileItem = downloadableFileObject
                fileName: str = fileItem.getName()
                size: int = fileItem.getSize()
                HttpFileUploadUtil.log(fileItem)
                if self.isValid(fileName, size) == False:
                    return False
                else:
                    self.processFile(fileItem)
                    self.getRequestHashMap().put(DownloadItemData.SIZE, str(size))
            else:
                self.getRequestHashMap().remove(DownloadItemData.FILE)
            licenseFileObject: object = self.getRequestHashMap().get(DownloadItemData.LICENSE_FILE)
            if HttpFileUploadUtil.getInstance().isValid(licenseFileObject):
                fileItem: FileItem = licenseFileObject
                fileName: str = fileItem.getName()
                size: int = fileItem.getSize()
                HttpFileUploadUtil.log(fileItem)
                if self.isValid(fileName, size) == False:
                    pass
                else:
                    self.processFile(fileItem)
            else:
                self.getRequestHashMap().remove(DownloadItemData.LICENSE_FILE)
            extraFilesObject: object = self.getRequestHashMap().get(DownloadItemData.EXTRA_FILES)
            if HttpFileUploadUtil.getInstance().isValid(extraFilesObject):
                fileItem: FileItem = extraFilesObject
                fileName: str = fileItem.getName()
                size: int = fileItem.getSize()
                HttpFileUploadUtil.log(fileItem)
                if self.isValid(fileName, size) == False:
                    pass
                else:
                    self.processFile(fileItem)
                    self.unzip(fileItem)
            else:
                self.getRequestHashMap().remove(DownloadItemData.EXTRA_FILES)
            hashMap: HashMap = self.getRequestHashMap()
            hashMap.put(self.basicItemData.ID, self.itemInterface.getId())
            licenseObject: object = hashMap.get(DownloadItemData.LICENSE_FILE)
            if licenseObject is not None:
                hashMap.put(DownloadItemData.LICENSE_FILE, (licenseObject).getName())
            else:
                hashMap.put(DownloadItemData.LICENSE_FILE, StringUtil.getInstance().EMPTY_STRING)
            fileObject: object = hashMap.get(DownloadItemData.FILE)
            if fileObject is not None:
                hashMap.put(DownloadItemData.FILE, (fileObject).getName())
            else:
                hashMap.put(DownloadItemData.FILE, StringUtil.getInstance().EMPTY_STRING)
            self.downloadableItem = DownloadableItem(hashMap)
            downloadableItemValidation: DownloadableItemValidation = DownloadableItemValidation(self.downloadableItem)
            if java_predicate(downloadableItemValidation, "isValid") == False:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF("DownloadableItem is not valid", self, self.commonStrings.IS_VALID)
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
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItemValidation import DownloadableItemValidation
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
            if StringValidationUtil.getInstance().isEmpty(command) or (((command > AddFileValidationView.ADDPRODUCT) - (command < AddFileValidationView.ADDPRODUCT)) != 0 and ((command > AddFileValidationView.ADDANOTHERDOWNLOADABLE) - (command < AddFileValidationView.ADDANOTHERDOWNLOADABLE)) != 0):
                return StringUtil.getInstance().EMPTY_STRING
            if self.itemInterface is None:
                ITEM_NOT_FOUND: str = "Item Does Not Exist"
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    self.logUtil.putF(ITEM_NOT_FOUND, self, "validationInfo()")
                return ITEM_NOT_FOUND
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
                stringBuffer.append(" does not exist.")
                stringBuffer.append("<br />")
            downloadableFileObject: object = self.getRequestHashMap().get(DownloadItemData.FILE)
            if HttpFileUploadUtil.getInstance().isValid(downloadableFileObject):
                fileItem: FileItem = downloadableFileObject
                fileName: str = fileItem.getName()
                size: int = fileItem.getSize()
                self.validationInfo(stringBuffer, fileName, size)
            else:
                stringBuffer.append("Download File Missing")
                stringBuffer.append("<br/>")
            licenseFileObject: object = self.getRequestHashMap().get(DownloadItemData.LICENSE_FILE)
            if HttpFileUploadUtil.getInstance().isValid(licenseFileObject):
                fileItem: FileItem = licenseFileObject
                fileName: str = fileItem.getName()
                size: int = fileItem.getSize()
                self.validationInfo(stringBuffer, fileName, size)
            else:
                pass
            extraFilesObject: object = self.getRequestHashMap().get(DownloadItemData.EXTRA_FILES)
            if HttpFileUploadUtil.getInstance().isValid(extraFilesObject):
                fileItem: FileItem = extraFilesObject
                fileName: str = fileItem.getName()
                size: int = fileItem.getSize()
                self.validationInfo(stringBuffer, fileName, size)
            else:
                pass
            if self.downloadableItem is not None:
                downloadableItemValidation: DownloadableItemValidation = DownloadableItemValidation(self.downloadableItem)
                if java_predicate(downloadableItemValidation, "isValid") == False:
                    log: str = downloadableItemValidation.validationInfo()
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                        self.logUtil.putF(log, self, self.commonStrings.IS_VALID)
                    stringBuffer.append(log)
                    stringBuffer.append("<br/>")
            return str(stringBuffer)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Getting Validation Info"
    

    # throws Exception
    def isValid_j2(self, fileName: str, size: int) -> bool:
        from org.allbinary.logic.io.file.FileData import FileData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        fileData: FileData = FileData.getInstance()
        if size > fileData.MINDOWNLOADABLEFILESIZE:
            if size < fileData.MAXDOWNLOADABLEFILESIZE:
                if not (StringValidationUtil.getInstance().isValidRequired(fileName, fileData.MINLEN, fileData.MAXLEN)):
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                        stringBuffer: StringMaker = StringMaker()
                        stringBuffer.append("File name is not valid: ")
                        stringBuffer.append(fileName)
                        self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
                    return False
                else:
                    pass
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("File Size To Large: ")
                    stringBuffer.appendlong(size)
                    stringBuffer.append(">")
                    stringBuffer.appendint(int(fileData.MAXDOWNLOADABLEFILESIZE))
                    self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
                return False
        else:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("File Size To Small: ")
                stringBuffer.appendlong(size)
                stringBuffer.append(">")
                stringBuffer.appendint(int(fileData.MINDOWNLOADABLEFILESIZE))
                self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
            return False
        return True

    def isValid(self, *args):
        implementation = __class__.__dict__.get("isValid_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().isValid(*args)
    

    def validationInfo_j3(self, stringBuffer: StringMaker, fileName: str, size: int) -> None:
        from org.allbinary.logic.io.file.FileData import FileData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        fileData: FileData = FileData.getInstance()
        if size > fileData.MINDOWNLOADABLEFILESIZE:
            if size < fileData.MAXDOWNLOADABLEFILESIZE:
                if not (StringValidationUtil.getInstance().isValidRequired(fileName, fileData.MINLEN, fileData.MAXLEN)):
                    stringBuffer.append("File Name must be more than ")
                    stringBuffer.appendint(int(fileData.MINLEN))
                    stringBuffer.append(" and less than ")
                    stringBuffer.appendint(int(fileData.MAXLEN))
                    stringBuffer.append(" characters in length: ")
                    stringBuffer.append(fileName)
                    stringBuffer.append("<br/>")
                else:
                    pass
            else:
                stringBuffer.append("File Is Not The Right Size. ")
                stringBuffer.appendint(int(fileData.MINDOWNLOADABLEFILESIZE))
                stringBuffer.append("< >")
                stringBuffer.appendint(int(fileData.MAXDOWNLOADABLEFILESIZE))
                stringBuffer.append("<br/>")

    def validationInfo(self, *args):
        implementation = __class__.__dict__.get("validationInfo_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().validationInfo(*args)
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return java_super_call(super(), "getTransformInfoInterface")
# from java.util.HashMap import HashMap
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.business.user.commerce.inventory.item.BasicItemValidation import BasicItemValidation
# from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
# from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
# from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItemValidation import DownloadableItemValidation
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
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.apache.commons.fileupload.FileItem import FileItem
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


