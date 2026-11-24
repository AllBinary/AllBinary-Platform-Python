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


class NotificationBuilder:
    NULL_NOTIFICATION_BUILDER: NotificationBuilder = None
    

    def build(self, context: Context, command: Command, message: str, integer: int, pendingIntent: PendingIntent) -> Parcelable:
        from org.allbinary.android.NullParcelable import NullParcelable
        from javax.microedition.lcdui.Command import Command
        from android.app.PendingIntent import PendingIntent
        from android.content.Context import Context
        from android.os.Parcelable import Parcelable
        return NullParcelable.NULL_PARCELABLE
# from org.allbinary.android.NullParcelable import NullParcelable
# from javax.microedition.lcdui.Command import Command
# from android.app.PendingIntent import PendingIntent
# from android.content.Context import Context
# from android.os.Parcelable import Parcelable


def _NotificationBuilder_NULL_NOTIFICATION_BUILDER() -> object:
    return NotificationBuilder()

lazy_static(NotificationBuilder, "NULL_NOTIFICATION_BUILDER", _NotificationBuilder_NULL_NOTIFICATION_BUILDER)

