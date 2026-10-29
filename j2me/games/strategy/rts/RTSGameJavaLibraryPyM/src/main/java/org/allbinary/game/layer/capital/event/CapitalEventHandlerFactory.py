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



class CapitalEventHandlerFactory:
    capitalEventHandlerArray: list[CapitalEventHandler] = None
    

    @staticmethod
    def _static_init() -> None:
        CapitalEventHandlerFactory.capitalEventHandlerArray = [None] * (10)
        for index in range(len(CapitalEventHandlerFactory.capitalEventHandlerArray) - 1, 0 - 1, -1):
            CapitalEventHandlerFactory.capitalEventHandlerArray[index] = CapitalEventHandler()
    

    @staticmethod
    def getInstance(groupInterface: Group) -> CapitalEventHandler:
        return CapitalEventHandlerFactory.capitalEventHandlerArray[int(groupInterface.getGroupId())]
    

    @staticmethod
    def removeAll() -> None:
        for index in range(len(CapitalEventHandlerFactory.capitalEventHandlerArray) - 1, 0 - 1, -1):
            CapitalEventHandlerFactory.capitalEventHandlerArray[index].removeAllListeners()
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.layer.capital.event.CapitalEventHandler import CapitalEventHandler


CapitalEventHandlerFactory._static_init()

