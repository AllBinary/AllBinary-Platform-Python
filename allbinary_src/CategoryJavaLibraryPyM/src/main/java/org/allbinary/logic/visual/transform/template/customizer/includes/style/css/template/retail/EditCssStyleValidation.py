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
# package org.allbinary.logic.visual.transform.template.customizer.includes.style.css.template.retail

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.allbinary.logic.visual.transform.template.customizer.includes.style.css.template.retail.CssStyleValidation import CssStyleValidation


class EditCssStyleValidation(*java_bases(CssStyleValidation, ValidationInterface, DomNodeInterface)):

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self.__jconstructor1(*args)

    def __jconstructor1(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)):
            self._constructor1_1(*args)
        else:
            self._constructor1_2(*args)
    

    def _constructor0(self) -> None:
        super().__init__()
    

    def _constructor1_1(self, document: Document) -> None:
        from org.w3c.dom.Document import Document
        super().__init__(document)
    

    def _constructor1_2(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        super().__init__(hashMap)
    

    def isValid(self) -> bool:
        return super().isValid()
    

    def validationInfo(self) -> str:
        return super().validationInfo()
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.dhtml.style.StyleData import StyleData
        from org.allbinary.logic.visual.dhtml.style.StylesData import StylesData
        from org.allbinary.logic.visual.dhtml.style.color.ColorsView import ColorsView
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(StylesData.getInstance().NAME)
        styleNode: Node = document.createElement(StyleData.getInstance().NAME)
        node.appendChild(styleNode)
        styleNode.appendChild(ColorsView().toXmlNode(document))
        size: int = self.cssStyleElementVector.size()
        for i in range(0, size):
            styleDomNodeInterface: DomNodeInterface = self.cssStyleElementVector.get(i)
            styleNode.appendChild(styleDomNodeInterface.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.logic.visual.dhtml.style.StyleData import StyleData
# from org.allbinary.logic.visual.dhtml.style.StylesData import StylesData
# from org.allbinary.logic.visual.dhtml.style.color.ColorsView import ColorsView
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


