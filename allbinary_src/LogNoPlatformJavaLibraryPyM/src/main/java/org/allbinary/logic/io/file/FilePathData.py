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

import os


class FilePathData:
    instance: FilePathData = None

    def _init_fields(self) -> None:
        self.SEPARATORCHAR: str = os.sep
        self.PATH_START: str = os.sep
    

    @staticmethod
    def getInstance() -> FilePathData:
        return FilePathData.instance
    

    def __init__(self) -> None:
        self._init_fields()
        if os.sep == '\\':
            self.PATH_START = os.sep + os.sep
# from java.io.File import File


FilePathData.instance = FilePathData()

