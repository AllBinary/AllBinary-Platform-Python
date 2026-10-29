# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations



# Java interface
class RTSInterface:
    

    def isSelfUpgradeable(self) -> bool:
        raise NotImplementedError()
    

    def isCompleted(self) -> bool:
        raise NotImplementedError()
    

    def getPercentComplete(self) -> int:
        raise NotImplementedError()
    

    def getLevel(self) -> int:
        raise NotImplementedError()
    

    def getMaxLevel(self) -> int:
        raise NotImplementedError()
    

    def getCost(self) -> int:
        raise NotImplementedError()
    

    def downgrade(self) -> None:
        raise NotImplementedError()
    

    def getDowngradeCost(self) -> int:
        raise NotImplementedError()
    

    def isDowngradeable(self) -> bool:
        raise NotImplementedError()
    

    def getUpgradeCost(self) -> int:
        raise NotImplementedError()
    

    def isUpgradeable(self) -> bool:
        raise NotImplementedError()
    

    def upgrade(self) -> None:
        raise NotImplementedError()


