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
# package org.allbinary.media.image

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ImageCompleteUtil:
    instance: ImageCompleteUtil = None
    

    @staticmethod
    def getInstance() -> ImageCompleteUtil:
        return ImageCompleteUtil.instance
    

    # throws Exception
    def waitForImage(self, image: Image, name: str) -> None:
        from javax.microedition.lcdui.Image import Image
        pass
# from javax.microedition.lcdui.Image import Image


def _ImageCompleteUtil_instance() -> object:
    return ImageCompleteUtil()

lazy_static(ImageCompleteUtil, "instance", _ImageCompleteUtil_instance)

