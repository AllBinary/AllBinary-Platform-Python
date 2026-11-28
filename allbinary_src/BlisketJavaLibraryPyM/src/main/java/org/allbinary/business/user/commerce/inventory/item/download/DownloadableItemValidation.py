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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.control.validate.Validation import Validation


@java_inherited_overloads
class DownloadableItemValidation(Validation):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("downloadableItem", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "downloadableItem" not in vars(self): self.downloadableItem: DownloadableItem = None
    

    def __init__(self, downloadableItem: DownloadableItem) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.downloadableItem = downloadableItem
    

    def isValid(self) -> bool:
        from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if self.downloadableItem.getId() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getId()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getId()) > AbSqlData.MAXNUM:
                return False
            if self.downloadableItem.getId() is not None and not (StringValidationUtil.getInstance().isNumber(self.downloadableItem.getId())):
                return False
            if self.downloadableItem.getSystem() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getSystem()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getSystem()) > AbSqlData.MAXSTRING:
                return False
            if self.downloadableItem.getPlatform() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getPlatform()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getPlatform()) > AbSqlData.MAXSTRING:
                return False
            if self.downloadableItem.getSpecialName() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getSpecialName()) < 0 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getSpecialName()) > AbSqlData.MAXSTRING:
                return False
            if self.downloadableItem.getVersion() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getVersion()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getVersion()) > AbSqlData.MAXSTRING:
                return False
            if self.downloadableItem.getChanges() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getChanges()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getChanges()) > AbSqlData.MAXBLOB:
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            if self.downloadableItem.getId() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getId()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getId()) > AbSqlData.MAXNUM:
                stringBuffer.append("Id is invalid. Must be number < ")
                stringBuffer.appendint(int(AbSqlData.MAXNUM))
                stringBuffer.append(" and > 0 digits.<br/>")
            if self.downloadableItem.getId() is not None and not (StringValidationUtil.getInstance().isNumber(self.downloadableItem.getId())):
                stringBuffer.append("Id is invalid. Must be > 0.<br/>")
            if self.downloadableItem.getSystem() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getSystem()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getSystem()) > AbSqlData.MAXSTRING:
                stringBuffer.append("System value is invalid. Must be < ")
                stringBuffer.appendint(int(AbSqlData.MAXSTRING))
                stringBuffer.append(" and > 0 characters long.<br/>")
            if self.downloadableItem.getPlatform() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getPlatform()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getPlatform()) > AbSqlData.MAXSTRING:
                stringBuffer.append("Platform value is invalid. Must be < ")
                stringBuffer.appendint(int(AbSqlData.MAXSTRING))
                stringBuffer.append(" and > 0 characters long.<br/>")
            if self.downloadableItem.getSpecialName() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getSpecialName()) < 0 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getSpecialName()) > AbSqlData.MAXSTRING:
                stringBuffer.append("Special Name value is invalid. Must be < ")
                stringBuffer.appendint(int(AbSqlData.MAXSTRING))
                stringBuffer.append(" and > 0 characters long.<br/>")
            if self.downloadableItem.getVersion() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getVersion()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getVersion()) > AbSqlData.MAXSTRING:
                stringBuffer.append("Version value is invalid. Must be < ")
                stringBuffer.appendint(int(AbSqlData.MAXSTRING))
                stringBuffer.append(" and > 0 characters long.<br/>")
            if self.downloadableItem.getChanges() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getChanges()) < 0 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.downloadableItem.getChanges()) > AbSqlData.MAXBLOB:
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


