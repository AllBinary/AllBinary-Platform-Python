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

from org.allbinary.logic.NullUtil import NullUtil


#GameInputNoPersistanceLibrary
class PersistentInputMapping:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.enumerationUtil: EnumerationUtil = EnumerationUtil.getInstance()
        self.inputMapping: InputToGameKeyMapping = InputToGameKeyMapping()
        self.inputMappingEventListenerInterface: InputMappingEventListenerInterface = NullInputMappingEventListener.NULL_INPUT_MAPPING_EVENT_LISTENER
        self.inputPersistance: InputPersistance = None
        self.inputMappingEvent: InputMappingEvent = InputMappingEvent(self)
    

    @staticmethod
    def getNullInstance() -> PersistentInputMapping:
        if PersistentInputMapping.instance == NullUtil.getInstance().NULL_OBJECT:
            PersistentInputMapping.instance = PersistentInputMapping(GamePersistanceStrings.getInstance().SAVED_INPUT_CONFIGURATION_RECORD_ID)
        return PersistentInputMapping.instance
    

    def __init__(self, name: str) -> None:
        self._init_fields()
        self.inputPersistance = InputPersistance(name)
    

    def getTotalMapped(self) -> int:
        return self.getInputMapping().getHashtable().size()
    

    def isDefaultNew(self) -> bool:
        return False
    

    def getDefault(self) -> InputToGameKeyMapping:
        from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
        return InputToGameKeyMapping.getNullInstance()
    

    # throws Exception
    def setDefault(self, abeClientInformation: AbeClientInformationInterface) -> None:
        self.getInputMapping().removeAll()
        self.getInputMapping().addMapping(self.getDefault())
        self.save(abeClientInformation)
    

    # throws Exception
    def update(self, abeClientInformation: AbeClientInformationInterface) -> None:
        self.inputPersistance.deleteAll(abeClientInformation)
        self.save(abeClientInformation)
    

    # throws Exception
    def save(self, abeClientInformation: AbeClientInformationInterface) -> None:
        self.inputPersistance.save(abeClientInformation, self.getInputMapping().getHashtable())
        self.inputMappingEvent.setInputToGameKeyMapping(self.getInputMapping())
        if self.getInputMappingEventListenerInterface() is not None:
            self.getInputMappingEventListenerInterface().onInputMappingEvent(self.inputMappingEvent)
    

    # throws Exception
    def init(self, abeClientInformation: AbeClientInformationInterface) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.INIT)
        try:
            self.inputPersistance.loadAll(abeClientInformation)
        except Exception as e:
            PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
            self.inputPersistance.deleteRecoreStore(abeClientInformation)
            self.setDefault(abeClientInformation)
            self.inputPersistance.loadAll(abeClientInformation)
        list_: BasicArrayList = self.inputPersistance.getList()
        totalMappedTo: int = 0
        size: int = list_.size()
        hashtable: ABHashtable[object, object] = None
        enumeration: Enumeration = None
        mappedToInput: Input = None
        gameActionInput: Input = None
        for index in range(0, size):
            hashtable = list_.objectArray[index]
            enumeration = hashtable.keys()
            while self.enumerationUtil.hasMoreElements(enumeration):
                mappedToInput = self.enumerationUtil.nextElement(enumeration)
                gameActionInput = hashtable.get(mappedToInput)
                totalMappedTo += 1
                self.getInputMapping().add(gameActionInput, mappedToInput)
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("End - Total Loaded Keys Mapped: ")
        stringBuffer.appendint(self.getTotalMapped())
        stringBuffer.append(" to: ")
        stringBuffer.appendint(totalMappedTo)
        self.logUtil.putF(str(stringBuffer), self, self.commonStrings.INIT)
    

    def setInputMappingEventListenerInterface(self, inputMappingEventListenerInterface: InputMappingEventListenerInterface) -> None:
        self.inputMappingEventListenerInterface = inputMappingEventListenerInterface
    

    def getInputMappingEventListenerInterface(self) -> InputMappingEventListenerInterface:
        return self.inputMappingEventListenerInterface
    

    def getInputMapping(self) -> InputToGameKeyMapping:
        return self.inputMapping
    

    # throws Exception
    def isDelete(self, input: Input) -> bool:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def isSystemInput(self, input: Input) -> bool:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
# from java.util.Enumeration import Enumeration
from org.allbinary.game.configuration.persistance.GamePersistanceStrings import GamePersistanceStrings
from org.allbinary.game.input.Input import Input
from org.allbinary.game.input.InputPersistance import InputPersistance
from org.allbinary.game.input.mapping.event.InputMappingEvent import InputMappingEvent
from org.allbinary.game.input.mapping.event.InputMappingEventListenerInterface import InputMappingEventListenerInterface
from org.allbinary.game.input.mapping.event.NullInputMappingEventListener import NullInputMappingEventListener
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.EnumerationUtil import EnumerationUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping


