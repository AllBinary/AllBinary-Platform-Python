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
# package org.allbinary.game.midlet

from __future__ import annotations



class LicenseLoadingTypeFactory:
    instance: LicenseLoadingTypeFactory = None

    def _init_fields(self) -> None:
        self.INITIAL_LOADING: LicenseLoadingType = LicenseLoadingType("Initial Loading")
        self.GAME_START: LicenseLoadingType = LicenseLoadingType("Game Start")
        self.LOGIN: LicenseLoadingType = LicenseLoadingType("Login")
        self.OTHER: LicenseLoadingType = LicenseLoadingType("Other/Usually The First Non Demo Level")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getIntance() -> LicenseLoadingTypeFactory:
        return LicenseLoadingTypeFactory.instance
from org.allbinary.game.midlet.LicenseLoadingType import LicenseLoadingType


LicenseLoadingTypeFactory.instance = LicenseLoadingTypeFactory()

