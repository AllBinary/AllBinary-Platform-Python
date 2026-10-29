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
# package org.allbinary.graphics.form

from __future__ import annotations



class CommandCurrentSelectionFormFactory:
    

    # throws Exception
    @staticmethod
    def getInstance(title: str, items: list[ABCustomItem], rectangle: Rectangle, formType: FormType, border: int, moveForSmallScreen: bool, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> ScrollSelectionForm:
        from org.allbinary.graphics.form.ScrollSelectionFormNoneFactory import ScrollSelectionFormNoneFactory
        from org.allbinary.graphics.form.CommandCurrentSelectionForm import CommandCurrentSelectionForm
        if Features.getInstance().isFeature(TouchFeatureFactory.getInstance().TOUCH_ENABLED):
            scrollSelectionForm: ScrollSelectionForm = CommandCurrentSelectionForm(title, items, border, moveForSmallScreen, backgroundBasicColor, foregroundBasicColor)
            scrollSelectionForm.init(rectangle, formType)
            return scrollSelectionForm
        else:
            return ScrollSelectionFormNoneFactory.getInstance()
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.TouchFeatureFactory import TouchFeatureFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


