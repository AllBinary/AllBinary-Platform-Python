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
# package org.allbinary.graphics

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class RectangleFactory:
    SINGLETON: Rectangle = None
    ARRAY_OF_ARRAYS: list[list[Rectangle]] = [[None] * (0) for _ in range(0)]


def _RectangleFactory_SINGLETON() -> object:
    from org.allbinary.graphics.Rectangle import Rectangle
    from org.allbinary.graphics.PointFactory import PointFactory
    return Rectangle(PointFactory.getInstance().ZERO_ZERO, 0, 0)

lazy_static(RectangleFactory, "SINGLETON", _RectangleFactory_SINGLETON)

