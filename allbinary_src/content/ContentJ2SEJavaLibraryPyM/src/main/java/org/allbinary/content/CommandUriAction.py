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
# package org.allbinary.content

from __future__ import annotations



class CommandUriAction:
    instance: CommandUriAction = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CommandUriAction:
        return CommandUriAction.instance
    

    def add(self, command: Command, url: str) -> None:
        self.hashtable.put(command, url)
    

    def process(self, command: Command) -> None:
        try:
            pass
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
    

    def getIntent(self, command: Command) -> Intent:
        url: str = self.hashtable.get(command)
        return self.intent
# from javax.microedition.lcdui.Command import Command
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable


CommandUriAction.instance = CommandUriAction()

