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
# package org.allbinary.input.automation.module.generic.configuration.profile

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfileDataWorkerType import GenericProfileDataWorkerType


class SavedCaptureGenericProfileDataWorkerType(GenericProfileDataWorkerType):
    SAVED_CAPTURE: SavedCaptureGenericProfileDataWorkerType = None

    def _init_fields(self) -> None:
        self.path: str = None
        self.lastFrame: int = 0
    

    def __init__(self, name: str, path: str, lastFrame: int) -> None:
        super().__init__(name)
        self._init_fields()
        self.setPath(path)
        self.setLastFrame(lastFrame)
    

    def getPath(self) -> str:
        return self.path
    

    def setPath(self, path: str) -> None:
        self.path = path
    

    def getLastFrame(self) -> int:
        return self.lastFrame
    

    def setLastFrame(self, lastFrame: int) -> None:
        self.lastFrame = lastFrame
# from org.allbinary.input.media.image.InputImageType import InputImageType


def _SavedCaptureGenericProfileDataWorkerType_SAVED_CAPTURE() -> object:
    from org.allbinary.input.media.image.InputImageType import InputImageType
    return SavedCaptureGenericProfileDataWorkerType("Saved " + InputImageType.CAPTURE.getName(), "c:\\share\\captures\\2\\", 100)

lazy_static(SavedCaptureGenericProfileDataWorkerType, "SAVED_CAPTURE", _SavedCaptureGenericProfileDataWorkerType_SAVED_CAPTURE)

