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

from org.allbinary.logic.NullUtil import NullUtil


class InGameOptionsFormFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.SINGLETON: CommandForm = CommandForm.getNullCommandForm()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> InGameOptionsFormFactory:
        if InGameOptionsFormFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            InGameOptionsFormFactory.instance = InGameOptionsFormFactory()
        return InGameOptionsFormFactory.instance
    

    def init(self, commandListener: CommandListener, initInterface: Init, title: str, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.game.configuration.InGameOptionsForm import InGameOptionsForm
        try:
            if self.SINGLETON == CommandForm.getNullCommandForm():
                initInterface.init()
                self.SINGLETON = InGameOptionsForm(commandListener, title, backgrounBasicColor, foregroundBasicColor)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.INIT, e)
    

    def get(self) -> CommandForm:
        return self.SINGLETON
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.screen.CommandForm import CommandForm
from org.allbinary.init.Init import Init
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


