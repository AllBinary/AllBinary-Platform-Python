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



class BufferedLineReader:

    def _init_fields(self) -> None:
        self.tmpIn: BufferedReader = None
    

    def __init__(self, file: AbFile) -> None:
        self._init_fields()
        self.tmpIn = BufferedReader(FileReader(AbFileNativeUtil.get(file)))
    

    def readUpToLines(self, readAheadIndex: int) -> None:
        pass
    

    # throws Exception
    def readLine(self) -> str:
        return self.tmpIn.readLine()
    

    def getSize(self) -> int:
        return 0
    

    def getCurrent(self) -> int:
        return 0
# from java.io.BufferedReader import BufferedReader
# from java.io.FileReader import FileReader
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil


