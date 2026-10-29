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

from org.allbinary.game.configuration.persistance.BasicPersitance import BasicPersitance


#GameInputNoPersistanceLibrary
class InputPersistance(BasicPersitance):

    def _init_fields(self) -> None:
        self.hashtableUtil: HashtableUtil = HashtableUtil.getInstance()
    

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._init_fields()
    

    # throws Exception
    def loadAll(self, abeClientInformation: AbeClientInformationInterface) -> None:
        recordStore: RecordStore = RecordStore.openRecordStore(self.getRecordId(abeClientInformation), True)
        recordEnum: RecordEnumeration = recordStore.enumerateRecords(NullRecordFilter.NULL_RECORD_FILTER, NullRecordComparator.NULL_RECORD_COMPARATOR, True)
        hashtable: ABHashtable[object, object] = None
        stringBuffer: StringMaker = StringMaker()
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        id: int = 0
        while recordEnum.hasNextElement():
            id = recordEnum.nextRecordId()
            stringBuffer.delete(0, stringBuffer.length())
            self.logUtil.putF(str(stringBuffer.append(self.persistanceStrings.LOADING_ID).appendint(id)), self, self.persistanceStrings.LOAD_ALL)
            hashtable = StdUtil.getInstance().createHashtable()
            self.valueList.add(hashtable)
            self.idList.add(smallIntegerSingletonFactory.getAt(id))
        recordStore.closeRecordStore()
    

    # throws Exception
    def save(self, abeClientInformation: AbeClientInformationInterface, hashtable: ABHashtable[object, object]) -> None:
        PreLogUtil.put(str(StringMaker().append(self.persistanceStrings.NOT_SAVING).append(StringUtil.getInstance().toString(hashtable))), self, self.commonStrings.SAVE)
        recordStore: RecordStore = RecordStore.openRecordStore(self.getRecordId(abeClientInformation), True)
        gameActionInput: Input = None
        list_: BasicArrayList = None
        input: Input = None
        inputObjectArray: list[object] = self.hashtableUtil.getKeysAsArray(hashtable)
        size: int = len(inputObjectArray)
        for index in range(0, size):
            gameActionInput = inputObjectArray[index]
            list_ = hashtable.get(inputObjectArray[index])
            for index2 in range(0, list_.size()):
                input = list_.get(index2)
        recordStore.closeRecordStore()
# from javax.microedition.rms.RecordEnumeration import RecordEnumeration
# from javax.microedition.rms.RecordStore import RecordStore
from org.allbinary.game.configuration.persistance.NullRecordComparator import NullRecordComparator
from org.allbinary.game.configuration.persistance.NullRecordFilter import NullRecordFilter
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.HashtableUtil import HashtableUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable


