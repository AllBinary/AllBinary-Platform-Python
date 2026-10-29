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
# package org.allbinary.business.error

from __future__ import annotations



class ErrorData:
    instance: ErrorData = None

    def _init_fields(self) -> None:
        self.NAME: str = "ERROR_NAME"
        self.TEXT: str = "ERROR_TEXT"
    

    @staticmethod
    def getInstance() -> ErrorData:
        return ErrorData.instance
    

    def __init__(self) -> None:
        self._init_fields()


ErrorData.instance = ErrorData()

