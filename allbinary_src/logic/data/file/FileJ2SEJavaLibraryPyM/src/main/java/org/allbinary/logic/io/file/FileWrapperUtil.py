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



class FileWrapperUtil:
    

    @staticmethod
    def wrapFiles(files: list[object]) -> list[AbFile]:
        from org.allbinary.logic.io.file.AbFile import AbFile
        try:
            abFileArray: list[AbFile] = [None] * (len(files))
            for index in range(len(files) - 1, 0 - 1, -1):
                abFileArray[index] = AbFile(files[index])
            return abFileArray
        except Exception as e:
            PreLogUtil.putSE("Exception Wrapping Files", "FileWrapperUtil", "wrapFiles", e)
            return [None] * (0)
    

    @staticmethod
    def wrapFile(file: File) -> AbFile:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.AbFile import AbFile
        try:
            return AbFile(file)
        except Exception as e:
            PreLogUtil.putSE("Exception Wrapping File", "FileWrapperUtil", "wrapFile", e)
            return AbFile.NULL_FILE
# from java.io.File import File
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil


