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



class SaveHighScoreRunnable(object):

    def _init_fields(self) -> None:
        from org.allbinary.game.score.displayable.HighScoreTextBox import HighScoreTextBox
        from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
        from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
        self.progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        self.isLast: bool = None
        self.textBox: HighScoreTextBox = None
    

    def __init__(self, isLast: bool, textBox: HighScoreTextBox) -> None:
        from org.allbinary.game.score.displayable.HighScoreTextBox import HighScoreTextBox
        self._init_fields()
        self.isLast = isLast
        self.textBox = textBox
    

    def run(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            if self.isLast:
                self.textBox.submit()
            else:
                self.textBox.saveHighScore()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.put(commonStrings.EXCEPTION, self, "run", e)
            self.progressCanvas.end()
# from org.allbinary.game.score.displayable.HighScoreTextBox import HighScoreTextBox
# from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
# from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings


