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
# package org.allbinary.game.init

from __future__ import annotations



# Java interface
class GameInitializationInterface:
    

    # throws Exception
    def init(self, abeClientInformation: AbeClientInformationInterface, commandListener: CommandListener, level: int) -> None:
        raise NotImplementedError()
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


