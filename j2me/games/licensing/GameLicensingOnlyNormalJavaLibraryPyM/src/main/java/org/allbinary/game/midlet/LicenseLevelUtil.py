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



class LicenseLevelUtil:
    instance: LicenseLevelUtil = None
    

    @staticmethod
    def getInstance() -> LicenseLevelUtil:
        return LicenseLevelUtil.instance
    

    def getMaxLevel(self, maxLevel: int, demoLevel: int) -> int:
        return maxLevel


LicenseLevelUtil.instance = LicenseLevelUtil()

