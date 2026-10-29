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



class GenericProfileCaptureWorkerFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(genericProfile: GenericProfile) -> CaptureWorkerInterface:
        from org.allbinary.input.automation.module.generic.SavedCaptureImagesWorker import SavedCaptureImagesWorker
        vector: BasicArrayList = genericProfile.getGenericProfileDataWorkerTypeVector()
        size: int = vector.size()
        for index in range(0, size):
            genericProfileDataWorkerType: GenericProfileDataWorkerType = vector.get(index)
            if genericProfileDataWorkerType == GenericProfileDataWorkerType.SCREEN_CAPTURE:
                return ScreenCaptureImagesWorker()
            elif genericProfileDataWorkerType == GenericProfileDataWorkerType.SAVED_CAPTURE:
                return SavedCaptureImagesWorker(genericProfileDataWorkerType)
        raise Exception("No CaptureWorkerInterface specified in GenericProfile")
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType
from org.allbinary.input.automation.module.generic.configuration.profile.SavedCaptureGenericProfileDataWorkerType import SavedCaptureGenericProfileDataWorkerType
from org.allbinary.input.media.image.capture.CaptureWorkerInterface import CaptureWorkerInterface
from org.allbinary.input.media.image.capture.ScreenCaptureImagesWorker import ScreenCaptureImagesWorker


