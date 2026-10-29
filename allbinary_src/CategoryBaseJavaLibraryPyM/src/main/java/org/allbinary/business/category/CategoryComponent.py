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
# package org.allbinary.business.category

from __future__ import annotations

from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
from org.allbinary.business.category.CategoryView import CategoryView


class CategoryComponent(CategoryView, TransformInterface):

    def _init_fields(self) -> None:
        self.NO_TYPE: int = 0
    

    def __init__(self, categoryInterface: CategoryInterface) -> None:
        super().__init__(categoryInterface)
        self._init_fields()
    

    def getTypeId(self) -> int:
        return self.NO_TYPE
    

    def getTransformDocumentInterface(self) -> TransformDocumentInterface:
        return None
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        return None
    

    def setTransformDocumentInterface(self, viewDocumentInterface: TransformDocumentInterface) -> None:
        pass
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        from org.allbinary.business.category.CategoryView import CategoryView
        document: Document = DomDocumentHelper.create()
        document.appendChild(CategoryView(self.getCategoryInterface()).toXmlNode(document))
        return document
    

    # throws Exception
    def view(self) -> str:
        return None
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document


