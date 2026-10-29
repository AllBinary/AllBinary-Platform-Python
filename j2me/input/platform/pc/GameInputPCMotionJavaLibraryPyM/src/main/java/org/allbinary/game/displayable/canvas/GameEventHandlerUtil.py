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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations



class GameEventHandlerUtil:
    

    @staticmethod
    def removeAllListeners() -> None:
        UpGameKeyEventHandler.getInstance().removeAllListeners()
        DownGameKeyEventHandler.getInstance().removeAllListeners()
from org.allbinary.game.input.event.DownGameKeyEventHandler import DownGameKeyEventHandler
from org.allbinary.game.input.event.UpGameKeyEventHandler import UpGameKeyEventHandler


