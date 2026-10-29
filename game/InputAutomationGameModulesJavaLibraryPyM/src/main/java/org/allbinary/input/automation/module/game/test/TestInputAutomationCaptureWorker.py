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
# package org.allbinary.input.automation.module.game.test

from __future__ import annotations

from org.allbinary.input.automation.module.AbstractInputAutomationWorker import AbstractInputAutomationWorker


class TestInputAutomationCaptureWorker(AbstractInputAutomationWorker):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.genericProfileActions: GenericProfileActions = None
        self.MESSAGE: str = "GenericInputAutomationCaptureWorker"
        self.PROCESS_DATA_WORKER_RESULTS: str = "processDataWorkerResults"
        self.IMAGE_AVAILABLE_SO_PROCESSING: str = "Image Available so processing"
        self.IMAGE_NOT_AVAILABLE: str = "Image Not Available"
    

    def __init__(self, inputAutomationActionInterface: InputAutomationActionInterface, genericProfileActions: GenericProfileActions, imageComparatorConstraintsInterface: ImageComparatorConstraintsInterface, motionRectangleConstraintsInterface: MotionRectangleConstraintsInterface) -> None:
        super().__init__(inputAutomationActionInterface)
        self._init_fields()
        self.logUtil.putF(self.MESSAGE, self, self.commonStrings.CONSTRUCTOR)
        self.setGenericProfileActions(genericProfileActions)
    

    # throws Exception
    def processDataWorkerResults(self) -> None:
        cacheInterface: J2SECacheInterface = CapturedBufferedImagesCacheSingleton.getInstance()
        if cacheInterface.keySet().size() > 0:
            self.logUtil.putF(self.IMAGE_AVAILABLE_SO_PROCESSING, self, self.PROCESS_DATA_WORKER_RESULTS)
            anyType: object = cacheInterface.keySet().toArray()[0]
            hashMap: dict = self.getGenericProfileActions().getHashMap()
            set: Set = hashMap.keySet()
            actionNameArray: list[object] = set.toArray()
            size: int = len(actionNameArray)
            for index in range(0, size):
                actionNameString: str = actionNameArray[index]
                genericProfileAction: GenericProfileAction = hashMap.get(actionNameString)
                genericProfileActionScript: GenericProfileActionScript = genericProfileAction.getGenericProfileActionScript()
                vector: BasicArrayList = genericProfileActionScript.getProfileActionConditionInterfaceVector()
            cacheInterface.get(anyType)
        else:
            self.logUtil.putF(self.IMAGE_NOT_AVAILABLE, self, self.PROCESS_DATA_WORKER_RESULTS)
    

    # throws Exception
    def process(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.PROCESS)
        self.startDataWorkers()
        self.processDataWorkerResults()
    

    def getGenericProfileActions(self) -> GenericProfileActions:
        return self.genericProfileActions
    

    def setGenericProfileActions(self, genericProfileActions: GenericProfileActions) -> None:
        self.genericProfileActions = genericProfileActions
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.input.automation.module.InputAutomationActionInterface import InputAutomationActionInterface
from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileAction import GenericProfileAction
from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActions import GenericProfileActions
from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GenericProfileActionScript import GenericProfileActionScript
from org.allbinary.input.media.image.capture.CapturedBufferedImagesCacheSingleton import CapturedBufferedImagesCacheSingleton
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.cache.J2SECacheInterface import J2SECacheInterface
from org.allbinary.media.image.comparison.ImageComparatorConstraintsInterface import ImageComparatorConstraintsInterface
from org.allbinary.media.image.comparison.motion.MotionRectangleConstraintsInterface import MotionRectangleConstraintsInterface


