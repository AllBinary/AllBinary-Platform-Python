# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.logic.communication.log.config.type

from __future__ import annotations



class LogConfigTypeFactory:
    instance: LogConfigTypeFactory = None

    def _init_fields(self) -> None:
        self.NO_DESCRIPTION: str = "No Description"
        self.OS: LogConfigType = LogConfigType("Operating System", self.NO_DESCRIPTION)
        self.FACTORYERROR: LogConfigType = LogConfigType("Factory Error", self.NO_DESCRIPTION)
    

    @staticmethod
    def getInstance() -> LogConfigTypeFactory:
        return LogConfigTypeFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        self._init_fields()
        LogConfigTypes.LOGGING.add(self.OS)
        LogConfigTypes.LOGGING.add(self.FACTORYERROR)
from org.allbinary.logic.communication.log.config.type.LogConfigType import LogConfigType


LogConfigTypeFactory.instance = LogConfigTypeFactory()

