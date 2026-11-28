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

from java.lang.JavaRuntimeStatic import lazy_static


class HttpData:
    instance: HttpData = None

    def _init_fields(self) -> None:
        if "EQUALS" not in vars(self): self.EQUALS: str = None
        if "PARAM_SEP" not in vars(self): self.PARAM_SEP: str = None
        if "URL_PARAM_SEP" not in vars(self): self.URL_PARAM_SEP: str = None
        self.URL_LABEL: str = "Url: "
    

    @staticmethod
    def getInstance() -> HttpData:
        return HttpData.instance
    

    def __init__(self) -> None:
        from org.allbinary.string.CommonSeps import CommonSeps
        __class__._init_fields(self)
        commonSeps: CommonSeps = CommonSeps.getInstance()
        self.EQUALS = commonSeps.EQUALS
        self.PARAM_SEP = commonSeps.AMPERSAND
        self.URL_PARAM_SEP = commonSeps.QUESTION
# from org.allbinary.string.CommonSeps import CommonSeps


def _HttpData_instance() -> object:
    return HttpData()

lazy_static(HttpData, "instance", _HttpData_instance)

