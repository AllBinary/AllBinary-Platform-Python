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



class StatusFactory:
    instance: StatusFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.SETSTATUS: str = "setStatus"
        self.STATUS_LABEL: str = "Status: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> StatusFactory:
        return StatusFactory.instance
    

    def setStatusNoLog(self, status: str) -> None:
        from org.allbinary.graphics.j2me.MyFrame import MyFrame
        MyFrame.statusJLabel.setText(status)
    

    def setStatus(self, status: str) -> None:
        self.setStatusNoLog(status)
        self.logUtil.putF(self.STATUS_LABEL + status, self, self.SETSTATUS)
from org.allbinary.logic.communication.log.LogUtil import LogUtil


StatusFactory.instance = StatusFactory()

