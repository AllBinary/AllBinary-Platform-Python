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
# package org.allbinary.graphics.color

from __future__ import annotations



class BasicColorFactory:
    instance: BasicColorFactory = None

    def _init_fields(self) -> None:
        self.NULL_COLOR: BasicColor = self.createInstanceARGB(255, 255, 255, 255, "null color")
        self.TAN: BasicColor = self.createInstance(0xE9D8B5)
        self.SKIN_PINK: BasicColor = self.createInstance(0xFDCECE)
        self.RED: BasicColor = self.createInstanceAN(BasicColorUtil.getInstance().ALPHA, 0xFF0000, "red")
        self.LIGHT_RED: BasicColor = self.createInstanceAN(BasicColorUtil.getInstance().ALPHA, 0xFFA0A0, "light red")
        self.DARK_GREEN: BasicColor = self.createInstance(0x00FF00)
        self.GREEN: BasicColor = self.createInstanceAN(BasicColorUtil.getInstance().ALPHA, 0x00DD00, "green")
        self.LIGHT_GREEN: BasicColor = self.createInstance(0x007700)
        self.PURPLE: BasicColor = self.createInstanceAN(BasicColorUtil.getInstance().ALPHA, 0x400040, "purple")
        self.BLUE: BasicColor = self.createInstanceAN(BasicColorUtil.getInstance().ALPHA, 0x0000FF, "blue")
        self.LIGHT_BLUE: BasicColor = self.createInstance(0x00aaff)
        self.VERY_LIGHT_BLUE: BasicColor = self.createInstance(0x000033)
        self.PUCE: BasicColor = self.createInstance(0xFF00AA)
        self.AQUA: BasicColor = self.createInstance(0x00FFFF)
        self.YELLOW: BasicColor = self.createInstanceAN(BasicColorUtil.getInstance().ALPHA, 0xFFFF00, "yellow")
        self.PINK: BasicColor = self.createInstance(0xFF00FF)
        self.BLACK: BasicColor = self.createInstanceAN(BasicColorUtil.getInstance().ALPHA, 0x000000, "black")
        self.GREY: BasicColor = self.createInstanceAN(BasicColorUtil.getInstance().ALPHA, 0xAAAAAA, "grey")
        self.LIGHT_GREY: BasicColor = self.createInstance(0xC0C0C0)
        self.DARK_GREY: BasicColor = self.createInstance(0x404040)
        self.ORANGE: BasicColor = self.createInstance(0xe07718)
        self.BROWN: BasicColor = self.createInstance(0x956B00)
        self.WHITE: BasicColor = self.createInstance(0xFFFFFF)
        self.TRANSPARENT_COLOR: BasicColor = self.createInstanceAN(0x00000000, 0x000000, StringUtil.getInstance().EMPTY_STRING)
        self.TRANSPARENT_GREY: BasicColor = self.createInstanceAN(0x52000000, 0xECECEC, StringUtil.getInstance().EMPTY_STRING)
        self.TRANSPARENT_BLACK: BasicColor = self.createInstanceAN(0x52000000, 0x000000, StringUtil.getInstance().EMPTY_STRING)
        self.TRANSPARENT_RED: BasicColor = self.createInstanceAN(0x52000000, 0xFF0000, StringUtil.getInstance().EMPTY_STRING)
        self.CLEAR_COLOR: BasicColor = self.BLACK
        self.BORDER_COLOR: BasicColor = self.WHITE

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicColorFactory:
        return BasicColorFactory.instance
    

    def createInstance(self, value: int) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.graphics.color.BasicColorUtil import BasicColorUtil
        return BasicColor(BasicColorUtil.getInstance().ALPHA, value, StringUtil.getInstance().EMPTY_STRING)
    

    def createInstanceA(self, alphaValue: int, value: int) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        return BasicColor(alphaValue, value, StringUtil.getInstance().EMPTY_STRING)
    

    def createInstanceAN(self, alphaValue: int, value: int, name: str) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        return BasicColor(alphaValue, value, name)
    

    def createInstanceARGB(self, alphaValue: int, r: int, g: int, b: int, name: str) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        ALPHA_MASK: int = 0xFF000000
        return BasicColor(alphaValue, ((alphaValue << 24) & ALPHA_MASK) + ((r << 16) & 0x00FF0000) + ((g << 8) & 0x0000FF00) + (b & 0x000000FF), StringUtil.getInstance().EMPTY_STRING)
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.string.StringUtil import StringUtil
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsProperty import JsProperty
from org.allbinary.graphics.color.BasicColorUtil import BasicColorUtil


BasicColorFactory.instance = BasicColorFactory()

