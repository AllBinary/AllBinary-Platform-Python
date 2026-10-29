# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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



class FileUnamedUtil:
    instance: FileUnamedUtil = None

    def _init_fields(self) -> None:
        self.commonSeps: CommonSeps = CommonSeps.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> FileUnamedUtil:
        return FileUnamedUtil.instance
    

    def process(self, string: str) -> str:
        simplifiedString: str = string.lower()
        simplifiedString = simplifiedString.replace(self.commonSeps.SPACE, self.commonSeps.UNDERSCORE)
        simplifiedString = simplifiedString.replace(self.commonSeps.DASH, self.commonSeps.UNDERSCORE)
        return simplifiedString
from org.allbinary.string.CommonSeps import CommonSeps


FileUnamedUtil.instance = FileUnamedUtil()

