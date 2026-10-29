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
# package org.allbinary.business.advertisement

from __future__ import annotations



class Advertisements:

    def _init_fields(self) -> None:
        self.bannerList: BasicArrayList = BasicArrayListD()
        self.pageList: BasicArrayList = BasicArrayListD()
        self.myRandomFactory: MyRandomFactory = MyRandomFactory.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    def addPage(self, advertisementProcessorInterface: AdvertisementProcessorInterface) -> None:
        if not self.pageList.contains(advertisementProcessorInterface):
            self.pageList.add(advertisementProcessorInterface)
    

    def startRandomPage(self) -> None:
        size: int = self.pageList.size()
        if size > 0:
            random: int = self.myRandomFactory.getAbsoluteNextInt(size)
            advertisementProcessorInterface: AdvertisementProcessorInterface = self.pageList.objectArray[random]
            advertisementProcessorInterface.start()
    

    def processRandomPage(self) -> None:
        if LockedUtil.getInstance().isLocked():
            size: int = self.pageList.size()
            if size > 0:
                random: int = self.myRandomFactory.getAbsoluteNextInt(size)
                advertisementProcessorInterface: AdvertisementProcessorInterface = self.pageList.objectArray[random]
                advertisementProcessorInterface.process()
    

    def stopAllPage(self) -> None:
        index = self.pageList.size()
        while (index := index - 1) >= 0:
            advertisementProcessorInterface: AdvertisementProcessorInterface = self.pageList.objectArray[index]
            advertisementProcessorInterface.stop()
    

    def addBanner(self, advertisementProcessorInterface: AdvertisementProcessorInterface) -> None:
        if not self.bannerList.contains(advertisementProcessorInterface):
            self.bannerList.add(advertisementProcessorInterface)
    

    def startAll(self) -> None:
        index = self.bannerList.size()
        while (index := index - 1) >= 0:
            advertisementProcessorInterface: AdvertisementProcessorInterface = self.bannerList.objectArray[index]
            advertisementProcessorInterface.start()
    

    def stopAllBanner(self) -> None:
        index = self.bannerList.size()
        while (index := index - 1) >= 0:
            advertisementProcessorInterface: AdvertisementProcessorInterface = self.bannerList.objectArray[index]
            advertisementProcessorInterface.stop()
    

    def getBanner(self, index: int) -> AdvertisementProcessorInterface:
        advertisementProcessorInterface: AdvertisementProcessorInterface = self.bannerList.objectArray[index]
        return advertisementProcessorInterface
    

    def stopAll(self) -> None:
        self.stopAllBanner()
        self.stopAllPage()
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.logic.system.security.licensing.LockedUtil import LockedUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


