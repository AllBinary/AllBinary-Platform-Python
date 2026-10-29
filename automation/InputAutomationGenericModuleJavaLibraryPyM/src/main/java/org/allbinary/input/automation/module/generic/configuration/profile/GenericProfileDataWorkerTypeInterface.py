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
# package org.allbinary.input.automation.module.generic.configuration.profile

from __future__ import annotations



# Java interface
class GenericProfileDataWorkerTypeInterface:
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def setName(self, name: str) -> None:
        raise NotImplementedError()
    

    def toString(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.toString()
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        raise NotImplementedError()
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


