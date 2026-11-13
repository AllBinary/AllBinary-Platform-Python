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

from java.lang.JavaRuntimeStatic import lazy_static


class CommandUriAction:
    instance: CommandUriAction = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CommandUriAction:
        return CommandUriAction.instance
    

    def add(self, command: Command, url: str) -> None:
        from javax.microedition.lcdui.Command import Command
        pass
    

    def process(self, command: Command) -> None:
        from javax.microedition.lcdui.Command import Command
        pass
# from javax.microedition.lcdui.Command import Command
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


def _CommandUriAction_instance() -> object:
    return CommandUriAction()

lazy_static(CommandUriAction, "instance", _CommandUriAction_instance)

