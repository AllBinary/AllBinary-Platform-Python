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
# package org.allbinary.input.media.image.capture

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class CapturedImageWorkerResultsEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.frame: int = None
        self.bufferedImage: BufferedImage = None
    

    def __init__(self, anyType: object, frame: int, bufferedImage: BufferedImage) -> None:
        super().__init__(anyType)
        self._init_fields()
        self.frame = frame
        self.setBufferedImage(bufferedImage)
    

    def getBufferedImage(self) -> BufferedImage:
        return self.bufferedImage
    

    def setBufferedImage(self, bufferedImage: BufferedImage) -> None:
        self.bufferedImage = bufferedImage
    

    def getFrame(self) -> int:
        return self.frame
# from java.awt.image.BufferedImage import BufferedImage


