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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations



class FormUtil:
    instance: FormUtil = None
    

    @staticmethod
    def getInstance() -> FormUtil:
        return FormUtil.instance
    

    def createFormRectangle(self) -> Rectangle:
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        pointFactory: PointFactory = PointFactory.getInstance()
        rectangle: Rectangle = Rectangle(pointFactory.createXY(30, 10), displayInfo.getLastWidth() - 30, displayInfo.getLastHeight() - 35)
        return rectangle
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.logic.communication.log.LogUtil import LogUtil


FormUtil.instance = FormUtil()

