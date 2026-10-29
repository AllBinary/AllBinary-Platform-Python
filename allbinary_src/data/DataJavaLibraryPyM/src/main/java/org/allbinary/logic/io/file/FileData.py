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



class FileData:
    instance: FileData = None

    def _init_fields(self) -> None:
        self.NAME: str = "FILE_NAME"
        self.ISFILE: str = "FILE_ISFILE"
        self.ISDIRECTORY: str = "FILE_ISDIRECTORY"
        self.ISHIDDEN: str = "FILE_ISHIDDEN"
        self.ISABSOLUTE: str = "FILE_ISABSOLUTE"
        self.ROOT_NAME: str = "FILE_ROOT_NAME"
        self.PATH: str = "FILE_PATH"
        self.ABSOLUTE_PATH: str = "FILE_ABSOLUTE_PATH"
        self.CANONICAL_PATH: str = "FILE_CANONICAL_PATH"
        self.PARENT: str = "FILE_PARENT"
        self.MINLEN: int = 1
        self.MAXLEN: int = 120
        self.MAXIMAGEFILESIZE: int = 1048576
        self.MINIMAGEFILESIZE: int = 32
        self.MAXDOWNLOADABLEFILESIZE: int = 1048576 * 20
        self.MINDOWNLOADABLEFILESIZE: int = 1
    

    @staticmethod
    def getInstance() -> FileData:
        return FileData.instance
    

    def __init__(self) -> None:
        self._init_fields()


FileData.instance = FileData()

