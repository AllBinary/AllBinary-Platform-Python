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
# package org.allbinary.game.score

from __future__ import annotations

from org.allbinary.game.score.HighScoresCanvasInputProcessorFactoryInterface import HighScoresCanvasInputProcessorFactoryInterface


class HighScoresCanvasNoInputProcessorFactory(HighScoresCanvasInputProcessorFactoryInterface):
    

    def getInstance(self, highScoresCanvas: HighScoresCanvas) -> HighScoresCanvasInputProcessor:
        from org.allbinary.game.score.HighScoresCanvasInputProcessor import HighScoresCanvasInputProcessor
        return HighScoresCanvasInputProcessor(highScoresCanvas)
from org.allbinary.game.score.displayable.HighScoresCanvas import HighScoresCanvas


