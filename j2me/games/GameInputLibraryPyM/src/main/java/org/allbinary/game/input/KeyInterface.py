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
# package org.allbinary.game.input

from __future__ import annotations



# Java interface
class KeyInterface:
    

    def keyPressed(self, keyCode: int) -> None:
        raise NotImplementedError()
    

    def keyReleased(self, keyCode: int) -> None:
        raise NotImplementedError()
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        raise NotImplementedError()
    

    def keyReleasedByDevice(self, keyCode: int, deviceId: int) -> None:
        raise NotImplementedError()


