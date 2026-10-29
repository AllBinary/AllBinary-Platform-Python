# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


class ABCustomImageItem(ABCustomItem):

    def _init_fields(self) -> None:
        self.yOffset: int = 0
    

    def __init__(self, label: str, image: Image, layout: int, altText: str, basicColor: BasicColor, yOffset: int) -> None:
        super().__init__(label, basicColor, basicColor)
        self._init_fields()
    

    def getImage(self) -> Image:
        return NullImage.NULL_IMAGE
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.graphics.color.BasicColor import BasicColor


