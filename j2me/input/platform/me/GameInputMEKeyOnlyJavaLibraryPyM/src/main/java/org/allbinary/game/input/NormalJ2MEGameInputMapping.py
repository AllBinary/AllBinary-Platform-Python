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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.game.input.J2MEGameInputMapping import J2MEGameInputMapping


class NormalJ2MEGameInputMapping(J2MEGameInputMapping):

    def __init__(self) -> None:
        super().__init__()
    

    def getDefault(self) -> InputToGameKeyMapping:
        from org.allbinary.game.input.NormalJ2MEDefaultGameInputMapping import NormalJ2MEDefaultGameInputMapping
        return NormalJ2MEDefaultGameInputMapping().getInputMapping()
from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping


