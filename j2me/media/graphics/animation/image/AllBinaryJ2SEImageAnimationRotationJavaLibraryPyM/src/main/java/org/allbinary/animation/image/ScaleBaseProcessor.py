# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.animation.image

from __future__ import annotations



class ScaleBaseProcessor:
    instance: ScaleBaseProcessor = None
    

    @staticmethod
    def getInstance() -> ScaleBaseProcessor:
        return ScaleBaseProcessor.instance
    

    def update(self, originalImage: Image, originalImageArray: list[Image], imageToShowArray: list[Image], index: int, scaleX: float, scaleY: float, maxScaleX: float, maxScaleY: float) -> None:
        pass
# from javax.microedition.lcdui.Image import Image


ScaleBaseProcessor.instance = ScaleBaseProcessor()

