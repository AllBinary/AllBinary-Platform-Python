# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


@java_inherited_overloads
class ABCustomImageItem(ABCustomItem):
    def _java_defaults(self):
        vars(self).setdefault("yOffset", 0)

    def _init_fields(self) -> None:
        self.yOffset: int = 0
    

    def __init__(self, label: str, image: Image, layout: int, altText: str, basicColor: BasicColor, yOffset: int) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(label, basicColor, basicColor)
        __class__._init_fields(self)
    

    def getImage(self) -> Image:
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.NullImage import NullImage
        return NullImage.NULL_IMAGE
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
# from org.allbinary.graphics.color.BasicColor import BasicColor


