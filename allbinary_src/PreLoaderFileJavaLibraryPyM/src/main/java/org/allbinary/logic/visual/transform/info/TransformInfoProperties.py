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



class TransformInfoProperties:

    def _init_fields(self) -> None:
        self.name: str = None
        self.label: str = None
        self.description: str = None
        self.objectFileName: str = None
        self.objectConfigFileName: str = None
        self.templateFileName: str = None
    

    def __init__(self, name: str, label: str, description: str, objectFileName: str, objectConfigFileName: str, templateFileName: str) -> None:
        self._init_fields()
        self.name = name
        self.label = label
        self.description = description
        self.objectFileName = objectFileName
        self.templateFileName = templateFileName
        self.objectConfigFileName = objectConfigFileName
    

    def setName(self, value: str) -> None:
        self.name = value
    

    def setDescription(self, value: str) -> None:
        self.description = value
    

    def setViewFile(self, value: str) -> None:
        self.objectFileName = value
    

    def setTemplateFile(self, value: str) -> None:
        self.templateFileName = value
    

    def setObjectConfigFile(self, value: str) -> None:
        self.objectConfigFileName = value
    

    def getName(self) -> str:
        return self.name
    

    def getLabel(self) -> str:
        return self.label
    

    def getDescription(self) -> str:
        return self.description
    

    def getViewFile(self) -> str:
        return self.objectFileName
    

    def getTemplateFile(self) -> str:
        return self.templateFileName
    

    def getObjectConfigFile(self) -> str:
        return self.objectConfigFileName


