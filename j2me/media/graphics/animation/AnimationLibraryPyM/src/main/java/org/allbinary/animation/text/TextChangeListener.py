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



class TextChangeListener:
    instance: TextChangeListener = None
    

    @staticmethod
    def getInstance() -> TextChangeListener:
        return TextChangeListener.instance
    

    def onMeasure(self) -> None:
        pass


TextChangeListener.instance = TextChangeListener()

