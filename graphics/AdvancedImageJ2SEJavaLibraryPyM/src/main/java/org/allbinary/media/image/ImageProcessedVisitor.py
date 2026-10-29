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
# package org.allbinary.media.image

from __future__ import annotations

from org.allbinary.media.image.ImageProcessorInputCompositeInterface import ImageProcessorInputCompositeInterface


# Java interface
class ImageProcessedVisitor(ImageProcessorInputCompositeInterface):
    

    # throws IOException
    def visit(self, generatedBufferedImage: BufferedImage, nameEnding: str, index: int) -> None:
        raise NotImplementedError()
# from java.awt.image.BufferedImage import BufferedImage
# from java.io.IOException import IOException


