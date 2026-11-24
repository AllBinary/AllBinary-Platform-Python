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
        self._init_fields()
    

    def showDialog(self, msg: str) -> None:
        with self._lock:
            return self._showDialog_unlocked(msg)

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
            return self._put_j3_1_unlocked(specialMessage, anyType, functionName)

    def _put_j3_1_unlocked(self, specialMessage: str, anyType: object, functionName: str) -> str:
        return self.put(specialMessage, anyType, functionName, None)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def put_j4_1(self, specialMessage: str, anyType: object, functionName: str, exception: Exception) -> str:
        with self._lock:
            return self._put_j4_1_unlocked(specialMessage, anyType, functionName, exception)

    def _put_j4_1_unlocked(self, specialMessage: str, anyType: object, functionName: str, exception: Exception) -> str:
        try:
            data: str = self.logFormatUtil.get(specialMessage, type(anyType).__module__ + "." + type(anyType).__qualname__, functionName, exception)
            self.showDialog(data)
            print(data)
            return data
        except Exception as e:
            PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, "put", e)
            return "Logging Error"
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def put_j3_2(self, specialMessage: str, className: str, functionName: str) -> str:
        with self._lock:
            return self._put_j3_2_unlocked(specialMessage, className, functionName)

    def _put_j3_2_unlocked(self, specialMessage: str, className: str, functionName: str) -> str:
        return self.put(specialMessage, className, functionName, None)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def put_j4_2(self, specialMessage: str, className: str, functionName: str, exception: Exception) -> str:
        with self._lock:
            return self._put_j4_2_unlocked(specialMessage, className, functionName, exception)

    def _put_j4_2_unlocked(self, specialMessage: str, className: str, functionName: str, exception: Exception) -> str:
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
            return self.put_j3_1(*args)
        if len(args) == 4 and True and (args[0] is None or isinstance(args[0], str)) and (args[2] is None or isinstance(args[2], str)) and not isinstance(args[3], (str, list, int, float)):
            return self.put_j4_1(*args)
        if len(args) == 3:
            return self.put_j3_2(*args)
        if len(args) == 4:
            return self.put_j4_2(*args)
        return getattr(self, "put_j" + str(len(args)))(*args)
# from java.awt.GridLayout import GridLayout
# from javax.swing.JDialog import JDialog
# from org.allbinary.string.CommonStrings import CommonStrings
# from javax.swing.JLabel import JLabel
# from javax.swing.JScrollPane import JScrollPane
# from javax.swing.JTextArea import JTextArea


def _GuiLog_instance() -> object:
    return GuiLog()

lazy_static(GuiLog, "instance", _GuiLog_instance)

