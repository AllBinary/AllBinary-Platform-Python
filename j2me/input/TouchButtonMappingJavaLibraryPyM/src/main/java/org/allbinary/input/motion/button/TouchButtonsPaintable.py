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

from org.allbinary.graphics.paint.Paintable import Paintable


class TouchButtonsPaintable(Paintable):

    def _init_fields(self) -> None:
        self.foregroundBasicColor: BasicColor = None
        self.foregroundColor: int = None
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.touchButtonFactory: TouchButtonFactory = TouchButtonFactory.getInstance()
    

    def __init__(self, basicColor: BasicColor) -> None:
        super().__init__()
        self._init_fields()
        self.foregroundBasicColor = basicColor
        self.foregroundColor = int(basicColor)
    

    def paint(self, graphics: Graphics) -> None:
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
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.input.motion.button.TouchButtonFactory import TouchButtonFactory


