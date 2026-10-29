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
# package org.allbinary.graphics.canvas.transition.progress

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class ProgressCanvasFactory:
    PROGRESS_FORM_SCREEN: object = NullUtil.getInstance().NULL_OBJECT
    

    @staticmethod
    def getInstance() -> ProgressCanvas:
        from org.allbinary.graphics.canvas.transition.progress.AndroidBasicTitleProgressBar import AndroidBasicTitleProgressBar
        if ProgressCanvasFactory.PROGRESS_FORM_SCREEN == NullUtil.getInstance().NULL_OBJECT:
            ProgressCanvasFactory.PROGRESS_FORM_SCREEN = AndroidBasicTitleProgressBar(StringUtil.getInstance().EMPTY_STRING, BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)
        return ProgressCanvasFactory.PROGRESS_FORM_SCREEN
    

    @staticmethod
    def getLazyInstance() -> PaintableInterface:
        return NullPaintable.getInstance()
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
from org.allbinary.logic.string.StringUtil import StringUtil


