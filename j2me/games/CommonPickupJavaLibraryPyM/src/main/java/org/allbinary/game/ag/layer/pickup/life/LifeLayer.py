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
# package org.allbinary.game.ag.layer.pickup.life

from __future__ import annotations

from org.allbinary.game.ag.life.LifeVisitorInterface import LifeVisitorInterface
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


class LifeLayer(AllBinaryLayer, LifeVisitorInterface):
    

    def __init__(self) -> None:
        super().__init__(StringUtil.getInstance().EMPTY_STRING, Rectangle(PointFactory.getInstance().ZERO_ZERO, 0, 0), ViewPosition.getInstanceD())
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def visit(self, lifeInterface: Life) -> None:
        lifeInterface.add(((int(1) + 32768) % 65536 - 32768))
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.ag.life.Life import Life
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.view.ViewPosition import ViewPosition


