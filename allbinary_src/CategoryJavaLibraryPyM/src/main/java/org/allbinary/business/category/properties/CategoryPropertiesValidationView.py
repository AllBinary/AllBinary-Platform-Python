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
# package org.allbinary.business.category.properties

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.allbinary.business.category.properties.CategoryPropertiesView import CategoryPropertiesView


class CategoryPropertiesValidationView(CategoryPropertiesView, ValidationInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, categoryPropertiesInterface: CategoryPropertiesInterface) -> None:
        super().__init__(categoryPropertiesInterface)
        self._init_fields()
    

    # throws Exception
    def isValid(self) -> bool:
        return self.categoryPropertiesInterface.isValid()
    

    # throws Exception
    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.categoryPropertiesInterface.validationInfo())
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation info error", self, "validationInfo()", e)
            return "Error Validating Data"
    

    # throws Exception
    def toValidationInfoDoc(self) -> Document:
        return None
    

    # throws Exception
    def toValidationInfoNode(self, document: Document) -> Node:
        return None
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


