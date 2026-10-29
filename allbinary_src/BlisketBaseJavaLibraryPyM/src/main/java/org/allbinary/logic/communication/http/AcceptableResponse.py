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



class AcceptableResponse:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self, candidate: str, tagName: str, index: int) -> None:
        from org.allbinary.logic.communication.http.AcceptableResponseUtil import AcceptableResponseUtil
        self._init_fields()
        self.logUtil.putF(tagName, self, self.commonStrings.CONSTRUCTOR)
        acceptableResponseUtil: AcceptableResponseUtil = AcceptableResponseUtil.getInstance()
        acceptableResponseUtil.candidateVector.addAt(index, candidate)
        acceptableResponseUtil.tagNameVector.addAt(index, tagName)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


