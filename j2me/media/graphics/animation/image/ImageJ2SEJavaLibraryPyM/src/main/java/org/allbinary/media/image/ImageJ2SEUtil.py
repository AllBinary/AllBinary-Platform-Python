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

from java.lang.JavaRuntimeStatic import lazy_static


class ImageJ2SEUtil:
    instance: ImageJ2SEUtil = None

    def _init_fields(self) -> None:
        self.TRANSPARENT_COLOR: Color = Color(0, 0, 0, 0)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ImageJ2SEUtil:
        return ImageJ2SEUtil.instance
# from java.awt.Color import Color


def _ImageJ2SEUtil_instance() -> object:
    return ImageJ2SEUtil()

lazy_static(ImageJ2SEUtil, "instance", _ImageJ2SEUtil_instance)

