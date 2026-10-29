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



class FileFactory:
    instance: FileFactory = None
    

    @staticmethod
    def getInstance() -> FileFactory:
        return FileFactory.instance
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, filePath: str) -> AbFile:
        from org.allbinary.logic.io.file.AbFile import AbFile
        return AbFile.createAbFileFromRawPath(filePath)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, file: AbFile, childFilePath: str) -> AbFile:
        from org.allbinary.logic.io.file.AbFile import AbFile
        return AbFile.createAbFileWithChild(file, childFilePath)
    

    # throws Exception
    def isFile(self, path: str) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        file: AbFile = AbFile.createAbFile(path)
        if file.exists():
            return True
        else:
            return False


FileFactory.instance = FileFactory()

