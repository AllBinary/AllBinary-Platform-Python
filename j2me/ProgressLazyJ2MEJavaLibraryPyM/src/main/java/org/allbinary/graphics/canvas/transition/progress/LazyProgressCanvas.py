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
# package org.allbinary.graphics.canvas.transition.progress

from __future__ import annotations

from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas


class LazyProgressCanvas(ProgressCanvas):
    

    def __init__(self, title: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(title, backgroundBasicColor, foregroundBasicColor)
    

    def start(self) -> None:
        super().start()
        self.hasPainted = False
    

    def end(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.END_METHOD_NAME)
            self.endActual()
            self.paintable = self.GAUGE_PAINTABLE
            ImageCacheFactory.getInstance().runTask()
            ImageCacheFactory.getInstance().progressEnded()
        except Exception as e:
            self.logUtil.putF(self.commonStrings.EXCEPTION, self, self.commonStrings.END_METHOD_NAME)
    

    def inGame(self) -> None:
        self.inGameProcessor = Processor.getInstance()
    

    def endFromInitialLazyLoadingComplete(self) -> None:
        super().endFromInitialLazyLoadingComplete()
        self.paintable = NullPaintable.getInstance()
    

    def endIfPaintedSinceStart(self) -> None:
        if self.paintable == self.GAUGE_PAINTABLE and self.hasPainted:
            self.endFromInitialLazyLoadingComplete()
from org.allbinary.canvas.Processor import Processor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.image.ImageCacheFactory import ImageCacheFactory


