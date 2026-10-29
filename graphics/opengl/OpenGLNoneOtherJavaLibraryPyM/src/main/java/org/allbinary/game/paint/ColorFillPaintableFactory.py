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
# package org.allbinary.game.paint

from __future__ import annotations



class ColorFillPaintableFactory:
    instance: ColorFillPaintableFactory = None
    

    @staticmethod
    def getInstance() -> ColorFillPaintableFactory:
        return ColorFillPaintableFactory.instance
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, basicColor: BasicColor, forThreedCanvas: bool) -> ColorFillBasePaintable:
        from org.allbinary.game.paint.ColorFillPaintable import ColorFillPaintable
        from org.allbinary.game.paint.OverScanColorFillPaintable import OverScanColorFillPaintable
        operatingSystem: GenericOperatingSystem = OperatingSystemFactory.getInstance().getOperatingSystemInstance()
        if operatingSystem.isOverScan():
            return OverScanColorFillPaintable(basicColor)
        else:
            return ColorFillPaintable(basicColor)
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory


ColorFillPaintableFactory.instance = ColorFillPaintableFactory()

