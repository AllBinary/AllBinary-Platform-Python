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
# package org.allbinary.logic.io.path

from __future__ import annotations



class AbPathUtil:
    instance: AbPathUtil = None

    def _init_fields(self) -> None:
        self.NO_ABPATH: AbPath = AbPath.createAbPath()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AbPathUtil:
        return AbPathUtil.instance
from org.allbinary.logic.io.path.AbPath import AbPath


AbPathUtil.instance = AbPathUtil()

