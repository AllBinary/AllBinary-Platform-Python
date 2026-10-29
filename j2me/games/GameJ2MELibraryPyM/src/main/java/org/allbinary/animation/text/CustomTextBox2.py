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

from org.allbinary.graphics.form.item.CustomTextBox import CustomTextBox


class CustomTextBox2(CustomTextBox):
    

    def __init__(self, cmdListener: CommandListener, label: str, text: str, maxSize: int, constraints: int, font: Font, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(cmdListener, label, text, maxSize, constraints, font, backgroundBasicColor, foregroundBasicColor)
        self.getTextFieldItem().setFocus(True)
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Font import Font
from org.allbinary.graphics.color.BasicColor import BasicColor


