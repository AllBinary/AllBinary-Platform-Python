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
# package org.allbinary.logic.io

from __future__ import annotations

# from java.io.FileOutputStream import FileOutputStream


class AbFileOutputStream(FileOutputStream):
    

    # throws FileNotFoundException
    @staticmethod
    def createFromAbFile(file: AbFile) -> AbFileOutputStream:
        return AbFileOutputStream(file.getPath(), False)
    

    # throws FileNotFoundException
    @staticmethod
    def createFromAbFileAppend(file: AbFile, append: bool) -> AbFileOutputStream:
        return AbFileOutputStream(file.getPath(), append)
    

    # throws FileNotFoundException
    @staticmethod
    def createFromFilePath(name: str) -> AbFileOutputStream:
        return AbFileOutputStream(name, False)
    

    # throws FileNotFoundException
    @staticmethod
    def createFromFilePathAppend(name: str, append: bool) -> AbFileOutputStream:
        return AbFileOutputStream(name, append)
    

    def __init__(self, name: str, append: bool) -> None:
        super().__init__(name, append)
# from java.io.FileNotFoundException import FileNotFoundException
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil


