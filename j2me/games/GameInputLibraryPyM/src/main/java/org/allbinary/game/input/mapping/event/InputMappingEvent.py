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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


@java_inherited_overloads
class InputMappingEvent(AllBinaryEventObject):
    def _java_defaults(self):
        vars(self).setdefault("inputToGameKeyMapping", None)

    def _init_fields(self) -> None:
        from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
        self.inputToGameKeyMapping: InputToGameKeyMapping = InputToGameKeyMapping.getNullInstance()
    

    def __init__(self, anyType: object) -> None:
        __class__._java_defaults(self)
        super().__init__(anyType)
        __class__._init_fields(self)
    

    def setInputToGameKeyMapping(self, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
        self.inputToGameKeyMapping = inputToGameKeyMapping
    

    def getInputToGameKeyMapping(self) -> InputToGameKeyMapping:
        from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
        return self.inputToGameKeyMapping
# from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping


