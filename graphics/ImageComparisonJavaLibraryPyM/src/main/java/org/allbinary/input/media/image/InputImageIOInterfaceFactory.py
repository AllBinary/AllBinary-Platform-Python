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
# package org.allbinary.input.media.image

from __future__ import annotations



class InputImageIOInterfaceFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(imageType: InputImageType) -> ImageIOInterface:
        from org.allbinary.input.media.image.InputImageType import InputImageType
        from org.allbinary.input.media.image.InputImageType import InputImageType
        from org.allbinary.input.media.image.InputImageType import InputImageType
        if imageType == InputImageType.CAPTURE:
            return CapturedImageInputOutput()
        elif imageType == InputImageType.COMPARISON:
            return ComparisonImageInputOutput()
        elif imageType == InputImageType.MOTION:
            return MotionRectanglesImageInputOutput()
        else:
            raise Exception("No ImageIOInterface for: " + str(imageType))
from org.allbinary.input.media.image.capture.CapturedImageInputOutput import CapturedImageInputOutput
from org.allbinary.media.image.comparison.ComparisonImageInputOutput import ComparisonImageInputOutput
from org.allbinary.media.image.comparison.motion.MotionRectanglesImageInputOutput import MotionRectanglesImageInputOutput
from org.allbinary.media.image.io.ImageIOInterface import ImageIOInterface


