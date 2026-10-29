# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations



class RTSScrollSelectionFormFactory:
    

    # throws Exception
    @staticmethod
    def getInstance(formLabel: str, items: list[ABCustomItem]) -> ScrollSelectionForm:
        basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        touchButtonLocationHelper: TouchButtonLocationHelper = TouchButtonLocationHelper()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        menuX: int = CommonButtons.getInstance().STANDARD_BUTTON_SIZE + touchButtonLocationHelper.getColumnsRemainderHalf()
        width: int = displayInfo.getLastWidth() - (menuX * 2)
        menuRectangle: Rectangle = Rectangle(PointFactory.getInstance().createXY(menuX, 16), width, CommonButtons.getInstance().STANDARD_BUTTON_SIZE)
        return MultipleScrollSelectionHorizontalForm.createForm(formLabel, items, menuRectangle, FormTypeFactory.getInstance().HORIZONTAL_FORM, 0, basicColorFactory.BLACK, basicColorFactory.WHITE)
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.form.FormTypeFactory import FormTypeFactory
from org.allbinary.graphics.form.MultipleScrollSelectionHorizontalForm import MultipleScrollSelectionHorizontalForm
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.input.motion.button.CommonButtons import CommonButtons
from org.allbinary.input.motion.button.TouchButtonLocationHelper import TouchButtonLocationHelper


