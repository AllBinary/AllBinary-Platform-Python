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
# package org.allbinary.game.paint

from __future__ import annotations

from org.allbinary.graphics.color.ColorChangeListener import ColorChangeListener
from org.allbinary.game.paint.BasicGameDemoPaintable import BasicGameDemoPaintable


class GameScrollMenuPaintable(BasicGameDemoPaintable, ColorChangeListener):
    

    def __init__(self, mainDemoStatePaintable: Paintable, ownershipPaintable: Paintable, helpPaintableInterface: Paintable, basicColor: BasicColor) -> None:
        super().__init__(mainDemoStatePaintable, ownershipPaintable, helpPaintableInterface)
        self.setColor(basicColor)
        ColorChangeEventHandler.getInstance().addListenerInterface(self)
    

    def setState(self, state: int) -> None:
        self.setCurrentStatePaintable(self.getMainDemoStatePaintable())
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        pass
    

    def setColor(self, basicColor: BasicColor) -> None:
        mainGameDemoStatePaintable: MainGameDemoStatePaintable = self.getMainDemoStatePaintable()
        formPaintable: FormPaintable = mainGameDemoStatePaintable.getMenuPaintableInterface()
        scrollSelectionForm: ScrollSelectionForm = formPaintable.getForm()
        mainGameDemoStatePaintable.getOwnershipPaintableInterface().setBasicColorP(basicColor)
        scrollSelectionForm.setButtonBasicColor(basicColor)
        item: ABTextItem = None
        stringComponent: ABStringComponent = None
        for index in range(scrollSelectionForm.size() - 1, 0 - 1, -1):
            item = scrollSelectionForm.get(index)
            stringComponent = item.getLabelStringComponent()
            if stringComponent is not None:
                stringComponent.setForegroundBasicColor(basicColor)
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.ColorChangeEventHandler import ColorChangeEventHandler
from org.allbinary.graphics.form.FormPaintable import FormPaintable
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.graphics.form.item.ABStringComponent import ABStringComponent
from org.allbinary.graphics.form.item.ABTextItem import ABTextItem
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


