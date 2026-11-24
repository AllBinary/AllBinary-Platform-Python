# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package javax.microedition.lcdui

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class NullImage:
    NULL_IMAGE_ARRAY: list[Image] = [None] * (0)
    NULL_IMAGE: Image = None


def _NullImage_NULL_IMAGE() -> object:
    from javax.microedition.lcdui.Image import Image
    return Image()

lazy_static(NullImage, "NULL_IMAGE", _NullImage_NULL_IMAGE)

