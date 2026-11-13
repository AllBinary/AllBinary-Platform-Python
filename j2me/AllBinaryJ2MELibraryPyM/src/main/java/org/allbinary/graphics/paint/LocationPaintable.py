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
# package org.allbinary.graphics.paint

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.graphics.paint.LocationPaintableInterface import LocationPaintableInterface


class LocationPaintable(LocationPaintableInterface):
    instance: LocationPaintable = None
    

    @staticmethod
    def getInstance() -> LocationPaintable:
        return LocationPaintable.instance
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
# from javax.microedition.lcdui.Graphics import Graphics


def _LocationPaintable_instance() -> object:
    return LocationPaintable()

lazy_static(LocationPaintable, "instance", _LocationPaintable_instance)

