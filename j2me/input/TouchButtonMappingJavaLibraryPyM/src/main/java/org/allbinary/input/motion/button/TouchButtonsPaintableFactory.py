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



class TouchButtonsPaintableFactory:
    

    @staticmethod
    def getInstance(basicColor: BasicColor) -> Paintable:
        from org.allbinary.input.motion.button.TouchButtonsPaintable import TouchButtonsPaintable
        return TouchButtonsPaintable(basicColor)
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.paint.Paintable import Paintable


