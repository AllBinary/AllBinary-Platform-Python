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
# package org.allbinary.image

from __future__ import annotations



class ImageTypeUtil:
    SINGLETON: ImageTypeUtil = None

    def _init_fields(self) -> None:
        self.PNG: str = "png"
        self.JPG: str = "jpg"
        self.GIF: str = "gif"
        self.list_: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        self._init_fields()
        self.list_.add(self.JPG)
        self.list_.add(self.GIF)
        self.list_.add(self.PNG)
    

    def isSupported(self, mediaFileType: str) -> bool:
        mediaFileType = mediaFileType.lower()
        for index in range(self.list_.size() - 1, 0 - 1, -1):
            name: str = self.list_.objectArray[index]
            if ((mediaFileType > name) - (mediaFileType < name)) == 0:
                return True
        return False
    

    @staticmethod
    def getInstance() -> ImageTypeUtil:
        return ImageTypeUtil.SINGLETON
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.image.BasicArrayListD import BasicArrayListD


ImageTypeUtil.SINGLETON = ImageTypeUtil()

