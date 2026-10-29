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



class MediaTypeData:
    instance: MediaTypeData = None

    def _init_fields(self) -> None:
        self.RESIZABLE_MEDIA: str = "RESIZABLE_MEDIA"
        self.NOT_RESIZABLE_MEDIA: str = "NOT_RESIZABLE_MEDIA"
    

    @staticmethod
    def getInstance() -> MediaTypeData:
        return MediaTypeData.instance
    

    def __init__(self) -> None:
        self._init_fields()


MediaTypeData.instance = MediaTypeData()

