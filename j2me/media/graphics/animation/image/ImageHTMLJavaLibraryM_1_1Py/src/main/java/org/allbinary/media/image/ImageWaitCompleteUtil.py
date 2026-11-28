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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.media.image.ImageCompleteUtil import ImageCompleteUtil


@java_inherited_overloads
class ImageWaitCompleteUtil(ImageCompleteUtil):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("timeDelayHelper", None)
        vars(self).setdefault("allTimeDelayHelper", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(18000)
        self.allTimeDelayHelper: TimeDelayHelper = TimeDelayHelper(120000)
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    # throws Exception
    def waitForImage(self, image: Image, name: str) -> None:
        from javax.microedition.lcdui.Image import Image
        self.timeDelayHelper.setStartTimeTNT()
        self.waitForATime(image, name, self.timeDelayHelper)
    

    # throws Exception
    def handleTimeout(self, name: str) -> None:
        if java_predicate(self.timeDelayHelper, "isTimeTNT"):
            raise Exception("isReady: Timeout Waiting or GameHtmlHasLoadedResourcesProcessor does not have this Image: " + name)
    

    # throws Exception
    def waitForATime(self, image: Image, name: str, timeDelayHelper: TimeDelayHelper) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        from org.microemu.device.playn.PlaynImage import PlaynImage
        playnImage: PlaynImage = image
        playnCoreImage: Image = playnImage.getImage()
        while not (java_predicate(playnCoreImage, "isReady")) or playnCoreImage.width() + playnCoreImage.height() <= 0:
            if java_predicate(timeDelayHelper, "isTimeTNT"):
                raise Exception("waitFor: Timeout Waiting or GameHtmlHasLoadedResourcesProcessor does not have this Image: " + name)
        if not (java_predicate(image, "isReady")):
            image.init(image.getImage())
    

    # throws Exception
    def waitForAll(self) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.util.ABHashtable import ABHashtable
        from org.allbinary.util.HashtableUtil import HashtableUtil
        self.allTimeDelayHelper.setStartTimeTNT()
        hashtable: ABHashtable[object, object] = GameFeatureImageCacheFactory.getInstance().getHashtableP()
        objectArray: list[object] = HashtableUtil.getInstance().getKeysAsArray(hashtable)
        size: int = len(objectArray)
        PreLogUtil.put("Image Total: " + str(size), self, "waitForAll")
        for index in range(0, size):
            self.waitForATime(hashtable.get(objectArray[index]), objectArray[index], self.allTimeDelayHelper)
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
# from org.allbinary.util.ABHashtable import ABHashtable
# from org.allbinary.util.HashtableUtil import HashtableUtil
# from org.microemu.device.playn.PlaynImage import PlaynImage


