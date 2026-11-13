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


class Anchor:
    TOP_LEFT: int = None
# from javax.microedition.lcdui.Graphics import Graphics


def _Anchor_TOP_LEFT() -> object:
    from javax.microedition.lcdui.Graphics import Graphics
    return Graphics.TOP & Graphics.LEFT

lazy_static(Anchor, "TOP_LEFT", _Anchor_TOP_LEFT)

