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

# from javax.microedition.lcdui.Command import Command
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.game.displayable.canvas.GameCommandCanvas import GameCommandCanvas


class GameInputMappingInstructionsCanvas(GameCommandCanvas):
    DISPLAY: Command = Command("Help", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
    CLOSE: Command = Command("Close", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
    NAME: str = "GameInputMappingInstructionsCanvas"

    def _init_fields(self) -> None:
        self.drawStringUtil: DrawStringUtil = DrawStringUtil.getInstance()
        self.TITLE: str = "Input Instructions"
        self.instructions: list[str] = ["Add Input Mapping:", "1. Select the desired action by generating a currently defined input for a given action.", "(Example: Press the '1' key to select the Fire action)", "2. Make the newly desired input for the selected action.", "(Example: Press 'f' to add it to the selected action)", "Note: If the input is already mapped to another action then it will not be added. You", "will need to deleted from the other action before adding it to another.", "Warning: Not all keys map for a given platform and show as Unknown.", StringUtil.getInstance().EMPTY_STRING, "Remove Input Mapping:", "1. Select the desired action by generating a currently defined input for a given action.", "(Example: Press the key '1' to select the Fire action)", "2. Select a mapped input for the selected action.", "(Example: Press the key '1' to select the '1' key input for the selected Fire action)", "3. Press the Delete Key."]
        self.colorFillPaintable: ColorFillBasePaintable = None
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, commandListener: CommandListener, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().__init__(commandListener, GameInputMappingInstructionsCanvas.NAME, allBinaryGameLayerManager.getBackgroundBasicColor(), allBinaryGameLayerManager.getForegroundBasicColor())
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.colorFillPaintable = ColorFillPaintableFactory.getInstance().getInstance(allBinaryGameLayerManager.getBackgroundBasicColor(), False)
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        self.removeAllCommands()
        self.addCommand(GameInputMappingInstructionsCanvas.CLOSE)
        self.setCommandListener(cmdListener)
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        self.colorFillPaintable.paint(graphics)
        halfWidth: int = self.displayInfo.getLastHalfWidth()
        beginWidth: int = (graphics.getFont().stringWidth(self.TITLE) >> 1)
        graphics.setColor(self.foregroundColor)
        graphics.drawString(self.TITLE, halfWidth - beginWidth, self.fontHeight, self.anchor)
        self.drawStringUtil.drawCenterStrings(graphics, self.instructions, self.displayInfo.getLastWidth(), self.fontHeight, halfWidth, 3 * self.fontHeight)
        super().paint(graphics)
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.paint.ColorFillBasePaintable import ColorFillBasePaintable
from org.allbinary.game.paint.ColorFillPaintableFactory import ColorFillPaintableFactory
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.draw.DrawStringUtil import DrawStringUtil


