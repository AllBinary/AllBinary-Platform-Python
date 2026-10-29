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



class BasicColorSetUtil:
    instance: BasicColorSetUtil = None
    

    @staticmethod
    def getInstance() -> BasicColorSetUtil:
        return BasicColorSetUtil.instance
    

    def __init__(self) -> None:
        pass
    

    def setBasicColorP(self, graphics: Graphics, basicColor: BasicColor) -> None:
        graphics.setColor(int(basicColor))
    

    def setBasicColorP3(self, graphics: Graphics, basicColor: BasicColor, value: int) -> None:
        graphics.setColor(value)
# from javax.microedition.lcdui.Graphics import Graphics


BasicColorSetUtil.instance = BasicColorSetUtil()

