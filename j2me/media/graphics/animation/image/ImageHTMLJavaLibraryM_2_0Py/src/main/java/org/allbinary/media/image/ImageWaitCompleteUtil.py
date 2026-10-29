# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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

from org.allbinary.media.image.ImageCompleteUtil import ImageCompleteUtil


class ImageWaitCompleteUtil(ImageCompleteUtil):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(18000)
        self.allTimeDelayHelper: TimeDelayHelper = TimeDelayHelper(120000)
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def waitForImage(self, image: Image, name: str) -> None:
        self.timeDelayHelper.setStartTimeTNT()
        self.waitForATime(image, name, self.timeDelayHelper)
    

    # throws Exception
    def handleTimeout(self, name: str) -> None:
        if self.timeDelayHelper.isTimeTNT():
            raise Exception("isReady: Timeout Waiting or GameHtmlHasLoadedResourcesProcessor does not have this Image: " + name)
    

    # throws Exception
    def waitForATime(self, image: Image, name: str, timeDelayHelper: TimeDelayHelper) -> None:
        playnImage: PlaynImage = image
        playnCoreImage: CoreImage = playnImage.getImage()
        while not playnCoreImage.isReady() or playnCoreImage.width() + playnCoreImage.height() <= 0:
            if timeDelayHelper.isTimeTNT():
                raise Exception("waitFor: Timeout Waiting or GameHtmlHasLoadedResourcesProcessor does not have this Image: " + name)
        if not image.isReady():
            image.init(image.getImage())
    

    # throws Exception
    def waitForAll(self) -> None:
        self.allTimeDelayHelper.setStartTimeTNT()
        hashtable: ABHashtable[object, object] = GameFeatureImageCacheFactory.getInstance().getHashtableP()
        objectArray: list[object] = HashtableUtil.getInstance().getKeysAsArray(hashtable)
        size: int = len(objectArray)
        PreLogUtil.put("Image Total: " + str(size), self, "waitForAll")
        for index in range(0, size):
            self.waitForATime(hashtable.get(objectArray[index]), objectArray[index], self.allTimeDelayHelper)
# from javax.microedition.lcdui.Image import Image
from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.HashtableUtil import HashtableUtil
from org.microemu.device.playn.PlaynImage import PlaynImage
from playn.core.CoreImage import CoreImage


