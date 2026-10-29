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
# package org.allbinary.input.automation.module.generic

from __future__ import annotations

from org.allbinary.input.automation.module.AbstractInputAutomationWorker import AbstractInputAutomationWorker


class GenericInputAutomationWorker(AbstractInputAutomationWorker):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.PROCESS_DATA_WORKER_RESULTS: str = "processDataWorkerResults"
        self.lastFrame: int = int(-1)
        self.frame: int = None
        self.genericProfile: GenericProfile = None
    

    def __init__(self, inputAutomationActionInterface: InputAutomationActionInterface, genericProfile: GenericProfile, motionRectangleConstraintsInterface: MotionRectangleConstraintsInterface, imageComparatorConstraintsInterface: ImageComparatorConstraintsInterface) -> None:
        from org.allbinary.input.automation.module.generic.GenericProfileCaptureWorkerFactory import GenericProfileCaptureWorkerFactory
        super().__init__(inputAutomationActionInterface)
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.setCaptureWorker(GenericProfileCaptureWorkerFactory.getInstance(genericProfile))
        self.setInputAutomationActionInterface(inputAutomationActionInterface)
        self.setImageComparisonWorker(ImageComparisonWorker(imageComparatorConstraintsInterface))
        self.setMotionRectanglesWorker(MotionRectanglesWorker(motionRectangleConstraintsInterface))
        self.setGenericProfile(genericProfile)
        vector: BasicArrayList = self.getGenericProfile().getGenericProfileDataWorkerTypeVector()
        size: int = vector.size()
        for index in range(0, size):
            genericProfileDataWorkerType: GenericProfileDataWorkerType = vector.get(index)
            self.logUtil.putF("Adding Listener: " + str(genericProfileDataWorkerType), self, self.commonStrings.CONSTRUCTOR)
            if genericProfileDataWorkerType == GenericProfileDataWorkerType.COMPARISON:
                self.getCaptureWorker().addListenerInterface(self.getImageComparisonWorker())
            elif genericProfileDataWorkerType == GenericProfileDataWorkerType.MOTION:
                self.getImageComparisonWorker().addListenerInterface(self.getMotionRectanglesWorker())
    

    # throws Exception
    def processDataWorkerResults(self) -> None:
        from org.allbinary.input.automation.module.generic.CaptureWorkerUtil import CaptureWorkerUtil
        self.logUtil.putF(self.commonStrings.START, self, self.PROCESS_DATA_WORKER_RESULTS)
        self.waitForDataWorkers()
        cacheInterface: J2SECacheInterface = CapturedBufferedImagesCacheSingleton.getInstance()
        keyArray: list[object] = cacheInterface.keySet().toArray()
        if len(keyArray) > 0:
            self.logUtil.putF("Image Available", self, self.PROCESS_DATA_WORKER_RESULTS)
            self.setFrame(keyArray[len(keyArray) - 1])
            if self.getFrame() > self.lastFrame:
                self.logUtil.putF("Processing new frame: " + str(self.getFrame()), self, self.PROCESS_DATA_WORKER_RESULTS)
                hashMap: dict = self.getGenericProfile().getGenericProfileActions().getHashMap()
                set: Set = hashMap.keySet()
                self.logUtil.putF("Processing " + str(set.size()) + "Actions", self, self.PROCESS_DATA_WORKER_RESULTS)
                actionNameArray: list[object] = set.toArray()
                size: int = len(actionNameArray)
                for index in range(0, size):
                    actionNameString: str = actionNameArray[index]
                    self.logUtil.putF("Processing Action: " + actionNameString, self, self.PROCESS_DATA_WORKER_RESULTS)
                    genericProfileAction: GenericProfileAction = hashMap.get(actionNameString)
                    genericProfileActionScript: GenericProfileActionScript = genericProfileAction.getGenericProfileActionScript()
                    vector: BasicArrayList = genericProfileActionScript.getProfileActionConditionInterfaceVector()
                    CaptureWorkerUtil.processProfileActionConditions(vector, self.getFrame())
                self.lastFrame = self.getFrame()
        else:
            self.logUtil.putF("Image Not Available", self, self.PROCESS_DATA_WORKER_RESULTS)
    

    # throws Exception
    def process(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.PROCESS)
        self.startDataWorkers()
        self.processDataWorkerResults()
    

    def getGenericProfile(self) -> GenericProfile:
        return self.genericProfile
    

    def setGenericProfile(self, genericProfile: GenericProfile) -> None:
        self.genericProfile = genericProfile
    

    def getFrame(self) -> int:
        return self.frame
    

    def setFrame(self, frame: int) -> None:
        self.frame = frame
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.input.automation.module.InputAutomationActionInterface import InputAutomationActionInterface
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType
from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileAction import GenericProfileAction
from org.allbinary.input.automation.module.generic.configuration.profile.actions.script.GenericProfileActionScript import GenericProfileActionScript
from org.allbinary.input.media.image.capture.CapturedBufferedImagesCacheSingleton import CapturedBufferedImagesCacheSingleton
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.cache.J2SECacheInterface import J2SECacheInterface
from org.allbinary.media.image.comparison.ImageComparatorConstraintsInterface import ImageComparatorConstraintsInterface
from org.allbinary.media.image.comparison.ImageComparisonWorker import ImageComparisonWorker
from org.allbinary.media.image.comparison.motion.MotionRectangleConstraintsInterface import MotionRectangleConstraintsInterface
from org.allbinary.media.image.comparison.motion.MotionRectanglesWorker import MotionRectanglesWorker


