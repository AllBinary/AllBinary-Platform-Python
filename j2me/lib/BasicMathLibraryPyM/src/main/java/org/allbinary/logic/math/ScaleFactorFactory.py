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
# package org.allbinary.logic.math

from __future__ import annotations



class ScaleFactorFactory:
    instance: ScaleFactorFactory = None

    def _init_fields(self) -> None:
        self.DEFAULT_SCALE_FACTOR: int = 10
        self.DEFAULT_SCALE_VALUE: int = 1024

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ScaleFactorFactory:
        return ScaleFactorFactory.instance


ScaleFactorFactory.instance = ScaleFactorFactory()

