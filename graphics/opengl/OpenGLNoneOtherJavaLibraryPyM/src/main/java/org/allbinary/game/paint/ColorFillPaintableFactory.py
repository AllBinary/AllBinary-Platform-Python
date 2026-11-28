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

from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import lazy_static


class ColorFillPaintableFactory:
    instance: ColorFillPaintableFactory = None
    

    @staticmethod
    def getInstance_j0() -> ColorFillPaintableFactory:
        return ColorFillPaintableFactory.instance
    

    def getInstance_j2(self, basicColor: BasicColor, forThreedCanvas: bool) -> ColorFillBasePaintable:
        from org.allbinary.game.paint.ColorFillPaintable import ColorFillPaintable
        from org.allbinary.game.paint.OverScanColorFillPaintable import OverScanColorFillPaintable
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
        from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
        operatingSystem: GenericOperatingSystem = OperatingSystemFactory.getInstance().getOperatingSystemInstance()
        if java_predicate(operatingSystem, "isOverScan"):
            return OverScanColorFillPaintable(basicColor)
        else:
            return ColorFillPaintable(basicColor)

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
# from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory


def _ColorFillPaintableFactory_instance() -> object:
    return ColorFillPaintableFactory()

lazy_static(ColorFillPaintableFactory, "instance", _ColorFillPaintableFactory_instance)

