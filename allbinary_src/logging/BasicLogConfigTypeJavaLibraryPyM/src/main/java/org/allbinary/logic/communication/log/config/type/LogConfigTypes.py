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


class LogConfigTypes:
    LOGGING: BasicArrayList = None
    

    def __init__(self) -> None:
        pass
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _LogConfigTypes_LOGGING() -> object:
    from org.allbinary.util.BasicArrayList import BasicArrayList
    from org.allbinary.util.BasicArrayListD import BasicArrayListD
    return BasicArrayListD()

lazy_static(LogConfigTypes, "LOGGING", _LogConfigTypes_LOGGING)

