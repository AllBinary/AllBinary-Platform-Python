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

from java.io.FileInputStream import FileInputStream


class AbFileInputStream(FileInputStream):
    

    def __init__(self, name: str) -> None:
        super().__init__(name)
    

    # throws FileNotFoundException
    @staticmethod
    def createFromAbFile(file: AbFile) -> AbFileInputStream:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil
        return AbFileInputStream(AbFileNativeUtil.get(file).getPath())
    

    # throws FileNotFoundException
    @staticmethod
    def createFromFile(file: File) -> AbFileInputStream:
        return AbFileInputStream(file.getPath())
# from java.io.File import File
# from java.io.FileNotFoundException import FileNotFoundException
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil


