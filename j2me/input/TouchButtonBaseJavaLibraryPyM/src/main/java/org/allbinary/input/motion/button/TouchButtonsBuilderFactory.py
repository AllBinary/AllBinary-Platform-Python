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



class TouchButtonsBuilderFactory:
    NO_TOUCH_BUTTON_BUILDER_FACTORY: TouchButtonsBuilderFactory = None
    

    def getInstance(self) -> BaseTouchInput:
        from org.allbinary.input.motion.button.NoButtonsTouchInputFactory import NoButtonsTouchInputFactory
        return NoButtonsTouchInputFactory.getInstance()


TouchButtonsBuilderFactory.NO_TOUCH_BUTTON_BUILDER_FACTORY = TouchButtonsBuilderFactory()

