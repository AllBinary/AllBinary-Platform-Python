# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.media.graphics.geography.map

from __future__ import annotations



class GeographicMapCellHistoryProgressBase:
    instance: GeographicMapCellHistoryProgressBase = None
    

    @staticmethod
    def getInstance() -> GeographicMapCellHistoryProgressBase:
        return GeographicMapCellHistoryProgressBase.instance
    

    def __init__(self) -> None:
        pass
    

    def init(self) -> None:
        raise RuntimeError()
    

    def isAnyProgress(self) -> bool:
        raise RuntimeError()


GeographicMapCellHistoryProgressBase.instance = GeographicMapCellHistoryProgressBase()

