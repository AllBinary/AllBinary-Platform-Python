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
from org.allbinary.content.NotificationBuilder import NotificationBuilder


class NotificationBuilderAPI23(NotificationBuilder):

    def __init__(self) -> None:
        super().__init__()
    

    def build(self, context: Context, command: Command, message: str, integer: int, pendingIntent: PendingIntent) -> Parcelable:
        notification: Notification = Builder(context).setSmallIcon(int(integer)).setTicker(message).setWhen(int(time.time() * 1000)).setContentTitle(command.getLabel()).setContentText(message).setContentIntent(pendingIntent).build()
        return notification
# from javax.microedition.lcdui.Command import Command
from android.app.Notification import Notification
from android.app.Notification.Builder import Builder
from android.app.PendingIntent import PendingIntent
from android.content.Context import Context
from android.os.Parcelable import Parcelable


