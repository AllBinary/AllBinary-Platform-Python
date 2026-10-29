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

from org.allbinary.layer.LayerManagerLoggingBase import LayerManagerLoggingBase


class LayerManagerLogging(LayerManagerLoggingBase):
    instance: LayerManagerLogging = None
    removeFailed: bool = False

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.stringBuilder: StringMaker = StringMaker()
        self.APPEND: str = "append"
        self.APPEND_: str = " append: "
        self._AT_: str = " at: "
        self.ATTEMPT_REMOVE_: str = " Remove Attempt: "
        self.REMOVE_: str = " Remove: "
        self.REMOVE: str = "remove"
        self.DID_NOT_REMOVE: str = " Did not remove: "
        self.CLEAR: str = " Clear List"

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> LayerManagerLogging:
        return LayerManagerLogging.instance
    

    # throws Exception
    def append(self, layerInterface: AllBinaryLayer) -> None:
        self.stringBuilder.delete(0, self.stringBuilder.length())
        self.logUtil.putF(str(self.stringBuilder.appendint(int(TsUtil.getInstance().hashCode(self))).append(self.APPEND_).append(layerInterface.getName())), self, self.APPEND)
    

    def appendAt(self, layerInterface: AllBinaryLayer, index: int) -> None:
        self.stringBuilder.delete(0, self.stringBuilder.length())
        self.logUtil.putF(str(self.stringBuilder.appendint(int(TsUtil.getInstance().hashCode(self))).append(self.APPEND_).append(layerInterface.getName()).append(self._AT_).appendint(index)), self, self.APPEND)
    

    def remove(self, layerInterface: AllBinaryLayer) -> None:
        if layerInterface is None:
            self.stringBuilder.delete(0, self.stringBuilder.length())
            self.logUtil.putF(str(self.stringBuilder.appendint(int(TsUtil.getInstance().hashCode(self))).append(self.ATTEMPT_REMOVE_).append(StringUtil.getInstance().toString(layerInterface))), self, self.REMOVE)
        else:
            self.stringBuilder.delete(0, self.stringBuilder.length())
            self.logUtil.putF(str(self.stringBuilder.appendint(int(TsUtil.getInstance().hashCode(self))).append(self.ATTEMPT_REMOVE_).append(layerInterface.getName())), self, self.REMOVE)
    

    def removeResult(self, layerManager: LayerManager, layerInterface: AllBinaryLayer, result: bool) -> None:
        if layerInterface is None:
            self.stringBuilder.delete(0, self.stringBuilder.length())
            self.logUtil.putF(str(self.stringBuilder.appendint(int(TsUtil.getInstance().hashCode(self))).append(self.REMOVE_).append(StringUtil.getInstance().toString(layerInterface))), self, self.REMOVE)
        elif result:
            if LayerManagerLogging.removeFailed:
                self.stringBuilder.delete(0, self.stringBuilder.length())
                self.logUtil.putF(str(self.stringBuilder.appendint(int(TsUtil.getInstance().hashCode(self))).append(self.REMOVE_).append(layerInterface.getName())), self, self.REMOVE)
        else:
            self.stringBuilder.delete(0, self.stringBuilder.length())
            self.logUtil.putF(str(self.stringBuilder.appendint(int(TsUtil.getInstance().hashCode(self))).append(self.DID_NOT_REMOVE).append(layerInterface.getName())), self, self.REMOVE)
            LayerManagerLogging.removeFailed = True
    

    def log(self, layerManager: LayerManager) -> None:
        self.stringBuilder.delete(0, self.stringBuilder.length())
        size: int = layerManager.getSize()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        self.stringBuilder.append(format(TsUtil.getInstance().hashCode(layerManager), "x")).append(commonSeps.COLON_SEP)
        self.stringBuilder.appendint(size).append(commonSeps.COLON_SEP)
        allBinaryLayer: AllBinaryLayer = None
        for index in range(0, size):
            allBinaryLayer = (layerManager.getLayerAt(index))
            self.stringBuilder.append(allBinaryLayer.getName()).append(commonSeps.COMMA)
        self.logUtil.putF(str(self.stringBuilder), self, self.REMOVE)
    

    def clear(self) -> None:
        self.stringBuilder.delete(0, self.stringBuilder.length())
        self.logUtil.putF(str(self.stringBuilder.appendint(int(TsUtil.getInstance().hashCode(self))).append(self.CLEAR)), self, self.CLEAR)
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps


LayerManagerLogging.instance = LayerManagerLogging()

