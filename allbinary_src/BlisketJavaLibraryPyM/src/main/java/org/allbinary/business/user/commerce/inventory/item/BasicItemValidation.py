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
# package org.allbinary.business.user.commerce.inventory.item

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.logic.control.validate.Validation import Validation


@java_inherited_overloads
class BasicItemValidation(Validation):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("MAXWEIGHT", 0)
        vars(self).setdefault("MAXPRICE", 0)
        vars(self).setdefault("itemInterface", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.MAXWEIGHT: int = 14
        self.MAXPRICE: int = 14
        if "itemInterface" not in vars(self): self.itemInterface: ItemInterface = None
    

    def __init__(self, itemInterface: ItemInterface) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.itemInterface = itemInterface
    

    def isValid(self) -> bool:
        from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if self.itemInterface.getId() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getId()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getId()) > AbSqlData.MAXNUM:
                return False
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if self.itemInterface.getId() is not None and not (stringValidationUtil.isNumber(self.itemInterface.getId())):
                return False
            if self.itemInterface.getNumber() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getNumber()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getNumber()) > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getNumber() is not None and not (stringValidationUtil.isNumber(self.itemInterface.getNumber())):
                return False
            if self.itemInterface.getInBaskets() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getInBaskets()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getInBaskets()) > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getInBaskets() is not None and not (stringValidationUtil.isNumber(self.itemInterface.getInBaskets())):
                return False
            if self.itemInterface.getWeight() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getWeight()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getWeight()) > self.MAXWEIGHT:
                return False
            if self.itemInterface.getWeight() is not None and not (stringValidationUtil.isNumber(self.itemInterface.getWeight())):
                return False
            if self.itemInterface.getEnabled() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getEnabled()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getEnabled()) > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getNewOrUsed() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getNewOrUsed()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getNewOrUsed()) > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getSummary() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getSummary()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getSummary()) > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getDescription() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getDescription()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getDescription()) > AbSqlData.MAXBLOB:
                return False
            if self.itemInterface.getKeywords() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getKeywords()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getKeywords()) > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getCategory() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getCategory()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getCategory()) > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getType() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getType()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getType()) > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getPrice() is None or not (java_predicate(self.itemInterface.getPrice(), "isValid")):
                return False
            if self.itemInterface.getCustoms() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getCustoms()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getCustoms()) > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getDownloads() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getDownloads()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getDownloads()) > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getGroups() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getGroups()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getGroups()) > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getOptions() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getOptions()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getOptions()) > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getPermissions() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getPermissions()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getPermissions()) > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getSpecials() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getSpecials()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getSpecials()) > AbSqlData.MAXNUM:
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
            if self.itemInterface.getId() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getId()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getId()) > AbSqlData.MAXNUM:
                stringBuffer.append("Id is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if self.itemInterface.getId() is not None and not (stringValidationUtil.isNumber(self.itemInterface.getId())):
                stringBuffer.append("Id is invalid. Must be > 0.<br />")
            if self.itemInterface.getNumber() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getNumber()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getNumber()) > AbSqlData.MAXNUM:
                stringBuffer.append("Number of items is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getNumber() is not None and not (stringValidationUtil.isNumber(self.itemInterface.getNumber())):
                stringBuffer.append("Number of items value is not a valid number.<br />")
            if self.itemInterface.getInBaskets() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getInBaskets()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getInBaskets()) > AbSqlData.MAXNUM:
                stringBuffer.append("Number in baskets is invalid. Must be < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getInBaskets() is not None and not (stringValidationUtil.isNumber(self.itemInterface.getInBaskets())):
                stringBuffer.append("In Baskets value is not a valid number.<br />")
            if self.itemInterface.getWeight() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getWeight()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getWeight()) > self.MAXWEIGHT:
                stringBuffer.append("Weight value is invalid. Must be < " + str(self.MAXWEIGHT) + " and > 0 digits.<br />")
            if self.itemInterface.getWeight() is not None and not (stringValidationUtil.isNumber(self.itemInterface.getWeight())):
                stringBuffer.append("Weight value is not a valid number.<br />")
            if self.itemInterface.getEnabled() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getEnabled()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getEnabled()) > AbSqlData.MAXSTRING:
                stringBuffer.append("For Sale value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getNewOrUsed() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getNewOrUsed()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getNewOrUsed()) > AbSqlData.MAXSTRING:
                stringBuffer.append("New Or Used value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getSummary() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getSummary()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getSummary()) > AbSqlData.MAXSTRING:
                stringBuffer.append("Summary value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getDescription() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getDescription()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getDescription()) > AbSqlData.MAXBLOB:
                stringBuffer.append("Description value is invalid. Must be < " + str(AbSqlData.MAXBLOB) + " and > 0 characters long.<br />")
            if self.itemInterface.getKeywords() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getKeywords()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getKeywords()) > AbSqlData.MAXSTRING:
                stringBuffer.append("Keywords value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getCategory() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getCategory()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getCategory()) > AbSqlData.MAXSTRING:
                stringBuffer.append("Category value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getType() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getType()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getType()) > AbSqlData.MAXSTRING:
                stringBuffer.append("Type value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getPrice() is None or not (java_predicate(self.itemInterface.getPrice(), "isValid")):
                stringBuffer.append("Price value is invalid. Must be < " + str(self.MAXPRICE) + " and > 0 in length.<br />")
            if self.itemInterface.getCustoms() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getCustoms()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getCustoms()) > AbSqlData.MAXNUM:
                stringBuffer.append("Custom items value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getDownloads() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getDownloads()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getDownloads()) > AbSqlData.MAXNUM:
                stringBuffer.append("Downloadable item value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getGroups() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getGroups()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getGroups()) > AbSqlData.MAXNUM:
                stringBuffer.append("Group item value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getOptions() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getOptions()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getOptions()) > AbSqlData.MAXNUM:
                stringBuffer.append("Option item value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getPermissions() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getPermissions()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getPermissions()) > AbSqlData.MAXNUM:
                stringBuffer.append("Permission item value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getSpecials() is None or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getSpecials()) < 1 or __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(self.itemInterface.getSpecials()) > AbSqlData.MAXNUM:
                stringBuffer.append("Special item value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
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


