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
# package org.allbinary.logic.visual.transform.info

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


# Java interface
class TransformInfoInterface(TableMappingInterface):
    

    def log(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def override(self, hashMap: dict) -> None:
        raise NotImplementedError()
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def setStoreName(self, value: str) -> None:
        raise NotImplementedError()
    

    def getStoreName(self) -> str:
        raise NotImplementedError()
    

    def getObjectFile(self) -> str:
        raise NotImplementedError()
    

    def getObject(self) -> object:
        raise NotImplementedError()
    

    # throws Exception
    def getTemplateFilePath(self) -> AbPath:
        raise NotImplementedError()
    

    def getTemplateFile(self) -> str:
        raise NotImplementedError()
    

    def getTemplate(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def getDataFilePath(self) -> AbPath:
        raise NotImplementedError()
    

    def getDataFile(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def getDataDocument(self) -> Document:
        raise NotImplementedError()
    

    def setName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setObjectFile(self, value: str) -> None:
        raise NotImplementedError()
    

    def setObject(self, anyType: object) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def setObjectConfigInterface(self, transformInfoObjectConfigInterface: TransformInfoObjectConfigInterface) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def getObjectConfigInterface(self) -> TransformInfoObjectConfigInterface:
        raise NotImplementedError()
    

    def setTemplateFile(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTemplate(self, value: str) -> None:
        raise NotImplementedError()
    

    def setDataFile(self, value: str) -> None:
        raise NotImplementedError()
    

    def setData(self, value: str) -> None:
        raise NotImplementedError()
    

    def setChild(self) -> None:
        raise NotImplementedError()
    

    def isChild(self) -> bool:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigInterface import TransformInfoObjectConfigInterface
from org.w3c.dom.Document import Document


