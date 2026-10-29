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

from org.allbinary.graphics.paint.Paintable import Paintable


class NullPaintable(Paintable):
    SINGLETON: NullPaintable = None
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> Paintable:
        return NullPaintable.SINGLETON


NullPaintable.SINGLETON = NullPaintable()

