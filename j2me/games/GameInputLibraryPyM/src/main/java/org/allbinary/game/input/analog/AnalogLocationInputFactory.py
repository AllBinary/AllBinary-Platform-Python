# Generated Code Do Not Modify
# package org.allbinary.game.input.analog

from __future__ import annotations



class AnalogLocationInputFactory:
    instance: AnalogLocationInputFactory = None

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> AnalogLocationInputFactory:
        return AnalogLocationInputFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def addPlayer(self, playerInputId: int) -> None:
        from org.allbinary.game.input.analog.AnalogLocationInput import AnalogLocationInput
        from org.allbinary.game.input.analog.AnalogLocationInput import AnalogLocationInput
        from org.allbinary.game.input.analog.AnalogLocationInput import AnalogLocationInput
        analogLocationInput: AnalogLocationInput = AnalogLocationInput.NULL_ANALOG_LOCATION_INPUT
        if playerInputId < self.list_.size():
            analogLocationInput = self.list_.get(playerInputId)
        if analogLocationInput == AnalogLocationInput.NULL_ANALOG_LOCATION_INPUT:
            analogLocationInput = AnalogLocationInput(playerInputId)
            self.list_.add(analogLocationInput)
    

    def getInstanceForPlayer(self, playerInputId: int) -> AnalogLocationInput:
        return self.list_.get(playerInputId)
    

    def getList(self) -> BasicArrayList:
        return self.list_
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


AnalogLocationInputFactory.instance = AnalogLocationInputFactory()

