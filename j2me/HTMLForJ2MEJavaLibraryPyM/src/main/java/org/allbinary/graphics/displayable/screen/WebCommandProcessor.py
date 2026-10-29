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
# package org.allbinary.graphics.displayable.screen

from __future__ import annotations



class WebCommandProcessor:
    instance: WebCommandProcessor = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.aboutCommandProcessor: AboutCommandProcessor = AboutCommandProcessor.getInstance()
        self.list_: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> WebCommandProcessor:
        return WebCommandProcessor.instance
    

    def process(self, midletCommandListener: CommandListener, command: Command, canvas: Canvas) -> None:
        try:
            PlayN.openURL(self.list_.removeAt(0))
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.PROCESS, e)
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from playn.core.PlayN import PlayN
from org.allbinary.graphics.displayable.screen.AboutCommandProcessor import AboutCommandProcessor


WebCommandProcessor.instance = WebCommandProcessor()

