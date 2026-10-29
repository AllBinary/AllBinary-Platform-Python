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
# package org.allbinary.logic.io.file

from __future__ import annotations

from org.allbinary.data.resource.ResourceUtil import ResourceUtil


class FileFactory:
    SINGLETON: FileFactory = None

    def _init_fields(self) -> None:
        self.context: Context = None
    

    def __init__(self, context: Context) -> None:
        self._init_fields()
        self.context = context
    

    @staticmethod
    def getInstance() -> FileFactory:
        return FileFactory.SINGLETON
    

    # throws Exception
    def isFile(self, path: str) -> bool:
        try:
            self.context.openFileInput(path)
            return True
        except FileNotFoundException as e:
            return False
    

    def getContext(self) -> Context:
        return self.context
    

    # throws Exception
    def getFile(self, filePath: str) -> AbFile:
        from org.allbinary.logic.io.file.AbFile import AbFile
        return AbFile.createAbFileFromRawPath(filePath)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, file: AbFile, childFilePath: str) -> AbFile:
        from org.allbinary.logic.io.file.AbFile import AbFile
        return AbFile.createAbFileWithChild(file, childFilePath)
# from java.io.FileNotFoundException import FileNotFoundException
from android.content.Context import Context


FileFactory.SINGLETON = FileFactory(ResourceUtil.getInstance().getContext())

