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
# package org.allbinary.logic.communication.log.config.type

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class LogConfigTypeFactory:
    instance: LogConfigTypeFactory = None

    def _init_fields(self) -> None:
        self.NO_DESCRIPTION: str = "No Description"
        self.INIT_SERVER: LogConfigType = LogConfigType("Init Server", self.NO_DESCRIPTION)
        self.LOBBY_SERVER: LogConfigType = LogConfigType("Lobby Server", self.NO_DESCRIPTION)
        self.GAME_SERVER: LogConfigType = LogConfigType("Game Server", self.NO_DESCRIPTION)
        self.GAME_SIMULATOR: LogConfigType = LogConfigType("Game Simulator", self.NO_DESCRIPTION)
        self.CUSTOM_TYPES: LogConfigType = LogConfigType("Custom Types", self.NO_DESCRIPTION)
    

    @staticmethod
    def getInstance() -> LogConfigTypeFactory:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        return LogConfigTypeFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        __class__._init_fields(self)
        LogConfigTypes.LOGGING.add(self.INIT_SERVER)
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigType import LogConfigType


def _LogConfigTypeFactory_instance() -> object:
    from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
    return LogConfigTypeFactory()

lazy_static(LogConfigTypeFactory, "instance", _LogConfigTypeFactory_instance)

