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
# package org.allbinary.game.layer.capital.event

from __future__ import annotations

from org.allbinary.game.layer.capital.event.CapitalEventHandler import CapitalEventHandler


class CapitalEventHandlerFactory:
    capitalEventHandlerArray: list[CapitalEventHandler] = [None] * (10)
    

    @staticmethod
    def _static_init() -> None:
        for index in range(len(CapitalEventHandlerFactory.capitalEventHandlerArray) - 1, 0 - 1, -1):
            CapitalEventHandlerFactory.capitalEventHandlerArray[index] = CapitalEventHandler()
    

    @staticmethod
    def getInstance(groupInterface: Group) -> CapitalEventHandler:
        from org.allbinary.game.identification.Group import Group
        groupId: int = int(groupInterface.getGroupId())
        return CapitalEventHandlerFactory.capitalEventHandlerArray[groupId]
    

    @staticmethod
    def removeAll() -> None:
        for index in range(len(CapitalEventHandlerFactory.capitalEventHandlerArray) - 1, 0 - 1, -1):
            CapitalEventHandlerFactory.capitalEventHandlerArray[index].removeAllListeners()
# from org.allbinary.game.identification.Group import Group


CapitalEventHandlerFactory._static_init()

