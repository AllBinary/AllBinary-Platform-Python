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
# package org.allbinary.logic.visual.theme

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.Validation import Validation


class ThemesValidation(Validation, DomNodeInterface):

    def _init_fields(self) -> None:
        self.themeVector: BasicArrayList = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        super().__init__()
        self._init_fields()
        self.themeVector = BasicArrayListD()
    

    def _constructor1(self, node: Node) -> None:
        super().__init__()
        self._init_fields()
    

    def _constructor1(self, hashMap: dict) -> None:
        super().__init__()
        self._init_fields()
    

    def isValid(self) -> bool:
        return True
    

    def validationInfo(self) -> str:
        return None
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.theme.ThemesData import ThemesData
        node: Node = document.createElement(ThemesData.getInstance().NAME)
        size: int = self.themeVector.size()
        for i in range(0, size):
            themeDomNodeInterface: DomNodeInterface = self.themeVector.get(i)
            node.appendChild(themeDomNodeInterface.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


