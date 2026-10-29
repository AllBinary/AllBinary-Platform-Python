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
# package org.allbinary.business.user.commerce.inventory.item.download

from __future__ import annotations

import datetime


class DownloadableItem:

    def _init_fields(self) -> None:
        self.id: str = None
        self.basicItemId: str = None
        self.enabled: str = None
        self.system: str = None
        self.platform: str = None
        self.specialName: str = None
        self.version: str = None
        self.changes: str = None
        self.licenseFile: str = None
        self.file: str = None
        self.size: int = None
        self.validTime: int = None
        self.retries: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, id: str) -> None:
        self._init_fields()
        EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        self.id = ProductIdGenerator().getNext()
        self.basicItemId = id
        self.enabled = EntryData.getInstance().YES
        self.system = "Java"
        self.platform = "Android"
        self.specialName = EMPTY_STRING
        self.version = EMPTY_STRING
        self.changes = EMPTY_STRING
        self.licenseFile = EMPTY_STRING
        self.file = EMPTY_STRING
        self.size = str(0)
        self.validTime = str(0)
        self.retries = EMPTY_STRING
    

    def _constructor1(self, hashMap: dict) -> None:
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        self._init_fields()
        self.id = hashMap.get(DownloadItemData.ID)
        self.basicItemId = hashMap.get(BasicItemData.getInstance().ID)
        self.enabled = hashMap.get(EntryData.getInstance().ENABLE)
        self.system = hashMap.get(DownloadItemData.SYSTEM)
        self.platform = hashMap.get(DownloadItemData.PLATFORM)
        self.specialName = hashMap.get(DownloadItemData.SPECIAL_NAME)
        self.version = hashMap.get(DownloadItemData.VERSION)
        self.changes = hashMap.get(DownloadItemData.CHANGES)
        self.licenseFile = hashMap.get(DownloadItemData.LICENSE_FILE)
        self.file = hashMap.get(DownloadItemData.FILE)
        value: str = hashMap.get(DownloadItemData.SIZE)
        if not StringValidationUtil.getInstance().isEmpty(value):
            self.size = str(value)
        else:
            self.size = int(0)
        validTime: str = hashMap.get(DownloadItemData.VALID_TIME)
        if not StringValidationUtil.getInstance().isEmpty(validTime):
            self.validTime = str(validTime)
        else:
            totalYears: str = hashMap.get(DownloadItemData.VALID_TIME_YEARS)
            totalMonths: str = hashMap.get(DownloadItemData.VALID_TIME_MONTHS)
            totalDays: str = hashMap.get(DownloadItemData.VALID_TIME_DAYS)
            totalHours: str = hashMap.get(DownloadItemData.VALID_TIME_HOURS)
            totalMinutes: str = hashMap.get(DownloadItemData.VALID_TIME_MINUTES)
            totalSeconds: str = hashMap.get(DownloadItemData.VALID_TIME_SECONDS)
            totalTime: int = TimeUtil.getInstance().getTotalTime(totalYears, totalMonths, totalDays, totalHours, totalMinutes, totalSeconds)
            self.validTime = int(totalTime)
        self.retries = hashMap.get(DownloadItemData.RETRIES)
    

    def toVector(self) -> BasicArrayList:
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(int(calendar.getTimeInMillis()))
        values: BasicArrayList = BasicArrayListD()
        values.add(self.getId())
        values.add(self.basicItemId)
        values.add(self.enabled)
        values.add(self.getSpecialName())
        values.add(self.getVersion())
        values.add(self.getChanges())
        values.add(self.getSystem())
        values.add(self.getPlatform())
        values.add(self.getLicenseFile())
        values.add(self.getFile())
        values.add(str(self.getSize()))
        values.add(str(self.getValidTime()))
        values.add(self.getRetries())
        values.add(time)
        values.add(time)
        return values
    

    def toHashMap(self) -> dict:
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
        values: dict = StdUtil.getInstance().createHashMap()
        values.put(DownloadItemData.ID, self.getId())
        values.put(BasicItemData.getInstance().ID, self.basicItemId)
        values.put(EntryData.getInstance().ENABLE, self.enabled)
        values.put(DownloadItemData.SYSTEM, self.getSystem())
        values.put(DownloadItemData.PLATFORM, self.getPlatform())
        values.put(DownloadItemData.SPECIAL_NAME, self.getSpecialName())
        values.put(DownloadItemData.VERSION, self.getVersion())
        values.put(DownloadItemData.CHANGES, self.getChanges())
        values.put(DownloadItemData.LICENSE_FILE, self.getLicenseFile())
        values.put(DownloadItemData.FILE, self.getFile())
        values.put(DownloadItemData.SIZE, str(self.getSize()))
        values.put(DownloadItemData.VALID_TIME, str(self.getValidTime()))
        values.put(DownloadItemData.RETRIES, self.getRetries())
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        values.put(EntryData.getInstance().LASTMODIFIED, time)
        return values
    

    def getId(self) -> str:
        return self.id
    

    def getSystem(self) -> str:
        return self.system
    

    def getPlatform(self) -> str:
        return self.platform
    

    def getSpecialName(self) -> str:
        return self.specialName
    

    def getVersion(self) -> str:
        return self.version
    

    def getChanges(self) -> str:
        return self.changes
    

    def getLicenseFile(self) -> str:
        return self.licenseFile
    

    def getFile(self) -> str:
        return self.file
    

    def getSize(self) -> int:
        return self.size
    

    def getValidTime(self) -> int:
        return self.validTime
    

    def getRetries(self) -> str:
        return self.retries
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.data.generator.ProductIdGenerator import ProductIdGenerator
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.time.TimeUtil import TimeUtil


