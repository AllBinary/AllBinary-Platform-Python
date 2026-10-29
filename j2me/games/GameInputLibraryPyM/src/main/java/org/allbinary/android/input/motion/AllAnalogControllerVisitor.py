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


class AllAnalogControllerVisitor(AnalogControllerVisitor):

    def __init__(self) -> None:
        super().__init__()
    

    def process(self, allbinaryLayerManager: AllBinaryLayerManager, analogLocationInputProcessor: AnalogLocationInputProcessor) -> None:
        analogLocationInputList: BasicArrayList = AnalogLocationInputFactory.getInstance().getList()
        analogLocationInput: AnalogLocationInput = None
        for index in range(analogLocationInputList.size() - 1, 0 - 1, -1):
            analogLocationInput = analogLocationInputList.get(index)
            analogLocationInputProcessor.process(allbinaryLayerManager, analogLocationInput)
from org.allbinary.game.input.analog.AnalogLocationInput import AnalogLocationInput
from org.allbinary.game.input.analog.AnalogLocationInputFactory import AnalogLocationInputFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.util.BasicArrayList import BasicArrayList


