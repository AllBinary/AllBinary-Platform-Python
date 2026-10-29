# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


class ABStringComponent:
    NULL_STRING_COMPONENT: ABStringComponent = None
    

    def getBackgroundBasicColor(self) -> BasicColor:
        return BasicColorFactory.getInstance().WHITE
    

    def __init__(self, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        pass
    

    def getForegroundBasicColor(self) -> BasicColor:
        return BasicColorFactory.getInstance().WHITE
    

    def setForegroundBasicColor(self, foregroundBasicColor: BasicColor) -> None:
        pass
from org.allbinary.graphics.color.BasicColor import BasicColor


ABStringComponent.NULL_STRING_COMPONENT = ABStringComponent(BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)

