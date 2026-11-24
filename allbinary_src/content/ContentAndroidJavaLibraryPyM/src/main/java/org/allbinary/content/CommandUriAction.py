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
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.util.ABHashtable import ABHashtable
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CommandUriAction:
        return CommandUriAction.instance
    

    def add(self, command: Command, url: str) -> None:
        from javax.microedition.lcdui.Command import Command
        self.hashtable.put(command, url)
    

    def process(self, command: Command) -> None:
        from javax.microedition.lcdui.Command import Command
        from android.content.Intent import Intent
        from org.allbinary.data.resource.ResourceUtil import ResourceUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            intent: Intent = self.getIntent(command)
            ResourceUtil.getInstance().getContext().startActivity(intent)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.PROCESS, e)
    

    def getIntent(self, command: Command) -> Intent:
        from javax.microedition.lcdui.Command import Command
        from android.content.Intent import Intent
        from android.net.Uri import Uri
        url: str = self.hashtable.get(command)
        uri: Uri = Uri.parse(url)
        intent: Intent = Intent(Intent.ACTION_VIEW, uri)
        return intent
# from javax.microedition.lcdui.Command import Command
# from android.content.Intent import Intent
# from android.net.Uri import Uri
# from org.allbinary.data.resource.ResourceUtil import ResourceUtil
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.ABHashtable import ABHashtable


def _CommandUriAction_instance() -> object:
    return CommandUriAction()

lazy_static(CommandUriAction, "instance", _CommandUriAction_instance)

