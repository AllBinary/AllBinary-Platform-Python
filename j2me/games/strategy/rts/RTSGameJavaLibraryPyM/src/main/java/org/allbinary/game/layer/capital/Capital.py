# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
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
# package org.allbinary.game.layer.capital

from __future__ import annotations



class Capital:

    def _init_fields(self) -> None:
        self.value: int = 0
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getTotalMoney(self) -> int:
        return self.value
    

    def removeMoney(self, points: int) -> None:
        self.value -= points
    

    def addMoney(self, points: int) -> None:
        self.value += points


