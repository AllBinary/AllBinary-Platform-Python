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
# package org.allbinary.logic.visual.transform.info.objectConfig

from __future__ import annotations

from org.allbinary.data.tree.dom.document.mapping.DomDocumentMappingInterface import DomDocumentMappingInterface


# Java interface
class TransformInfoObjectConfigInterface(DomDocumentMappingInterface):
    

    def containsView(self, transformInfoInterface: TransformInfoInterface) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def getName(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def getTransformsGroup(self, group: str) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getTransforms(self) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getParentTransforms(self) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getGroupTransforms(self) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getOutputTypeName(self) -> str:
        raise NotImplementedError()
    

    def setOutputTypeName(self, value: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def getInputOutputTypeName(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def getInputOutputTypeFile(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def getImportUriPath(self) -> str:
        raise NotImplementedError()
    

    def toString(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


