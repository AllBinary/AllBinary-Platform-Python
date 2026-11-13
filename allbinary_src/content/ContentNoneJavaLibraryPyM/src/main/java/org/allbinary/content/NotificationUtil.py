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


class NotificationUtil:
    SINGLETON: NotificationUtil = None
    

    @staticmethod
    def getInstance() -> NotificationUtil:
        return NotificationUtil.SINGLETON
    

    def notify(self, command: Command, resource: str, message: str) -> None:
        from javax.microedition.lcdui.Command import Command
        pass
# from javax.microedition.lcdui.Command import Command


def _NotificationUtil_SINGLETON() -> object:
    return NotificationUtil()

lazy_static(NotificationUtil, "SINGLETON", _NotificationUtil_SINGLETON)

