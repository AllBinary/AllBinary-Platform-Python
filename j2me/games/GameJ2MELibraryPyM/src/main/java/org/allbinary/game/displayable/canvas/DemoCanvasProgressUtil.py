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



class DemoCanvasProgressUtil:
    

    @staticmethod
    def showProgress(demoCanvas: DemoCanvas) -> None:
        DemoCanvasProgressUtil.showProgressOptionallyInTheBackground(demoCanvas, False)
    

    @staticmethod
    def showProgressOptionallyInTheBackground(demoCanvas: DemoCanvas, background: bool) -> None:
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        progressCanvas.startBackground(background)
        paintableArray: list[PaintableInterface] = [None] * (2)
        paintableArray[0] = progressCanvas
        paintableArray[1] = demoCanvas.getDefaultPaintableInterface()
        demoCanvas.setDefaultPaintableInterface(PaintableComposite(paintableArray))
        demoCanvas.setPaintableInterface(demoCanvas.getDefaultPaintableInterface())
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.graphics.paint.PaintableComposite import PaintableComposite
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


