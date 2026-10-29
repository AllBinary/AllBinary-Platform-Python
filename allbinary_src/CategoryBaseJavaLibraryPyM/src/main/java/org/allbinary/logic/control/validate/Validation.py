# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.logic.control.validate

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface


class Validation(ValidationInterface):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def isValid(self) -> bool:
        raise RuntimeError()
    

    # throws Exception
    def toValidationInfoNode(self, document: Document) -> Node:
        raise RuntimeError()
    

    # throws Exception
    def toValidationInfoDoc(self) -> Document:
        raise RuntimeError()
    

    # throws Exception
    def validationInfo(self) -> str:
        raise RuntimeError()
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


