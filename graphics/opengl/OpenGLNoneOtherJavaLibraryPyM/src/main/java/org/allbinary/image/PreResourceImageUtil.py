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

from java.lang.JavaRuntimeStatic import lazy_static


class PreResourceImageUtil:
    instance: PreResourceImageUtil = None
    

    @staticmethod
    def getInstance() -> PreResourceImageUtil:
        return PreResourceImageUtil.instance
    

    def encapsulate(self, image: Image) -> Image:
        from javax.microedition.lcdui.Image import Image
        return image
    

    def updateGL(self, gl: GL, image: Image) -> None:
        from javax.microedition.khronos.opengles.GL import GL
        from javax.microedition.lcdui.Image import Image
        pass
    

    def update(self, graphics: Graphics, image: Image) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from javax.microedition.lcdui.Image import Image
        pass
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image


def _PreResourceImageUtil_instance() -> object:
    return PreResourceImageUtil()

lazy_static(PreResourceImageUtil, "instance", _PreResourceImageUtil_instance)

