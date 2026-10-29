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

from org.allbinary.logic.control.validate.Validation import Validation


class BasicItemValidation(Validation):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.MAXWEIGHT: int = 14
        self.MAXPRICE: int = 14
        self.itemInterface: ItemInterface = None
    

    def __init__(self, itemInterface: ItemInterface) -> None:
        super().__init__()
        self._init_fields()
        self.itemInterface = itemInterface
    

    def isValid(self) -> bool:
        try:
            if self.itemInterface.getId() is None or self.itemInterface.getId().length() < 1 or self.itemInterface.getId().length() > AbSqlData.MAXNUM:
                return False
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if self.itemInterface.getId() is not None and not stringValidationUtil.isNumber(self.itemInterface.getId()):
                return False
            if self.itemInterface.getNumber() is None or self.itemInterface.getNumber().length() < 1 or self.itemInterface.getNumber().length() > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getNumber() is not None and not stringValidationUtil.isNumber(self.itemInterface.getNumber()):
                return False
            if self.itemInterface.getInBaskets() is None or self.itemInterface.getInBaskets().length() < 1 or self.itemInterface.getInBaskets().length() > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getInBaskets() is not None and not stringValidationUtil.isNumber(self.itemInterface.getInBaskets()):
                return False
            if self.itemInterface.getWeight() is None or self.itemInterface.getWeight().length() < 1 or self.itemInterface.getWeight().length() > self.MAXWEIGHT:
                return False
            if self.itemInterface.getWeight() is not None and not stringValidationUtil.isNumber(self.itemInterface.getWeight()):
                return False
            if self.itemInterface.getEnabled() is None or self.itemInterface.getEnabled().length() < 1 or self.itemInterface.getEnabled().length() > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getNewOrUsed() is None or self.itemInterface.getNewOrUsed().length() < 1 or self.itemInterface.getNewOrUsed().length() > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getSummary() is None or self.itemInterface.getSummary().length() < 1 or self.itemInterface.getSummary().length() > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getDescription() is None or self.itemInterface.getDescription().length() < 1 or self.itemInterface.getDescription().length() > AbSqlData.MAXBLOB:
                return False
            if self.itemInterface.getKeywords() is None or self.itemInterface.getKeywords().length() < 1 or self.itemInterface.getKeywords().length() > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getCategory() is None or self.itemInterface.getCategory().length() < 1 or self.itemInterface.getCategory().length() > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getType() is None or self.itemInterface.getType().length() < 1 or self.itemInterface.getType().length() > AbSqlData.MAXSTRING:
                return False
            if self.itemInterface.getPrice() is None or not self.itemInterface.getPrice().isValid():
                return False
            if self.itemInterface.getCustoms() is None or self.itemInterface.getCustoms().length() < 1 or self.itemInterface.getCustoms().length() > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getDownloads() is None or self.itemInterface.getDownloads().length() < 1 or self.itemInterface.getDownloads().length() > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getGroups() is None or self.itemInterface.getGroups().length() < 1 or self.itemInterface.getGroups().length() > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getOptions() is None or self.itemInterface.getOptions().length() < 1 or self.itemInterface.getOptions().length() > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getPermissions() is None or self.itemInterface.getPermissions().length() < 1 or self.itemInterface.getPermissions().length() > AbSqlData.MAXNUM:
                return False
            if self.itemInterface.getSpecials() is None or self.itemInterface.getSpecials().length() < 1 or self.itemInterface.getSpecials().length() > AbSqlData.MAXNUM:
                return False
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            if self.itemInterface.getId() is None or self.itemInterface.getId().length() < 1 or self.itemInterface.getId().length() > AbSqlData.MAXNUM:
                stringBuffer.append("Id is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if self.itemInterface.getId() is not None and not stringValidationUtil.isNumber(self.itemInterface.getId()):
                stringBuffer.append("Id is invalid. Must be > 0.<br />")
            if self.itemInterface.getNumber() is None or self.itemInterface.getNumber().length() < 1 or self.itemInterface.getNumber().length() > AbSqlData.MAXNUM:
                stringBuffer.append("Number of items is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getNumber() is not None and not stringValidationUtil.isNumber(self.itemInterface.getNumber()):
                stringBuffer.append("Number of items value is not a valid number.<br />")
            if self.itemInterface.getInBaskets() is None or self.itemInterface.getInBaskets().length() < 1 or self.itemInterface.getInBaskets().length() > AbSqlData.MAXNUM:
                stringBuffer.append("Number in baskets is invalid. Must be < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getInBaskets() is not None and not stringValidationUtil.isNumber(self.itemInterface.getInBaskets()):
                stringBuffer.append("In Baskets value is not a valid number.<br />")
            if self.itemInterface.getWeight() is None or self.itemInterface.getWeight().length() < 1 or self.itemInterface.getWeight().length() > self.MAXWEIGHT:
                stringBuffer.append("Weight value is invalid. Must be < " + str(self.MAXWEIGHT) + " and > 0 digits.<br />")
            if self.itemInterface.getWeight() is not None and not stringValidationUtil.isNumber(self.itemInterface.getWeight()):
                stringBuffer.append("Weight value is not a valid number.<br />")
            if self.itemInterface.getEnabled() is None or self.itemInterface.getEnabled().length() < 1 or self.itemInterface.getEnabled().length() > AbSqlData.MAXSTRING:
                stringBuffer.append("For Sale value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getNewOrUsed() is None or self.itemInterface.getNewOrUsed().length() < 1 or self.itemInterface.getNewOrUsed().length() > AbSqlData.MAXSTRING:
                stringBuffer.append("New Or Used value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getSummary() is None or self.itemInterface.getSummary().length() < 1 or self.itemInterface.getSummary().length() > AbSqlData.MAXSTRING:
                stringBuffer.append("Summary value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getDescription() is None or self.itemInterface.getDescription().length() < 1 or self.itemInterface.getDescription().length() > AbSqlData.MAXBLOB:
                stringBuffer.append("Description value is invalid. Must be < " + str(AbSqlData.MAXBLOB) + " and > 0 characters long.<br />")
            if self.itemInterface.getKeywords() is None or self.itemInterface.getKeywords().length() < 1 or self.itemInterface.getKeywords().length() > AbSqlData.MAXSTRING:
                stringBuffer.append("Keywords value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getCategory() is None or self.itemInterface.getCategory().length() < 1 or self.itemInterface.getCategory().length() > AbSqlData.MAXSTRING:
                stringBuffer.append("Category value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getType() is None or self.itemInterface.getType().length() < 1 or self.itemInterface.getType().length() > AbSqlData.MAXSTRING:
                stringBuffer.append("Type value is invalid. Must be < " + str(AbSqlData.MAXSTRING) + " and > 0 characters long.<br />")
            if self.itemInterface.getPrice() is None or not self.itemInterface.getPrice().isValid():
                stringBuffer.append("Price value is invalid. Must be < " + str(self.MAXPRICE) + " and > 0 in length.<br />")
            if self.itemInterface.getCustoms() is None or self.itemInterface.getCustoms().length() < 1 or self.itemInterface.getCustoms().length() > AbSqlData.MAXNUM:
                stringBuffer.append("Custom items value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getDownloads() is None or self.itemInterface.getDownloads().length() < 1 or self.itemInterface.getDownloads().length() > AbSqlData.MAXNUM:
                stringBuffer.append("Downloadable item value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getGroups() is None or self.itemInterface.getGroups().length() < 1 or self.itemInterface.getGroups().length() > AbSqlData.MAXNUM:
                stringBuffer.append("Group item value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getOptions() is None or self.itemInterface.getOptions().length() < 1 or self.itemInterface.getOptions().length() > AbSqlData.MAXNUM:
                stringBuffer.append("Option item value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getPermissions() is None or self.itemInterface.getPermissions().length() < 1 or self.itemInterface.getPermissions().length() > AbSqlData.MAXNUM:
                stringBuffer.append("Permission item value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
            if self.itemInterface.getSpecials() is None or self.itemInterface.getSpecials().length() < 1 or self.itemInterface.getSpecials().length() > AbSqlData.MAXNUM:
                stringBuffer.append("Special item value is invalid. Must be number < " + str(AbSqlData.MAXNUM) + " and > 0 digits.<br />")
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


