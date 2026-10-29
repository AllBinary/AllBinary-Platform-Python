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
# package org.allbinary.logic.visual.media

from __future__ import annotations

from org.allbinary.logic.StdUtil import StdUtil


class MediaData:
    hashMap: dict = StdUtil.getInstance().createHashMap()

    def _init_fields(self) -> None:
        self.name: str = None
        self.type_: str = None
        self.extension: str = None
    

    def __init__(self, a_Name: str) -> None:
        from org.allbinary.logic.visual.media.MediaTypeData import MediaTypeData
        self._init_fields()
        self.name = a_Name
        self.extension = "." + self.name
        self.type_ = MediaTypeData.getInstance().NOT_RESIZABLE_MEDIA
        MediaData.hashMap.put(a_Name, self)
    

    def getName(self) -> str:
        return self.name
    

    def getType(self) -> str:
        return self.type_
    

    def getExtension(self) -> str:
        return self.extension
    

    def isConvertableTo(self, mediaData: MediaData) -> bool:
        from org.allbinary.logic.visual.media.MediaDataFactory import MediaDataFactory
        from org.allbinary.logic.visual.media.MediaDataFactory import MediaDataFactory
        if self == MediaDataFactory.getInstance().GIF and mediaData == MediaDataFactory.getInstance().JPG:
            return True
        return False
    

    def toString(self) -> str:
        return self.getName()

    def __str__(self) -> str:
        return self.toString()
    

    # throws Exception
    @staticmethod
    def get(a_Name: str) -> MediaData:
        mediaData: MediaData = MediaData.hashMap.get(a_Name)
        if mediaData is not None:
            return mediaData
        else:
            raise Exception("No Such MediaData")
    

    @staticmethod
    def getDefault() -> MediaData:
        from org.allbinary.logic.visual.media.MediaDataFactory import MediaDataFactory
        return MediaDataFactory.getInstance().JPG
    

    @staticmethod
    def toHashMap() -> dict:
        return MediaData.hashMap
# from java.util.HashMap import HashMap


