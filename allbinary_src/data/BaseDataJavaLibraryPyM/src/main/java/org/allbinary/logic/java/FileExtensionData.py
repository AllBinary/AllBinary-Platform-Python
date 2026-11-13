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
# package org.allbinary.logic.java

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class FileExtensionData:
    instance: FileExtensionData = None

    def _init_fields(self) -> None:
        self.DOT_JAVA_SOURCE: str = ".java"
        self.JAVA_SOURCE: str = "java"
    

    @staticmethod
    def getInstance() -> FileExtensionData:
        return FileExtensionData.instance
    

    def __init__(self) -> None:
        self._init_fields()


def _FileExtensionData_instance() -> object:
    return FileExtensionData()

lazy_static(FileExtensionData, "instance", _FileExtensionData_instance)

