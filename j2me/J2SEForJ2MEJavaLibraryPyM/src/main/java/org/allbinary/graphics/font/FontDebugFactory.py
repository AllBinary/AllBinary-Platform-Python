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
# package org.allbinary.graphics.font

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class FontDebugFactory:
    instance: FontDebugFactory = None
    

    @staticmethod
    def getInstance() -> FontDebugFactory:
        return FontDebugFactory.instance
    

    def setFont(self, font: Font, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        graphics.setFont(font)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics


def _FontDebugFactory_instance() -> object:
    return FontDebugFactory()

lazy_static(FontDebugFactory, "instance", _FontDebugFactory_instance)

