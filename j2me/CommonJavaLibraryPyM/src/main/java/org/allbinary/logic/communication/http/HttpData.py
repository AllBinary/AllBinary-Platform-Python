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
# package org.allbinary.logic.communication.http

from __future__ import annotations



class HttpData:
    instance: HttpData = None

    def _init_fields(self) -> None:
        self.EQUALS: str = None
        self.PARAM_SEP: str = None
        self.URL_PARAM_SEP: str = None
        self.URL_LABEL: str = "Url: "
    

    @staticmethod
    def getInstance() -> HttpData:
        return HttpData.instance
    

    def __init__(self) -> None:
        self._init_fields()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        self.EQUALS = commonSeps.EQUALS
        self.PARAM_SEP = commonSeps.AMPERSAND
        self.URL_PARAM_SEP = commonSeps.QUESTION
from org.allbinary.string.CommonSeps import CommonSeps


HttpData.instance = HttpData()

