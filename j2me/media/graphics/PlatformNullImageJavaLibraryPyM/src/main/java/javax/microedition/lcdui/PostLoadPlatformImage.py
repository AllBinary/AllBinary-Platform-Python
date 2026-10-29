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
# package javax.microedition.lcdui

from __future__ import annotations

from javax.microedition.lcdui.PlatformImage import PlatformImage


#PlatformNullImageJavaLibrary
class PostLoadPlatformImage(PlatformImage):
    instance: PostLoadPlatformImage = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> PostLoadPlatformImage:
        return PostLoadPlatformImage.instance


PostLoadPlatformImage.instance = PostLoadPlatformImage()

