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
# package org.allbinary.layer

from __future__ import annotations



class BasicLayerProcessor:
    NULL_LAYER_PROCESSOR: BasicLayerProcessor = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.list_: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def add(self, layerInterface: AllBinaryLayer) -> None:
        if not self.list_.contains(layerInterface):
            self.list_.add(layerInterface)
    

    # throws Exception
    def process(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        raise Exception(CommonStrings.getInstance().NOT_IMPLEMENTED)
    

    def getList(self) -> BasicArrayList:
        return self.list_
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


BasicLayerProcessor.NULL_LAYER_PROCESSOR = BasicLayerProcessor()

