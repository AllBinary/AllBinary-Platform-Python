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



class TouchButtonsPaintableCompositeFactory:
    

    @staticmethod
    def getInstance(inputMappingInterface: InputMappingInterface, basicColor: BasicColor) -> ProcessPaintable:
        from org.allbinary.input.motion.button.TouchButtonsPaintableComposite import TouchButtonsPaintableComposite
        return TouchButtonsPaintableComposite(inputMappingInterface, basicColor)
from org.allbinary.game.input.mapping.InputMappingInterface import InputMappingInterface
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.paint.ProcessPaintable import ProcessPaintable


