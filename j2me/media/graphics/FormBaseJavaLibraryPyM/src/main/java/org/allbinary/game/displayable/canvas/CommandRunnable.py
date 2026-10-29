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



class CommandRunnable(object):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commandFormInputProcessor: CommandFormInputProcessor = None
        self.command: Command = None
    

    def __init__(self, commandFormInputProcessor: CommandFormInputProcessor, command: Command) -> None:
        self._init_fields()
        self.commandFormInputProcessor = commandFormInputProcessor
        self.command = command
    

    def run(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START_RUNNABLE, self, self.commonStrings.RUN)
            canvas: MyCanvas = self.commandFormInputProcessor.getCanvas()
            commandListener: CommandListener = canvas.getCustomCommandListener()
            commandListener.commandAction(self.command, canvas)
            self.logUtil.putF(self.commonStrings.END_RUNNABLE, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


