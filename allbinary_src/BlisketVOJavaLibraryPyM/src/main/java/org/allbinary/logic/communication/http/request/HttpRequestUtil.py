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
# package org.allbinary.logic.communication.http.request

from __future__ import annotations



class HttpRequestUtil:
    instance: HttpRequestUtil = None
    

    @staticmethod
    def getInstance() -> HttpRequestUtil:
        return HttpRequestUtil.instance
    

    def __init__(self) -> None:
        pass
    

    def getLastSeparatorIndex(self, requestPath: str) -> int:
        beginIndex: int = requestPath.rfind(AbPathData.getInstance().SEPARATOR)
        if beginIndex < 0:
            beginIndex = requestPath.rfind("\\")
        return beginIndex
    

    # throws Exception
    def generateFileName(self, requestPath: str) -> str:
        beginIndex: int = self.getLastSeparatorIndex(requestPath)
        if beginIndex < 0:
            return requestPath
        else:
            return requestPath[beginIndex + 1:]
from org.allbinary.logic.io.path.AbPathData import AbPathData


HttpRequestUtil.instance = HttpRequestUtil()

