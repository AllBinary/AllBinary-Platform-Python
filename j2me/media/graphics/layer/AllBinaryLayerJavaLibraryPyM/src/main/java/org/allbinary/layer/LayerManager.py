# Generated Code Do Not Modify
# package org.allbinary.layer

from __future__ import annotations

import threading


class LayerManager:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.systemWrapper: ABSystemWrapper = ABSystemWrapper.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.layerManagerLogging: LayerManagerLoggingBase = None
        self.list_: BasicArrayList = BasicArrayListD()
        self.anyType: SynchObject = SynchObject()
    

    def __init__(self, layerManagerLogging: LayerManagerLoggingBase) -> None:
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.layerManagerLogging = layerManagerLogging
    

    def contains(self, layerInterface: AllBinaryLayer) -> bool:
        return self.list_.contains(layerInterface)
    

    # throws Exception
    def update(self, layerInterface: AllBinaryLayer) -> None:
        had: bool = self.list_.remove(layerInterface)
        if had:
            nextLayerInterface: AllBinaryLayer = None
            size: int = self.list_.size()
            for index in range(0, size):
                nextLayerInterface = self.list_.get(index)
                if layerInterface.getZP() > nextLayerInterface.getZP():
                    self.list_.addAt(index, layerInterface)
                    return
            self.list_.add(layerInterface)
    

    # throws Exception
    def insert(self, layerInterface: AllBinaryLayer) -> None:
        nextLayerInterface: AllBinaryLayer = None
        size: int = self.list_.size()
        for index in range(0, size):
            nextLayerInterface = self.list_.get(index)
            if layerInterface.getZP() > nextLayerInterface.getZP():
                self.appendAt(layerInterface, index)
                return
        self.append(layerInterface)
    

    # throws Exception
    def append(self, layerInterface: AllBinaryLayer) -> None:
        self.layerManagerLogging.append(layerInterface)
        self.list_.add(layerInterface)
    

    # throws Exception
    def appendAt(self, layerInterface: AllBinaryLayer, index: int) -> None:
        self.layerManagerLogging.appendAt(layerInterface, index)
        self.list_.addAt(index, layerInterface)
    

    # throws Exception
    def remove(self, layerInterface: AllBinaryLayer) -> None:
        with self._lock:  # synchronized (self.anyType)
            self.layerManagerLogging.remove(layerInterface)
            result: bool = self.list_.remove(layerInterface)
            self.layerManagerLogging.removeResult(self, layerInterface, result)
    

    def getLayerAt(self, index: int) -> Layer:
        return self.list_.objectArray[index]
    

    def getSize(self) -> int:
        return self.list_.size()
    

    # throws Exception
    def cleanup(self) -> None:
        with self._lock:  # synchronized (self.anyType)
            self.list_.clear()
            self.layerManagerLogging.clear()
            self.tsUtil.gc()
            self.tsUtil.gc()
    

    def paint(self, g: Graphics, x: int, y: int) -> None:
        with self._lock:  # synchronized (self.anyType)
            comp: Layer = None
            index = self.list_.size()
            while (index := index - 1) >= 0:
                comp = self.list_.objectArray[index]
                if comp is not None and comp.isVisible():
                    comp.paint(g)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.thread.SynchObject import SynchObject
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper


