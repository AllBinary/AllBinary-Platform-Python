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
# package org.allbinary.media.image

from __future__ import annotations



class ImageCompleteUtil:
    instance: ImageCompleteUtil = None

    def _init_fields(self) -> None:
        self.ISREADY: str = "isReady"
        self.COMPLETE: str = "Image loading complete for: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ImageCompleteUtil:
        return ImageCompleteUtil.instance
    

    # throws Exception
    def waitForImage(self, image: Image, name: str) -> None:
        pass
    

    # throws Exception
    def isReady(self, image: Image, name: str, timeDelayHelper: TimeDelayHelper) -> bool:
        playnImage: PlaynImage = image
        playnCoreImage: CoreImage = playnImage.getImage()
        if not playnCoreImage.isReady() or playnCoreImage.width() + playnCoreImage.height() <= 0:
            self.handleTimeout(name)
            return False
        if not image.isReady():
            image.init(image.getImage())
            if not image.isReady():
                PreLogUtil.put("Waiting for Not Ready Image: " + image.getName(), self, self.ISREADY)
        commonStrings: CommonStrings = CommonStrings.getInstance()
        PreLogUtil.put(self.COMPLETE + image.getName(), self, commonStrings.SUCCESS)
        return True
    

    # throws Exception
    def handleTimeout(self, name: str) -> None:
        pass
    

    # throws Exception
    def waitForAll(self) -> None:
        pass
# from javax.microedition.lcdui.Image import Image
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.microemu.device.playn.PlaynImage import PlaynImage
from playn.core.CoreImage import CoreImage


ImageCompleteUtil.instance = ImageCompleteUtil()

