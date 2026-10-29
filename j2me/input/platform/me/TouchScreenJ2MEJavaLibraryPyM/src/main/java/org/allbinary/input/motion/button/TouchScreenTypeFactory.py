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



class TouchScreenTypeFactory:
    instance: TouchScreenTypeFactory = None
    

    @staticmethod
    def getInstance() -> TouchScreenTypeFactory:
        return TouchScreenTypeFactory.instance
    

    def TouchScreenTypeFactory(self) -> None:
        from org.allbinary.input.motion.button.TouchScreenFactory import TouchScreenFactory
        touchScreenFactory: TouchScreenFactory = TouchScreenFactory.getInstance()
        touchScreenFactory.setTouch(True)


TouchScreenTypeFactory.instance = TouchScreenTypeFactory()

