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
# package org.allbinary.logic.visual.transform

from __future__ import annotations

from org.allbinary.data.tree.dom.document.mapping.DomDocumentMappingInterface import DomDocumentMappingInterface
from org.allbinary.logic.visual.transform.info.CompositeTransformInfoInterface import CompositeTransformInfoInterface


# Java interface
class TransformInterface(DomDocumentMappingInterface, CompositeTransformInfoInterface):
    

    def getTypeId(self) -> int:
        raise NotImplementedError()
    

    def setTransformDocumentInterface(self, viewDocumentInterface: TransformDocumentInterface) -> None:
        raise NotImplementedError()
    

    def getTransformDocumentInterface(self) -> TransformDocumentInterface:
        raise NotImplementedError()
    

    # throws Exception
    def view(self) -> str:
        raise NotImplementedError()
from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface


