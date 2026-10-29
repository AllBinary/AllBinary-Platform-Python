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
# package org.allbinary.business.user.commerce.inventory.item.download

from __future__ import annotations

from org.allbinary.logic.control.validate.Validation import Validation


class DownloadableItemValidation(Validation):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.downloadableItem: DownloadableItem = None
    

    def __init__(self, downloadableItem: DownloadableItem) -> None:
        super().__init__()
        self._init_fields()
        self.downloadableItem = downloadableItem
    

    def isValid(self) -> bool:
        try:
            if self.downloadableItem.getId() is None or self.downloadableItem.getId().length() < 1 or self.downloadableItem.getId().length() > AbSqlData.MAXNUM:
                return False
            if self.downloadableItem.getId() is not None and not StringValidationUtil.getInstance().isNumber(self.downloadableItem.getId()):
                return False
            if self.downloadableItem.getSystem() is None or self.downloadableItem.getSystem().length() < 1 or self.downloadableItem.getSystem().length() > AbSqlData.MAXSTRING:
                return False
            if self.downloadableItem.getPlatform() is None or self.downloadableItem.getPlatform().length() < 1 or self.downloadableItem.getPlatform().length() > AbSqlData.MAXSTRING:
                return False
            if self.downloadableItem.getSpecialName() is None or self.downloadableItem.getSpecialName().length() < 0 or self.downloadableItem.getSpecialName().length() > AbSqlData.MAXSTRING:
                return False
            if self.downloadableItem.getVersion() is None or self.downloadableItem.getVersion().length() < 1 or self.downloadableItem.getVersion().length() > AbSqlData.MAXSTRING:
                return False
            if self.downloadableItem.getChanges() is None or self.downloadableItem.getChanges().length() < 1 or self.downloadableItem.getChanges().length() > AbSqlData.MAXBLOB:
                return False
            if self.downloadableItem.getSize() is None:
                return False
            else:
                size: str = str(self.downloadableItem.getSize())
                if len(size) < 1 or len(size) > AbSqlData.MAXNUM:
                    return False
            if self.downloadableItem.getValidTime() is None:
                return False
            else:
                size: str = str(self.downloadableItem.getValidTime())
                if len(size) < 1 or len(size) > AbSqlData.MAXNUM:
                    return False
            if self.downloadableItem.getRetries() is None:
                return False
            else:
                size: str = str(self.downloadableItem.getRetries())
                if len(size) < 1 or len(size) > AbSqlData.MAXNUM:
                    return False
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            if self.downloadableItem.getId() is None or self.downloadableItem.getId().length() < 1 or self.downloadableItem.getId().length() > AbSqlData.MAXNUM:
                stringBuffer.append("Id is invalid. Must be number < ")
                stringBuffer.appendint(int(AbSqlData.MAXNUM))
                stringBuffer.append(" and > 0 digits.<br/>")
            if self.downloadableItem.getId() is not None and not StringValidationUtil.getInstance().isNumber(self.downloadableItem.getId()):
                stringBuffer.append("Id is invalid. Must be > 0.<br/>")
            if self.downloadableItem.getSystem() is None or self.downloadableItem.getSystem().length() < 1 or self.downloadableItem.getSystem().length() > AbSqlData.MAXSTRING:
                stringBuffer.append("System value is invalid. Must be < ")
                stringBuffer.appendint(int(AbSqlData.MAXSTRING))
                stringBuffer.append(" and > 0 characters long.<br/>")
            if self.downloadableItem.getPlatform() is None or self.downloadableItem.getPlatform().length() < 1 or self.downloadableItem.getPlatform().length() > AbSqlData.MAXSTRING:
                stringBuffer.append("Platform value is invalid. Must be < ")
                stringBuffer.appendint(int(AbSqlData.MAXSTRING))
                stringBuffer.append(" and > 0 characters long.<br/>")
            if self.downloadableItem.getSpecialName() is None or self.downloadableItem.getSpecialName().length() < 0 or self.downloadableItem.getSpecialName().length() > AbSqlData.MAXSTRING:
                stringBuffer.append("Special Name value is invalid. Must be < ")
                stringBuffer.appendint(int(AbSqlData.MAXSTRING))
                stringBuffer.append(" and > 0 characters long.<br/>")
            if self.downloadableItem.getVersion() is None or self.downloadableItem.getVersion().length() < 1 or self.downloadableItem.getVersion().length() > AbSqlData.MAXSTRING:
                stringBuffer.append("Version value is invalid. Must be < ")
                stringBuffer.appendint(int(AbSqlData.MAXSTRING))
                stringBuffer.append(" and > 0 characters long.<br/>")
            if self.downloadableItem.getChanges() is None or self.downloadableItem.getChanges().length() < 0 or self.downloadableItem.getChanges().length() > AbSqlData.MAXBLOB:
                stringBuffer.append("Changes value is invalid. Must be < ")
                stringBuffer.appendint(int(AbSqlData.MAXBLOB))
                stringBuffer.append(" and >= 0 characters long.<br/>")
            if self.downloadableItem.getSize() is None:
                stringBuffer.append("File Size is null")
            else:
                size: str = str(self.downloadableItem.getSize())
                if len(size) < 1 or len(size) > AbSqlData.MAXNUM:
                    stringBuffer.append("File Size is invalid. Must be number < ")
                    stringBuffer.appendint(int(AbSqlData.MAXNUM))
                    stringBuffer.append(" and > 0 digits.<br/>")
            if self.downloadableItem.getValidTime() is None:
                stringBuffer.append("Valid Time is null")
            else:
                size: str = str(self.downloadableItem.getValidTime())
                if len(size) < 1 or len(size) > AbSqlData.MAXNUM:
                    stringBuffer.append("Valid Time is invalid. Must be number < ")
                    stringBuffer.appendint(int(AbSqlData.MAXNUM))
                    stringBuffer.append(" and > 0 digits.<br/>")
            if self.downloadableItem.getRetries() is None:
                stringBuffer.append("Retries is null")
            else:
                size: str = str(self.downloadableItem.getRetries())
                if len(size) < 1 or len(size) > AbSqlData.MAXNUM:
                    stringBuffer.append("Retries is invalid. Must be number < ")
                    stringBuffer.appendint(int(AbSqlData.MAXNUM))
                    stringBuffer.append(" and > 0 digits.<br/>")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


