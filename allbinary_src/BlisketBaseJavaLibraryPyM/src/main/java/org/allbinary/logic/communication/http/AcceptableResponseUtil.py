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



class AcceptableResponseUtil:
    instance: AcceptableResponseUtil = None

    def _init_fields(self) -> None:
        self.candidateVector: BasicArrayList = BasicArrayListD()
        self.tagNameVector: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AcceptableResponseUtil:
        return AcceptableResponseUtil.instance
    

    @staticmethod
    def _static_init() -> None:
        TsUtil.getInstance().hashCode(AcceptableResponseFactory.getInstance().HTML)
    

    def get(self, index: int) -> str:
        return self.candidateVector.get(index)
    

    def getTagName(self, index: int) -> str:
        return self.tagNameVector.get(index)
    

    def size(self) -> int:
        return self.candidateVector.size()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.AcceptableResponseFactory import AcceptableResponseFactory


AcceptableResponseUtil.instance = AcceptableResponseUtil()

AcceptableResponseUtil._static_init()

