# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ABStringComponent:
    NULL_STRING_COMPONENT: ABStringComponent = None
    

    def getBackgroundBasicColor(self) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        return BasicColorFactory.getInstance().WHITE
    

    def __init__(self, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        pass
    

    def getForegroundBasicColor(self) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        return BasicColorFactory.getInstance().WHITE
    

    def setForegroundBasicColor(self, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        pass
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


def _ABStringComponent_NULL_STRING_COMPONENT() -> object:
    from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
    return ABStringComponent(BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)

lazy_static(ABStringComponent, "NULL_STRING_COMPONENT", _ABStringComponent_NULL_STRING_COMPONENT)

