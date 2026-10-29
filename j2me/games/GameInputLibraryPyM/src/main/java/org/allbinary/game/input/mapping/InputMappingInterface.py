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
# package org.allbinary.game.input.mapping

from __future__ import annotations



# Java interface
class InputMappingInterface:
    

    # throws Exception
    def processInputMapping(self, gameKey: GameKey, input: Input) -> None:
        raise NotImplementedError()
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.Input import Input


