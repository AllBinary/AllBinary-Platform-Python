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
# package org.allbinary.bounds.event

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class BoundsChangeEvent(AllBinaryEventObject):
    

    def __init__(self, rectangle: Rectangle) -> None:
        from org.allbinary.graphics.Rectangle import Rectangle
        super().__init__(rectangle)
    

    def getRectangle(self) -> Rectangle:
        from org.allbinary.graphics.Rectangle import Rectangle
        return self.getSource()
# from org.allbinary.graphics.Rectangle import Rectangle


