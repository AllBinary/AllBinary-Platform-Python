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

from org.allbinary.android.input.motion.AnalogControllerVisitor import AnalogControllerVisitor


class SingleAnalogControllerVisitor(AnalogControllerVisitor):

    def _init_fields(self) -> None:
        self.playerInputId: int = None
    

    def __init__(self, playerInputId: int) -> None:
        super().__init__()
        self._init_fields()
        self.playerInputId = playerInputId
    

    def process(self, allbinaryLayerManager: AllBinaryLayerManager, analogLocationInputProcessor: AnalogLocationInputProcessor) -> None:
        analogLocationInput: AnalogLocationInput = AnalogLocationInputFactory.getInstance().getInstanceForPlayer(self.playerInputId)
        analogLocationInputProcessor.process(allbinaryLayerManager, analogLocationInput)
from org.allbinary.game.input.analog.AnalogLocationInput import AnalogLocationInput
from org.allbinary.game.input.analog.AnalogLocationInputFactory import AnalogLocationInputFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


