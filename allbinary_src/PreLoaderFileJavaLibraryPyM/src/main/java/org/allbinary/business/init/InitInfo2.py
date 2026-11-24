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
# package org.allbinary.business.init

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class InitInfo2:
    instance: InitInfo2 = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.io.file.directory.Directory import Directory
        self.directory: Directory = Directory.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> InitInfo2:
        return InitInfo2.instance
    

    def isTestHtmlPathValid(self, value: AbPath) -> bool:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return self.directory.create(value)
    

    def isMainPathValid(self, value: AbPath) -> bool:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return self.directory.create(value)
# from org.allbinary.logic.io.file.directory.Directory import Directory
# from org.allbinary.logic.io.path.AbPath import AbPath


def _InitInfo2_instance() -> object:
    return InitInfo2()

lazy_static(InitInfo2, "instance", _InitInfo2_instance)

