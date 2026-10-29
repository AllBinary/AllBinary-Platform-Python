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
# package org.allbinary.game.configuration.persistance

from __future__ import annotations

from org.allbinary.game.configuration.persistance.BasicPersitance import BasicPersitance


class KeyValuePersistance(BasicPersitance):

    def _init_fields(self) -> None:
        self.tsUtil: TsUtil = TsUtil.getInstance()
    

    def __init__(self, recordId: str) -> None:
        super().__init__(recordId)
        self._init_fields()
    

    # throws Exception
    def loadAll(self, abeClientInformation: AbeClientInformationInterface) -> None:
        self.loadAllSize(abeClientInformation, 1)
    

    # throws Exception
    def loadAllSize(self, abeClientInformation: AbeClientInformationInterface, size: int) -> None:
        from org.allbinary.game.configuration.persistance.NullRecordStore import NullRecordStore
        from org.allbinary.game.configuration.persistance.NullRecordFilter import NullRecordFilter
        from org.allbinary.game.configuration.persistance.NullRecordComparator import NullRecordComparator
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            recordStore = RecordStore.openRecordStore(self.getRecordId(abeClientInformation), True)
            recordEnum: RecordEnumeration = recordStore.enumerateRecords(NullRecordFilter.NULL_RECORD_FILTER, NullRecordComparator.NULL_RECORD_COMPARATOR, True)
            hashtable: ABHashtable[str, str] = None
            name: str = None
            value: str = None
            smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
            stringBuffer: StringMaker = StringMaker()
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
                    hashtable = ABHashtable()
                    for index in range(0, size):
                        name = inputStream.readUTF()
                        inputStream.readUTF()
                        value = inputStream.readUTF()
                        hashtable.put(name, value)
                    self.valueList.add(hashtable)
                    self.idList.add(smallIntegerSingletonFactory.getAt(id))
        except Exception as e:
            raise e
        finally:
            if recordStore is not None:
                PreLogUtil.put(self.persistanceStrings.CLOSING_RECORDSTORE, self, self.persistanceStrings.LOAD_ALL)
                recordStore.closeRecordStore()
    

    # throws Exception
    def save(self, abeClientInformation: AbeClientInformationInterface, hashtable: ABHashtable[object, object]) -> None:
        from org.allbinary.game.configuration.persistance.NullRecordStore import NullRecordStore
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            self.logUtil.putF(str(StringMaker().append(self.persistanceStrings.SAVING).append(StringUtil.getInstance().toString(hashtable))), self, self.commonStrings.SAVE)
            recordStore = RecordStore.openRecordStore(self.getRecordId(abeClientInformation), True)
            byteArrayOutputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            outputStream: DataOutputStream = DataOutputStream(byteArrayOutputStream)
            value: str = None
            commonSeps: CommonSeps = CommonSeps.getInstance()
            objectArray: list[object] = HashtableUtil.getInstance().getKeysAsArray(hashtable)
            anyType: object = None
            size: int = len(objectArray)
            for index in range(0, size):
                outputStream.writeUTF(objectArray[index])
                outputStream.writeUTF(commonSeps.EQUALS)
                anyType = objectArray[index]
                value = hashtable.get(anyType)
                outputStream.writeUTF(value)
            tsUtil: TsUtil = TsUtil.getInstance()
            savedGameBytes: list[int] = tsUtil.getByteArray(str(byteArrayOutputStream))
            recordStore.addRecord(savedGameBytes, 0, len(savedGameBytes))
        except Exception as e:
            raise e
        finally:
            if recordStore is not None:
                PreLogUtil.put(self.persistanceStrings.CLOSING_RECORDSTORE, self, self.commonStrings.SAVE)
                recordStore.closeRecordStore()
    

    def get(self, index: int) -> ABHashtable[object, object]:
        hashtable: ABHashtable[object, object] = self.valueList.objectArray[index]
        return hashtable
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.DataInputStream import DataInputStream
# from java.io.DataOutputStream import DataOutputStream
# from javax.microedition.rms.RecordEnumeration import RecordEnumeration
# from javax.microedition.rms.RecordStore import RecordStore
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.HashtableUtil import HashtableUtil


