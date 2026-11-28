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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
from org.allbinary.business.category.CategoryView import CategoryView


@java_inherited_overloads
class CategoryComponent(*java_bases(CategoryView, TransformInterface)):
    def _java_defaults(self):
        vars(self).setdefault("NO_TYPE", 0)

    def _init_fields(self) -> None:
        self.NO_TYPE: int = 0
    

    def __init__(self, categoryInterface: CategoryInterface) -> None:
        __class__._java_defaults(self)
        super().__init__(categoryInterface)
        __class__._init_fields(self)
    

    def getTypeId(self) -> int:
        return self.NO_TYPE
    

    def getTransformDocumentInterface(self) -> TransformDocumentInterface:
        from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
        return None
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return None
    

    def setTransformDocumentInterface(self, viewDocumentInterface: TransformDocumentInterface) -> None:
        from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
        pass
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        from org.allbinary.business.category.CategoryView import CategoryView
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.w3c.dom.Document import Document
        document: Document = DomDocumentHelper.create()
        document.appendChild(CategoryView(self.getCategoryInterface()).toXmlNode(document))
        return document
    

    # throws Exception
    def view(self) -> str:
        return None
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Document import Document


