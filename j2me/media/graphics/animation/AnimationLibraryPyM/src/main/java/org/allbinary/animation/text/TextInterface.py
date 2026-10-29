# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.animation.text

from __future__ import annotations



# Java interface
class TextInterface:
    

    def setTextWithOnMeasure(self, text: str, textChangeListener: TextChangeListener) -> None:
        raise NotImplementedError()
    

    def getText(self) -> str:
        raise NotImplementedError()
    

    def setText(self, text: str) -> None:
        raise NotImplementedError()
    

    def getFontHeight(self) -> int:
        raise NotImplementedError()
    

    def getWidth(self) -> int:
        raise NotImplementedError()


