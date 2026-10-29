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



class NotificationUtil:
    SINGLETON: NotificationUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.notificationManager: NotificationManager = ResourceUtil.getInstance().getContext().getSystemService(Context.NOTIFICATION_SERVICE)
        self.notificationBuilder: NotificationBuilder = None
    

    @staticmethod
    def getInstance() -> NotificationUtil:
        return NotificationUtil.SINGLETON
    

    def __init__(self) -> None:
        from org.allbinary.content.NotificationBuilder import NotificationBuilder
        from org.allbinary.content.NotificationBuilderAPI23 import NotificationBuilderAPI23
        self._init_fields()
        SDK_VERSION: int = AndroidInfoFactory.getInstance().getVersion()
        if SDK_VERSION > 22:
            self.notificationBuilder = NotificationBuilderAPI23()
        else:
            self.notificationBuilder = NotificationBuilder.NULL_NOTIFICATION_BUILDER
    

    def notify(self, command: Command, resource: str, message: str) -> None:
        from org.allbinary.content.CommandUriAction import CommandUriAction
        context: Context = ResourceUtil.getInstance().getContext()
        intent: Intent = CommandUriAction.getInstance().getIntent(command)
        integer: int = ResourceUtil.getInstance().getResourceId(resource)
        FLAG_IMMUTABLE: int = 1 << 26
        SDK_VERSION: int = AndroidInfoFactory.getInstance().getVersion()
        pendingIntent: PendingIntent = PendingIntent.getActivity(context, 0, intent, (FLAG_IMMUTABLE if SDK_VERSION > 22 else 0))
        if self.notificationBuilder is None:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.EXCEPTION, self, commonStrings.NOT_IMPLEMENTED)
            return
        self.notificationBuilder.build(context, command, message, integer, pendingIntent)
# from javax.microedition.lcdui.Command import Command
from android.app.Notification import Notification
from android.app.NotificationManager import NotificationManager
from android.app.PendingIntent import PendingIntent
from android.content.Context import Context
from android.content.Intent import Intent
from org.allbinary.android.AndroidInfoFactory import AndroidInfoFactory
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


NotificationUtil.SINGLETON = NotificationUtil()

