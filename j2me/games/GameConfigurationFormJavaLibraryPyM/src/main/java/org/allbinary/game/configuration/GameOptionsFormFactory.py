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
# package org.allbinary.game.configuration

from __future__ import annotations



class GameOptionsFormFactory:
    instance: GameOptionsFormFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameOptionsFormFactory:
        return GameOptionsFormFactory.instance
    

    def init(self, commandListener: CommandListener, title: str, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> CommandForm:
        from org.allbinary.game.configuration.GameOptionsForm import GameOptionsForm
        try:
            return GameOptionsForm(commandListener, title, backgrounBasicColor, foregroundBasicColor)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.INIT, e)
            return CommandForm.getNullCommandForm()
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.screen.CommandForm import CommandForm
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


GameOptionsFormFactory.instance = GameOptionsFormFactory()

