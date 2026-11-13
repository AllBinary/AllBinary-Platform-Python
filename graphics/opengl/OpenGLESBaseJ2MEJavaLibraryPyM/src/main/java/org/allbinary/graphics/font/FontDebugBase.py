# Generated Code Do Not Modify
# package org.allbinary.graphics.font

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


#OpenGLESBaseJ2MEJavaLibrary
class FontDebugBase:
    instanceBase: FontDebugBase = None

    def _init_fields(self) -> None:
        self.SET_FONT: str = "setFont"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> FontDebugBase:
        return FontDebugBase.instanceBase
    

    def debugMetrics(self, currentFont: Font, convertedTextSize: float, displayMetrics: object, stringBuffer: StringMaker) -> None:
        from javax.microedition.lcdui.Font import Font
        from org.allbinary.logic.string.StringMaker import StringMaker
        pass
    

    def debugDpi(self, densityDpi: int, stringBuffer: StringMaker) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        pass
    

    def debugDimension(self, currentFont: Font, convertedTextSize: float, longestDimensionTotalPixels: int, stringBuffer: StringMaker) -> None:
        from javax.microedition.lcdui.Font import Font
        from org.allbinary.logic.string.StringMaker import StringMaker
        pass
# from javax.microedition.lcdui.Font import Font
# from org.allbinary.logic.string.StringMaker import StringMaker


def _FontDebugBase_instanceBase() -> object:
    return FontDebugBase()

lazy_static(FontDebugBase, "instanceBase", _FontDebugBase_instanceBase)

