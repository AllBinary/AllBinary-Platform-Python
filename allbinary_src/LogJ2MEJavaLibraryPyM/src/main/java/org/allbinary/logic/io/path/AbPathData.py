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
# package org.allbinary.logic.io.path

from __future__ import annotations



class AbPathData:
    instance: AbPathData = None

    def _init_fields(self) -> None:
        self.EXTENSION_SEP: str = CommonSeps.getInstance().PERIOD
        self.SEPARATORCHAR: str = '/'
        self.SEPARATOR: str = CommonSeps.getInstance().FORWARD_SLASH
    

    @staticmethod
    def getInstance() -> AbPathData:
        return AbPathData.instance
    

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.logic.io.file.FilePathData import FilePathData
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps


AbPathData.instance = AbPathData()

