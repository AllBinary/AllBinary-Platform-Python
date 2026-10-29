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
# package org.allbinary.logic.control.validate

from __future__ import annotations



# Java interface
class ValidationInterface:
    

    # throws Exception
    def isValid(self) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def toValidationInfoNode(self, document: Document) -> Node:
        raise NotImplementedError()
    

    # throws Exception
    def toValidationInfoDoc(self) -> Document:
        raise NotImplementedError()
    

    # throws Exception
    def validationInfo(self) -> str:
        raise NotImplementedError()
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


