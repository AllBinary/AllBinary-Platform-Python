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



class BufferedIOUtil:
    

    # throws Exception
    @staticmethod
    def copy(backupFile: AbFile, backupFileBak: AbFile) -> None:
        line: str = StringUtil.getInstance().EMPTY_STRING
        tmpOut: BufferedWriter = BufferedWriter(FileWriter(AbFileNativeUtil.get(backupFileBak)))
        tmpIn: BufferedReader = BufferedReader(FileReader(AbFileNativeUtil.get(backupFile)))
        while True:
            line = tmpIn.readLine()
            if line is None:
                break
            tmpOut.write(line, 0, len(line))
            tmpOut.newLine()
        tmpOut.flush()
# from java.io.BufferedReader import BufferedReader
# from java.io.BufferedWriter import BufferedWriter
# from java.io.FileReader import FileReader
# from java.io.FileWriter import FileWriter
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil
from org.allbinary.logic.string.StringUtil import StringUtil


