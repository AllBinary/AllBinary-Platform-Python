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
# package org.allbinary.logic.communication.http.file.upload.media

from __future__ import annotations

import threading


class UploadMediaSingleton:
    uploadMedia: UploadMediaSingleton = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.readerFileTypesHashMap: dict = None
        self.writerFileTypesHashMap: dict = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.readerFileTypesHashMap = StdUtil.getInstance().createHashMap()
        self.writerFileTypesHashMap = StdUtil.getInstance().createHashMap()
        hashMap: dict = MediaData.toHashMap()
        set: Set = hashMap.keySet()
        mediaDataNameArray: list[object] = set.toArray()
        size: int = len(mediaDataNameArray)
        for index in range(0, size):
            mediaDataName: str = mediaDataNameArray[index]
            mediaData: MediaData = hashMap.get(mediaDataName)
            self.readerFileTypesHashMap.put(mediaData.getName(), mediaData.getType())
        mediaIOUtil: MediaIOUtil = MediaIOUtil.getInstance()
        RESIZABLE_MEDIA: str = MediaTypeData.getInstance().RESIZABLE_MEDIA
        readerFileTypes: list[str] = mediaIOUtil.getReaderFormatNames()
        for index in range(0, len(readerFileTypes)):
            self.readerFileTypesHashMap.put(readerFileTypes[index], RESIZABLE_MEDIA)
        writerFileTypes: list[str] = mediaIOUtil.getWriterFormatNames()
        for index in range(0, len(writerFileTypes)):
            self.writerFileTypesHashMap.put(writerFileTypes[index], RESIZABLE_MEDIA)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Supported Media Readers: ")
            stringBuffer.append(str(self.readerFileTypesHashMap))
            stringBuffer.append(" Writers: ")
            stringBuffer.append(str(self.writerFileTypesHashMap))
            self.logUtil.putF(str(stringBuffer), self, self.commonStrings.CONSTRUCTOR)
    

    @staticmethod
    def getInstance() -> UploadMediaSingleton:
        with UploadMediaSingleton._lock:
            return UploadMediaSingleton._getInstance_unlocked()

    @staticmethod
    def _getInstance_unlocked() -> UploadMediaSingleton:
        if UploadMediaSingleton.uploadMedia is None:
            UploadMediaSingleton.uploadMedia = UploadMediaSingleton()
        return UploadMediaSingleton.uploadMedia
    

    def isReaderSupported(self, mediaFileType: str) -> bool:
        return self.readerFileTypesHashMap.containsKey(mediaFileType)
    

    def isWriterSupported(self, mediaFileType: str) -> bool:
        return self.readerFileTypesHashMap.containsKey(mediaFileType)
    

    def isSupported(self, mediaFileType: str) -> bool:
        return self.isReaderSupported(mediaFileType) and self.isWriterSupported(mediaFileType)
    

    def isMedia(self, mediaFileType: str, aMediaType: str) -> bool:
        return self.isReaderMedia(mediaFileType, aMediaType) and self.isWriterMedia(mediaFileType, aMediaType)
    

    def isReaderMedia(self, mediaFileType: str, aMediaType: str) -> bool:
        return self.isMedia(mediaFileType, aMediaType, self.readerFileTypesHashMap)
    

    def isWriterMedia(self, mediaFileType: str, aMediaType: str) -> bool:
        return self.isMedia(mediaFileType, aMediaType, self.writerFileTypesHashMap)
    

    # Java overloaded method: Python keeps the last definition
    def isMedia(self, mediaFileType: str, aMediaType: str, hashMap: dict) -> bool:
        if hashMap.containsKey(mediaFileType):
            mediaType: str = hashMap.get(mediaFileType)
            if ((mediaType > aMediaType) - (mediaType < aMediaType)) == 0:
                return True
            else:
                return False
        else:
            return False
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.media.MediaData import MediaData
from org.allbinary.logic.visual.media.MediaIOUtil import MediaIOUtil
from org.allbinary.logic.visual.media.MediaTypeData import MediaTypeData
from org.allbinary.string.CommonStrings import CommonStrings


