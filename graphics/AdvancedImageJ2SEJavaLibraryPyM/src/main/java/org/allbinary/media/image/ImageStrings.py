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



class ImageStrings:
    instance: ImageStrings = None

    def _init_fields(self) -> None:
        self.PNG: str = "PNG"
        self.PNG_EXTENSION: str = ".png"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ImageStrings:
        return ImageStrings.instance


ImageStrings.instance = ImageStrings()

