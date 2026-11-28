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
# package org.allbinary.logic.communication.log

from __future__ import annotations

from java.lang.System import System
import threading
from java.lang.JavaRuntimeStatic import lazy_static


class GuiLog:
    instance: GuiLog = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logFormatUtil: LogFormatUtil = LogFormatUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    @staticmethod
    def getInstance() -> GuiLog:
        return GuiLog.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def showDialog(self, msg: str) -> None:
        with self._lock:
            return __class__.__dict__["_showDialog_unlocked"].__get__(self, __class__)(msg)

    def _showDialog_unlocked(self, msg: str) -> None:
        error: JDialog = JDialog()
        size: int = len(msg) * 9
        x: int = size
        if x > 550:
            x = 550
        error.getContentPane().setLayout(GridLayout(1, 1))
        if size > 255:
            y: int = 550
            error.setSize(x, y)
            error.getContentPane().add(JScrollPane(JTextArea(msg)))
        elif size > 0:
            y: int = 50
            error.setSize(x, y)
            error.getContentPane().add(JScrollPane(JLabel(msg)))
        error.show()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def put_j3_1(self, specialMessage: str, anyType: object, functionName: str) -> str:
        with self._lock:
            return __class__.__dict__["_put_j3_1_unlocked"].__get__(self, __class__)(specialMessage, anyType, functionName)

    def _put_j3_1_unlocked(self, specialMessage: str, anyType: object, functionName: str) -> str:
        return self.put(specialMessage, anyType, functionName, None)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def put_j4_1(self, specialMessage: str, anyType: object, functionName: str, exception: Exception) -> str:
        with self._lock:
            return __class__.__dict__["_put_j4_1_unlocked"].__get__(self, __class__)(specialMessage, anyType, functionName, exception)

    def _put_j4_1_unlocked(self, specialMessage: str, anyType: object, functionName: str, exception: Exception) -> str:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        try:
            data: str = self.logFormatUtil.get(specialMessage, __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(anyType)), functionName, exception)
            self.showDialog(data)
            print(data)
            return data
        except Exception as e:
            PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, "put", e)
            return "Logging Error"
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def put_j3_2(self, specialMessage: str, className: str, functionName: str) -> str:
        with self._lock:
            return __class__.__dict__["_put_j3_2_unlocked"].__get__(self, __class__)(specialMessage, className, functionName)

    def _put_j3_2_unlocked(self, specialMessage: str, className: str, functionName: str) -> str:
        return self.put(specialMessage, className, functionName, None)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def put_j4_2(self, specialMessage: str, className: str, functionName: str, exception: Exception) -> str:
        with self._lock:
            return __class__.__dict__["_put_j4_2_unlocked"].__get__(self, __class__)(specialMessage, className, functionName, exception)

    def _put_j4_2_unlocked(self, specialMessage: str, className: str, functionName: str, exception: Exception) -> str:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        try:
            data: str = self.logFormatUtil.get(specialMessage, className, functionName, exception)
            self.showDialog(data)
            print(data)
            return data
        except Exception as e:
            PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, "put", e)
            return "Logging Error"

    def put(self, *args):
        if len(args) == 3 and True and (args[0] is None or isinstance(args[0], str)) and (args[2] is None or isinstance(args[2], str)):
            return __class__.__dict__["put_j3_1"].__get__(self, __class__)(*args)
        if len(args) == 4 and True and (args[0] is None or isinstance(args[0], str)) and (args[2] is None or isinstance(args[2], str)) and not isinstance(args[3], (str, list, int, float)):
            return __class__.__dict__["put_j4_1"].__get__(self, __class__)(*args)
        if len(args) == 3:
            return __class__.__dict__["put_j3_2"].__get__(self, __class__)(*args)
        if len(args) == 4:
            return __class__.__dict__["put_j4_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("put_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().put(*args)
# from java.awt.GridLayout import GridLayout
# from javax.swing.JDialog import JDialog
# from org.allbinary.string.CommonStrings import CommonStrings
# from javax.swing.JLabel import JLabel
# from javax.swing.JScrollPane import JScrollPane
# from javax.swing.JTextArea import JTextArea
from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil


def _GuiLog_instance() -> object:
    return GuiLog()

lazy_static(GuiLog, "instance", _GuiLog_instance)

