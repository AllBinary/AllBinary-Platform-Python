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



class InputOutputTypeData:
    instance: InputOutputTypeData = None

    def _init_fields(self) -> None:
        self.NAME: str = "INPUT_OUTPUT_TYPE_NAME"
        self.FILE: str = "INPUT_OUTPUT_TYPE_FILE"
        self.RESPONSE: str = "INPUT_OUTPUT_TYPE_RESPONSE"
        self.DB: str = "INPUT_OUTPUT_TYPE_DB"
        self.JSP: str = "jsp"
        self.JSP_FRAGMENT: str = "jspf"
        self.PHP: str = "php"
        self.ASP: str = "asp"
        self.PL: str = "pl"
        self.DEFAULT: str = self.JSP
        self.DEFAULT_FRAGMENT: str = self.JSP_FRAGMENT
    

    @staticmethod
    def getInstance() -> InputOutputTypeData:
        return InputOutputTypeData.instance
    

    def __init__(self) -> None:
        self._init_fields()


InputOutputTypeData.instance = InputOutputTypeData()

