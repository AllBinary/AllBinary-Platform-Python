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
# package org.allbinary.game.input.mapping.event

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class InputMappingEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.inputToGameKeyMapping: InputToGameKeyMapping = InputToGameKeyMapping.getNullInstance()
    

    def __init__(self, anyType: object) -> None:
        super().__init__(anyType)
        self._init_fields()
    

    def setInputToGameKeyMapping(self, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        self.inputToGameKeyMapping = inputToGameKeyMapping
    

    def getInputToGameKeyMapping(self) -> InputToGameKeyMapping:
        return self.inputToGameKeyMapping
from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping


