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
# package org.allbinary.game.score.displayable

from __future__ import annotations

from org.allbinary.graphics.form.item.CustomTextBox import CustomTextBox


class HighScoreTextBox(CustomTextBox):

    def _init_fields(self) -> None:
        self.virtualKeyboardEventHandler: VirtualKeyboardEventHandler = VirtualKeyboardEventHandler.getInstance()
        self.highScoreUtil: HighScoreUtil = None
        self.pleaseWait: Paintable = SimpleTextPaintable(self.commonStrings.PLEASE_WAIT, BasicColorFactory.getInstance().WHITE)
        self.paintable: Paintable = NullPaintable.getInstance()
        self.submitted: bool = False
    

    def __init__(self, highScoresFactoryInterface: HighScoresFactoryInterface, highScoresHelper: HighScoresHelperBaseInterface, abeClientInformation: AbeClientInformationInterface, gameInfo: GameInfo, cmdListener: CommandListener, name: str, highScore: HighScore, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.game.score.displayable.HighScoreUtil import HighScoreUtil
        super().__init__(cmdListener, "New High Score Enter Name:", name, 12, TextField.ANY, Font.getDefaultFont(), backgrounBasicColor, foregroundBasicColor)
        self._init_fields()
        self.highScoreUtil = HighScoreUtil(highScoresFactoryInterface, highScoresHelper, abeClientInformation, gameInfo, cmdListener, name, highScore)
        operatingSystemInterface: GenericOperatingSystem = OperatingSystemFactory.getInstance().getOperatingSystemInstance()
        if operatingSystemInterface.isOverScan():
            username: str = InApplicationPurchaseFactory.getInstance().getUserName()
            if username is not None:
                self.getTextFieldItem().setString(username)
            else:
                self.getTextFieldItem().setString("NoGamerInfo")
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        from org.allbinary.game.score.displayable.HighScoreUtil import HighScoreUtil
        self.removeAllCommands()
        PostGameCommandFactory.getInstance().addCommands(self)
        self.addCommand(HighScoreUtil.SUBMIT_TEXTBOX_COMMAND)
        self.setCommandListener(cmdListener)
    

    def open(self) -> None:
        self.virtualKeyboardEventHandler.open()
        self.paintable = NullPaintable.getInstance()
        super().open()
    

    # throws Exception
    def close(self) -> None:
        from org.allbinary.game.score.displayable.HighScoreUtil import HighScoreUtil
        self.virtualKeyboardEventHandler.close()
        self.paintable = self.pleaseWait
        self.repaintBehavior.onChangeRepaint(self)
        super().close()
        self.removeCommand(HighScoreUtil.SUBMIT_TEXTBOX_COMMAND)
        self.update()
        if self.submitted:
            self.highScoreUtil.saveHighScore()
        else:
            pass
        self.paintable = NullPaintable.getInstance()
        self.repaintBehavior.onChangeRepaint(self)
    

    # throws Exception
    def update(self) -> None:
        name: str = self.getTextFieldItem().getString()
        self.highScoreUtil.update(name)
        super().update()
    

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
        self.paintable.paint(graphics)
    

    def saveHighScore(self) -> None:
        self.highScoreUtil.saveHighScore()
    

    def submit(self) -> None:
        self.highScoreUtil.submit(self)
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.TextField import TextField
from org.allbinary.PostGameCommandFactory import PostGameCommandFactory
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.score.HighScore import HighScore
from org.allbinary.game.score.HighScoresHelperBaseInterface import HighScoresHelperBaseInterface
from org.allbinary.game.score.HighScoresFactoryInterface import HighScoresFactoryInterface
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.graphics.paint.SimpleTextPaintable import SimpleTextPaintable
from org.allbinary.input.event.VirtualKeyboardEventHandler import VirtualKeyboardEventHandler
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.InApplicationPurchaseFactory import InApplicationPurchaseFactory


