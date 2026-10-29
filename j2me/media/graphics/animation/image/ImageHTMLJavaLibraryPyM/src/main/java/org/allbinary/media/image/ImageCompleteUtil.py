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
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(18000)
        self.allTimeDelayHelper: TimeDelayHelper = TimeDelayHelper(120000)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ImageCompleteUtil:
        return ImageCompleteUtil.instance
    

    # throws Exception
    def waitForImage(self, image: Image, name: str) -> None:
        self.timeDelayHelper.setStartTime()
        self.waitForATime(image, name, self.timeDelayHelper)
    

    # throws Exception
    def isReady(self, image: Image, name: str, timeDelayHelper: TimeDelayHelper) -> bool:
        playnImage: PlaynImage = image
        if not playnImage.getImage().isReady() and playnImage.getImage().width() + playnImage.getImage().height() == 0:
            if timeDelayHelper.isTime():
                raise Exception("isReady: Timeout Waiting or GameHtmlHasLoadedResourcesProcessor does not have this Image: " + name)
            return False
        return True
    

    # throws Exception
    def waitForATime(self, image: Image, name: str, timeDelayHelper: TimeDelayHelper) -> None:
        playnImage: PlaynImage = image
        while not playnImage.getImage().isReady() and playnImage.getImage().width() + playnImage.getImage().height() == 0:
            if timeDelayHelper.isTime():
                raise Exception("waitFor: Timeout Waiting or GameHtmlHasLoadedResourcesProcessor does not have this Image: " + name)
    

    # throws Exception
    def waitForAll(self) -> None:
        self.allTimeDelayHelper.setStartTime()
        hashtable: dict = GameFeatureImageCacheFactory.getInstance().getHashtable()
        objectArray: list[object] = HashtableUtil.getInstance().getKeysAsArray(hashtable)
        size: int = len(objectArray)
        PreLogUtil.put("Total: " + str(size), self, "waitForAll")
        for index in range(0, size):
            self.waitForATime(hashtable.get(objectArray[index]), objectArray[index], self.allTimeDelayHelper)
# from javax.microedition.lcdui.Image import Image
from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.HashtableUtil import HashtableUtil
from org.microemu.device.playn.PlaynImage import PlaynImage


ImageCompleteUtil.instance = ImageCompleteUtil()

