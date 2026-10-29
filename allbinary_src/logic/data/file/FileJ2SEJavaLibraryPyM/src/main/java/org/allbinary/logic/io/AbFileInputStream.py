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

# from java.io.FileInputStream import FileInputStream


class AbFileInputStream(FileInputStream):

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, name: str) -> None:
        super().__init__(name)
    

    def _constructor1(self, file: AbFile) -> None:
        super().__init__(AbFileNativeUtil.get(file))
    

    def _constructor1(self, file: File) -> None:
        super().__init__(file)
# from java.io.File import File
# from java.io.FileNotFoundException import FileNotFoundException
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil


