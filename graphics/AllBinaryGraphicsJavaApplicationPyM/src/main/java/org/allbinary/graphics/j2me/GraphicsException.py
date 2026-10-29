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
# package org.allbinary.graphics.j2me

from __future__ import annotations



class GraphicsException(Exception):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.guiLog: GuiLog = GuiLog.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 3:
            self._constructor3(*args)
    

    def _constructor3(self, msg: str, obj: object, method: str) -> None:
        super().__init__(msg)
        self._init_fields()
        try:
            self.guiLog.showDialog(msg)
            self.logUtil.put(msg, obj, method, self)
        except Exception as e:
            pass
    

    def _constructor3(self, msg: str, className: str, method: str) -> None:
        super().__init__(msg)
        self._init_fields()
        try:
            self.guiLog.showDialog(msg)
            self.logUtil.put(msg, className, method, self)
        except Exception as e:
            pass
from org.allbinary.logic.communication.log.GuiLog import GuiLog
from org.allbinary.logic.communication.log.LogUtil import LogUtil


