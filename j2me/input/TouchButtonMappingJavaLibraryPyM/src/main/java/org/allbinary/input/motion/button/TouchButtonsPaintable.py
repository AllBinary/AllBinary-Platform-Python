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
# package org.allbinary.input.motion.button

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class TouchButtonsPaintable(Paintable):
    def _java_defaults(self):
        vars(self).setdefault("foregroundBasicColor", None)
        vars(self).setdefault("foregroundColor", 0)
        vars(self).setdefault("basicSetColorUtil", None)
        vars(self).setdefault("touchButtonFactory", None)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
        if "foregroundBasicColor" not in vars(self): self.foregroundBasicColor: BasicColor = None
        if "foregroundColor" not in vars(self): self.foregroundColor: int = 0
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.touchButtonFactory: TouchButtonFactory = TouchButtonFactory.getInstance()
    

    def __init__(self, basicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__()
        __class__._init_fields(self)
        self.foregroundBasicColor = basicColor
        self.foregroundColor = int(basicColor)
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.util.BasicArrayList import BasicArrayList
        list_: BasicArrayList = self.touchButtonFactory.getList()
        self.basicSetColorUtil.setBasicColorP3(graphics, self.foregroundBasicColor, self.foregroundColor)
        touchButton: TouchButton = None
        index = list_.size()
        while (index := index - 1) >= 0:
            touchButton = list_.objectArray[index]
            touchButton.paint(graphics)
        index = list_.size()
        while (index := index - 1) >= 0:
            touchButton = list_.objectArray[index]
            touchButton.paintHint(graphics)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
# from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.input.motion.button.TouchButtonFactory import TouchButtonFactory


