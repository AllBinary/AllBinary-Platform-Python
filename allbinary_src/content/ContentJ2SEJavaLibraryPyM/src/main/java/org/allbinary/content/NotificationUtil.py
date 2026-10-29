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

import time


class NotificationUtil:
    SINGLETON: NotificationUtil = None

    def _init_fields(self) -> None:
        self.notificationManager: NotificationManager = ResourceUtil.getInstance().getContext().getSystemService(Context.NOTIFICATION_SERVICE)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> NotificationUtil:
        return NotificationUtil.SINGLETON
    

    def notify(self, command: Command, resource: str, message: str) -> None:
        from org.allbinary.content.CommandUriAction import CommandUriAction
        from org.allbinary.content.Notification import Notification
        from org.allbinary.content.PendingIntent import PendingIntent
        context: Context = ResourceUtil.getInstance().getContext()
        intent: Intent = CommandUriAction.getInstance().getIntent(command)
        integer: int = ResourceUtil.getInstance().getResourceId(resource)
        notification: Notification = Notification(int(integer), message, int(time.time() * 1000))
        pendingIntent: PendingIntent = PendingIntent.getActivity(context, 0, intent, 0)
        notification.setLatestEventInfo(context, command.getLabel(), message, pendingIntent)
        self.notificationManager.notify(TsUtil.getInstance().hashCode(command), notification)
# from javax.microedition.lcdui.Command import Command
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.TsUtil import TsUtil
from org.allbinary.content.Context import Context


NotificationUtil.SINGLETON = NotificationUtil()

