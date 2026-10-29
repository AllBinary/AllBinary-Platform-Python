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

from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream


class AbFileLocalInputStream(AbFileInputStream):
    

    def __init__(self, file: AbFile) -> None:
        super().__init__(AbFileNativeUtil.get(file))
# from java.io.FileNotFoundException import FileNotFoundException
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil


