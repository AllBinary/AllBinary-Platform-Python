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


#GameInputPersistanceLibrary
class InputPersistance(BasicPersitance):

    def _init_fields(self) -> None:
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.hashtableUtil: HashtableUtil = HashtableUtil.getInstance()
    

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._init_fields()
    

    # throws Exception
    def loadAll(self, abeClientInformation: AbeClientInformationInterface) -> None:
        from org.allbinary.game.input.GameKeyMappingFactory import GameKeyMappingFactory
        from org.allbinary.game.input.InputFactory import InputFactory
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            recordStore = RecordStore.openRecordStore(self.getRecordId(abeClientInformation), True)
            recordEnum: RecordEnumeration = recordStore.enumerateRecords(NullRecordFilter.NULL_RECORD_FILTER, NullRecordComparator.NULL_RECORD_COMPARATOR, True)
            gameActionInputId: int = 0
            inputId: int = 0
            gameActionInput: Input = None
            input: Input = None
            hashtable: ABHashtable[object, object] = None
            gameKeyFactory: GameKeyMappingFactory = GameKeyMappingFactory.getInstance()
            stringBuffer: StringMaker = StringMaker()
            inputFactory: InputFactory = InputFactory.getInstance()
            smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
            stdUtil: StdUtil = StdUtil.getInstance()
            recordAsBytes: list[int] = None
            byteArrayInputStream: ByteArrayInputStream = None
            inputStream: DataInputStream = None
            while recordEnum.hasNextElement():
                id: int = recordEnum.nextRecordId()
                stringBuffer.delete(0, stringBuffer.length())
                self.logUtil.putF(str(stringBuffer.append(self.persistanceStrings.LOADING_ID).appendint(id)), self, self.persistanceStrings.LOAD_ALL)
                recordAsBytes = self.tsUtil.getRecord(recordStore, id)
                if recordAsBytes is not None:
                    byteArrayInputStream = ByteArrayInputStream(recordAsBytes)
                    inputStream = DataInputStream(byteArrayInputStream)
                    hashtable = stdUtil.createHashtable()
                    value: int = 0
                    while inputStream.available() > 0:
                        gameActionInputIdAsString: str = inputStream.readUTF()
                        value = int(gameActionInputIdAsString)
                        gameActionInputId = value
                        inputStream.readUTF()
                        value = int(inputStream.readUTF())
                        inputId = value
                        gameActionInput = gameKeyFactory.getGameKey(gameActionInputId)
                        input = inputFactory.getInstanceById(inputId)
                        if input == inputFactory.NO_INPUT or gameActionInput is None:
                            stringBuffer.delete(0, stringBuffer.length())
                            if input == inputFactory.NO_INPUT:
                                stringBuffer.append(self.persistanceStrings.ERROR_LOADING_ID)
                                stringBuffer.appendlong(inputId)
                                stringBuffer.append(self.persistanceStrings.GAME_ACTION_INPUT)
                                stringBuffer.appendlong(gameActionInputId)
                                PreLogUtil.put(str(stringBuffer), self, self.persistanceStrings.LOAD_ALL)
                            if gameActionInput is None:
                                stringBuffer.delete(0, stringBuffer.length())
                                stringBuffer.append(self.persistanceStrings.ERROR_LOADING)
                                stringBuffer.appendlong(gameActionInputId)
                                stringBuffer.append(self.persistanceStrings.ID)
                                stringBuffer.appendlong(inputId)
                                PreLogUtil.put(str(stringBuffer), self, self.persistanceStrings.LOAD_ALL)
                        else:
                            pass
                        hashtable.put(input, gameActionInput)
                    self.valueList.add(hashtable)
                    self.idList.add(smallIntegerSingletonFactory.getAt(id))
                else:
                    pass
        except Exception as e:
            raise e
        finally:
            if recordStore is not None:
                PreLogUtil.put(self.persistanceStrings.CLOSING_RECORDSTORE, self, self.persistanceStrings.LOAD_ALL)
                recordStore.closeRecordStore()
    

    # throws Exception
    def save(self, abeClientInformation: AbeClientInformationInterface, hashtable: ABHashtable[object, object]) -> None:
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            stringBuffer: StringMaker = StringMaker()
            PreLogUtil.put(str(stringBuffer.append(self.persistanceStrings.SAVING).append(StringUtil.getInstance().toString(hashtable))), self, self.commonStrings.SAVE)
            recordStore = RecordStore.openRecordStore(self.getRecordId(abeClientInformation), True)
            byteArrayOutputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            outputStream: DataOutputStream = DataOutputStream(byteArrayOutputStream)
            gameActionInput: Input = None
            list_: BasicArrayList = None
            input: Input = None
            savedGameBytes: list[int] = None
            commonSeps: CommonSeps = CommonSeps.getInstance()
            smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
            inputObjectArray: list[object] = self.hashtableUtil.getKeysAsArray(hashtable)
            size: int = len(inputObjectArray)
            for index in range(0, size):
                gameActionInput = inputObjectArray[index]
                list_ = hashtable.get(inputObjectArray[index])
                for index2 in range(0, list_.size()):
                    gameActionInputIdAsString: str = str(smallIntegerSingletonFactory.getAt(gameActionInput.getId()))
                    outputStream.writeUTF(gameActionInputIdAsString)
                    outputStream.writeUTF(commonSeps.EQUALS)
                    input = list_.objectArray[index2]
                    inputIdAsString: str = str(smallIntegerSingletonFactory.getAt(input.getId()))
                    outputStream.writeUTF(inputIdAsString)
            savedGameBytes = byteArrayOutputStream.toByteArray()
            recordStore.addRecord(savedGameBytes, 0, len(savedGameBytes))
        except Exception as e:
            raise e
        finally:
            if recordStore is not None:
                PreLogUtil.put(self.persistanceStrings.CLOSING_RECORDSTORE, self, self.commonStrings.SAVE)
                recordStore.closeRecordStore()
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.DataInputStream import DataInputStream
# from java.io.DataOutputStream import DataOutputStream
# from javax.microedition.rms.RecordEnumeration import RecordEnumeration
# from javax.microedition.rms.RecordStore import RecordStore
from org.allbinary.TsUtil import TsUtil
from org.allbinary.game.configuration.persistance.NullRecordComparator import NullRecordComparator
from org.allbinary.game.configuration.persistance.NullRecordFilter import NullRecordFilter
from org.allbinary.game.configuration.persistance.NullRecordStore import NullRecordStore
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.HashtableUtil import HashtableUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable


