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
# package org.allbinary.android.input.motion

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.android.input.motion.AnalogControllerVisitor import AnalogControllerVisitor


@java_inherited_overloads
class SingleAnalogControllerVisitor(AnalogControllerVisitor):
    def _java_defaults(self):
        vars(self).setdefault("playerInputId", 0)

    def _init_fields(self) -> None:
        if "playerInputId" not in vars(self): self.playerInputId: int = 0
    

    def __init__(self, playerInputId: int) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.playerInputId = playerInputId
    

    def process(self, allbinaryLayerManager: AllBinaryLayerManager, analogLocationInputProcessor: AnalogLocationInputProcessor) -> None:
        from org.allbinary.game.input.analog.AnalogLocationInput import AnalogLocationInput
        from org.allbinary.game.input.analog.AnalogLocationInputFactory import AnalogLocationInputFactory
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        analogLocationInput: AnalogLocationInput = AnalogLocationInputFactory.getInstance().getInstanceForPlayer(self.playerInputId)
        analogLocationInputProcessor.process(allbinaryLayerManager, analogLocationInput)
# from org.allbinary.game.input.analog.AnalogLocationInput import AnalogLocationInput
# from org.allbinary.game.input.analog.AnalogLocationInputFactory import AnalogLocationInputFactory
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


