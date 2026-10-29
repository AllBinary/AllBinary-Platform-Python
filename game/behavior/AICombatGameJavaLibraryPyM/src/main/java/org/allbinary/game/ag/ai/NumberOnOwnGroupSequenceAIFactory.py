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
# package org.allbinary.game.ag.ai

from __future__ import annotations



class NumberOnOwnGroupSequenceAIFactory:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getInstance(self, hashtable: ABHashtable[object, object], artificialIntelligenceInterface: list[ArtificialIntelligenceInterface], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> ArtificialIntelligenceInterface:
        from org.allbinary.game.ag.ai.NumberInSameGroupSequence import NumberInSameGroupSequence
        from org.allbinary.game.ag.ai.NumberOnOwnGroupSequenceAI import NumberOnOwnGroupSequenceAI
        integerArray: list[int] = NumberInSameGroupSequence.getInstance().NUMBER_ON_SAME_TEAM_SEQUENCE
        list_: BasicArrayList = BasicArrayListD()
        for index in range(0, len(integerArray)):
            integerCanBeNull: object = hashtable.get(integerArray[index])
            if integerCanBeNull is None:
                break
            list_.add(integerCanBeNull)
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Total AI Properties: ")
        stringBuffer.appendint(list_.size())
        stringBuffer.append(" == Total AI: ")
        stringBuffer.appendint(len(artificialIntelligenceInterface))
        stringBuffer.append(" + 1")
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(str(stringBuffer), self, commonStrings.GET_INSTANCE)
        if len(artificialIntelligenceInterface) - 1 > list_.size():
            raise Exception("Not enough AI properties.")
        if len(artificialIntelligenceInterface) - 1 < list_.size():
            raise Exception("Too Many AI properties.")
        numberOnSameTeam: list[int] = [None] * (list_.size())
        for index in range(0, len(numberOnSameTeam)):
            numberOnSameTeam[index] = list_.objectArray[index]
        return NumberOnOwnGroupSequenceAI(numberOnSameTeam, artificialIntelligenceInterface, ownerLayerInterface, gameInput)
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


