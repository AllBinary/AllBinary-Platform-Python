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
# package org.allbinary.animation.text

from __future__ import annotations

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface


class CustomTextBoxIndexedAnimationFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.scaleProperties: ScaleProperties = None
        self.maxLength: int = None
    

    def __init__(self, fontSize: int, maxLength: int) -> None:
        self._init_fields()
        self.scaleProperties = ScaleProperties()
        self.scaleProperties.scaleHeight = fontSize
        self.maxLength = maxLength
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.text.CustomTextBox2 import CustomTextBox2
        from org.allbinary.animation.text.CustomTextBoxIndexedAnimation import CustomTextBoxIndexedAnimation
        abToGBUtil: ABToGBUtil = ABToGBUtil.getInstance()
        abCanvas: AllBinaryGameCanvas = abToGBUtil.abCanvas
        font: Font = Font.getFont(Font.FACE_SYSTEM, Font.STYLE_PLAIN, self.scaleProperties.scaleHeight)
        customTextBox: CustomTextBox = CustomTextBox2(abCanvas.getCustomCommandListener(), StringUtil.getInstance().EMPTY_STRING, StringUtil.getInstance().EMPTY_STRING, self.maxLength, TextField.ANY, font, abCanvas.getLayerManager().getBackgroundBasicColor(), abCanvas.getLayerManager().getForegroundBasicColor())
        return CustomTextBoxIndexedAnimation(customTextBox)
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        fontSize: int = self.scaleProperties.scaleHeight
        self.scaleProperties = scaleProperties
        if self.scaleProperties.scaleHeight < 6:
            self.scaleProperties.scaleHeight = fontSize
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.TextField import TextField
from org.allbinary.graphics.form.item.CustomTextBox import CustomTextBox
from org.allbinary.animation.Animation import Animation
from org.allbinary.game.canvas.ABToGBUtil import ABToGBUtil
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.media.ScaleProperties import ScaleProperties


