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

from java.lang.JavaRuntimeStatic import java_inherited_overloads


@java_inherited_overloads
class GraphicsException(Exception):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("guiLog", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.GuiLog import GuiLog
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.guiLog: GuiLog = GuiLog.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 3:
            __class__.__jconstructor3(self, *args)

    def __jconstructor3(self, *args) -> None:
        if True and (args[0] is None or isinstance(args[0], str)) and (args[2] is None or isinstance(args[2], str)):
            __class__._constructor3_1(self, *args)
        else:
            __class__._constructor3_2(self, *args)
    

    def _constructor3_1(self, msg: str, obj: object, method: str) -> None:
        __class__._java_defaults(self)
        super().__init__(msg)
        __class__._init_fields(self)
        try:
            self.guiLog.showDialog(msg)
            self.logUtil.put(msg, obj, method, self)
        except Exception as e:
            pass
    

    def _constructor3_2(self, msg: str, className: str, method: str) -> None:
        __class__._java_defaults(self)
        super().__init__(msg)
        __class__._init_fields(self)
        try:
            self.guiLog.showDialog(msg)
            self.logUtil.put(msg, className, method, self)
        except Exception as e:
            pass
# from org.allbinary.logic.communication.log.GuiLog import GuiLog
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


