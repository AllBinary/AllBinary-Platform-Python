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



class ImageSwtUtil:
    instance: ImageSwtUtil = None
    

    @staticmethod
    def getInstance() -> ImageSwtUtil:
        return ImageSwtUtil.instance
from org.eclipse.swt.graphics.Color import Color
from org.eclipse.swt.graphics.RGB import RGB
from org.microemu.app.BareMain import BareMain


ImageSwtUtil.instance = ImageSwtUtil()

