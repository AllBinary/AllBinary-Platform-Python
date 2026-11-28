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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from org.allbinary.layer.LayerManager import LayerManager


@java_inherited_overloads
class AllBinaryLayerManager(LayerManager):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("layerManagerEventHandler", None)
        vars(self).setdefault("createLayerManagerEvent", None)
        vars(self).setdefault("deleteLayerManagerEvent", None)
        vars(self).setdefault("basicLayerProcessorArray", None)

    def _init_fields(self) -> None:
        from org.allbinary.layer.event.LayerManagerEvent import LayerManagerEvent
        from org.allbinary.layer.event.LayerManagerEventHandler import LayerManagerEventHandler
        self.layerManagerEventHandler: LayerManagerEventHandler = LayerManagerEventHandler.getInstance()
        self.createLayerManagerEvent: LayerManagerEvent = LayerManagerEvent(self, self.layerManagerEventHandler.CREATE)
        self.deleteLayerManagerEvent: LayerManagerEvent = LayerManagerEvent(self, self.layerManagerEventHandler.DELETE)
        self.basicLayerProcessorArray: list[LayerProcessor] = [None] * (0)
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.layer.LayerManagerNoDebug import LayerManagerNoDebug
        super().__init__(LayerManagerNoDebug.getInstance())
        __class__._init_fields(self)
    

    def getLayerProcessorArray(self) -> list[LayerProcessor]:
        return self.basicLayerProcessorArray
    

    def setLayerProcessorArray(self, layerProcessorArray: list[LayerProcessor]) -> None:
        self.basicLayerProcessorArray = layerProcessorArray
    

    def log(self) -> None:
        size: int = len(self.basicLayerProcessorArray)
        for index in range(0, size):
            layerProcessorInterface: LayerProcessor = self.basicLayerProcessorArray[index]
    

    # throws Exception
    def append(self, layerInterface: AllBinaryLayer) -> None:
        if not (self.contains(layerInterface)):
            self.appendProcessors(layerInterface)
            java_super_call(super(), "append", layerInterface)
    

    # throws Exception
    def appendAt(self, layerInterface: AllBinaryLayer, index: int) -> None:
        if not (self.contains(layerInterface)):
            self.appendProcessors(layerInterface)
            java_super_call(super(), "appendAt", layerInterface, index)
    

    # throws Exception
    def appendProcessors(self, layerInterface: AllBinaryLayer) -> None:
        self.createLayerManagerEvent.setLayerInterface(layerInterface)
        self.layerManagerEventHandler.fireEvent(self.createLayerManagerEvent)
        layerProcessorInterface: LayerProcessor = None
        index = len(self.basicLayerProcessorArray)
        while (index := index - 1) >= 0:
            layerProcessorInterface = self.basicLayerProcessorArray[index]
            if layerProcessorInterface.isProcessorLayer(layerInterface):
                layerProcessorInterface.getLayerManager().append(layerInterface)
    

    # throws Exception
    def remove(self, layerInterface: AllBinaryLayer) -> None:
        with self._lock:
            return __class__.__dict__["_remove_unlocked"].__get__(self, __class__)(layerInterface)

    def _remove_unlocked(self, layerInterface: AllBinaryLayer) -> None:
        self.deleteLayerManagerEvent.setLayerInterface(layerInterface)
        self.layerManagerEventHandler.fireDeleteEvent(self.deleteLayerManagerEvent)
        layerProcessorInterface: LayerProcessor = None
        index = len(self.basicLayerProcessorArray)
        while (index := index - 1) >= 0:
            layerProcessorInterface = self.basicLayerProcessorArray[index]
            layerProcessorInterface.getLayerManager().remove(layerInterface)
        java_super_call(super(), "remove", layerInterface)
    

    # throws Exception
    def process(self) -> None:
        layerProcessorInterface: LayerProcessor = None
        size: int = len(self.basicLayerProcessorArray)
        for index in range(0, size):
            layerProcessorInterface = self.basicLayerProcessorArray[index]
            layerProcessorInterface.process(self)
    

    # throws Exception
    def cleanup(self) -> None:
        layerProcessorInterface: LayerProcessor = None
        size: int = len(self.basicLayerProcessorArray)
        for index in range(0, size):
            layerProcessorInterface = self.basicLayerProcessorArray[index]
            layerProcessorInterface.getLayerManager().cleanup()
        java_super_call(super(), "cleanup")
# from org.allbinary.layer.event.LayerManagerEvent import LayerManagerEvent
# from org.allbinary.layer.event.LayerManagerEventHandler import LayerManagerEventHandler


