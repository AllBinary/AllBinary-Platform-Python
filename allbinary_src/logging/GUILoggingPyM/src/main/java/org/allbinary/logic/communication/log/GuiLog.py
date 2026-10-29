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


class GuiLog:
    instance: GuiLog = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
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
        from org.allbinary.logic.communication.log.JDialog import JDialog
        from org.allbinary.logic.communication.log.GridLayout import GridLayout
        from org.allbinary.logic.communication.log.JScrollPane import JScrollPane
        from org.allbinary.logic.communication.log.JLabel import JLabel
        from org.allbinary.logic.communication.log.JScrollPane import JScrollPane
        from org.allbinary.logic.communication.log.JTextArea import JTextArea
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
    

    def put(self, specialMessage: str, anyType: object, functionName: str) -> str:
        with self._lock:
            return self._put_unlocked(specialMessage, anyType, functionName)

    def _put_unlocked(self, specialMessage: str, anyType: object, functionName: str) -> str:
        return self.put(specialMessage, anyType, functionName, None)
    

    # Java overloaded method: Python keeps the last definition
    def put(self, specialMessage: str, anyType: object, functionName: str, exception: Exception) -> str:
        with self._lock:
            return self._put_unlocked(specialMessage, anyType, functionName, exception)

    def _put_unlocked(self, specialMessage: str, anyType: object, functionName: str, exception: Exception) -> str:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        try:
            data: str = self.logFormatUtil.get(specialMessage, type(anyType).__module__ + "." + type(anyType).__qualname__, functionName, exception)
            self.showDialog(data)
            print(data)
            return data
        except Exception as e:
            PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, "put", e)
            return "Logging Error"
    

    # Java overloaded method: Python keeps the last definition
    def put(self, specialMessage: str, className: str, functionName: str) -> str:
        with self._lock:
            return self._put_unlocked(specialMessage, className, functionName)

    def _put_unlocked(self, specialMessage: str, className: str, functionName: str) -> str:
        return self.put(specialMessage, className, functionName, None)
    

    # Java overloaded method: Python keeps the last definition
    def put(self, specialMessage: str, className: str, functionName: str, exception: Exception) -> str:
        with self._lock:
            return self._put_unlocked(specialMessage, className, functionName, exception)

    def _put_unlocked(self, specialMessage: str, className: str, functionName: str, exception: Exception) -> str:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        try:
            data: str = self.logFormatUtil.get(specialMessage, className, functionName, exception)
            self.showDialog(data)
            print(data)
            return data
        except Exception as e:
            PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, "put", e)
            return "Logging Error"
# from java.awt import *
# from javax.swing import *
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil


GuiLog.instance = GuiLog()

