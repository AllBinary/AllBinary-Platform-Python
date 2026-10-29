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
# package org.allbinary.logic.visual.dhtml.style.css.property.font

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.allbinary.logic.visual.dhtml.style.css.property.font.FontFamilyView import FontFamilyView


class FontFamilyValidation(FontFamilyView, ValidationInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        super().__init__()
        self._init_fields()
    

    def _constructor1(self, node: Node) -> None:
        super().__init__(node)
        self._init_fields()
    

    # throws Exception
    def isValid(self) -> bool:
        try:
            valid: bool = True
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("FontFamilyValidation", self, self.commonStrings.IS_VALID)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("CssValidation: " + str(valid), self, self.commonStrings.IS_VALID)
            return valid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate data", self, self.commonStrings.IS_VALID, e)
            return False
    

    # throws Exception
    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Css Font Family Property Validation Error")
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


