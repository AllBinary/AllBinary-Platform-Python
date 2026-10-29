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
# package org.allbinary.logic.communication.log.config

from __future__ import annotations



class LogConfigData:
    instance: LogConfigData = None

    def _init_fields(self) -> None:
        self.NAME: str = "LOG_CONFIG_NAME"
        self.DESCRIPTION: str = "LOG_CONFIG_DESCRIPTION"
        self.FILE: str = "LOG_CONFIG_FILE"
    

    @staticmethod
    def getInstance() -> LogConfigData:
        return LogConfigData.instance
    

    def __init__(self) -> None:
        self._init_fields()


LogConfigData.instance = LogConfigData()

