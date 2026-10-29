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
# package org.allbinary.game.score

from __future__ import annotations



class HighScoreNamePersistanceSingleton:
    SINGLETON: HighScoreNamePersistanceSingleton = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.platformRecordIdUtil: PlatformRecordIdUtil = PlatformRecordIdUtil.getInstance()
        self.RECORD_ID: str = "_SN"
        self.name: str = StringUtil.getInstance().EMPTY_STRING
        self.nameBasicArrayList: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> HighScoreNamePersistanceSingleton:
        return HighScoreNamePersistanceSingleton.SINGLETON
    

    def clear(self) -> None:
        self.name = StringUtil.getInstance().EMPTY_STRING
    

    # throws Exception
    def deleteAll(self, abeClientInformation: AbeClientInformationInterface, gameInfo: GameInfo) -> None:
        size: int = self.nameBasicArrayList.size()
        for index in range(0, size):
            integer: int = self.nameBasicArrayList.objectArray[index]
            self.delete(abeClientInformation, gameInfo, int(integer))
        self.clear()
    

    def getRecordId(self, abeClientInformation: AbeClientInformationInterface) -> str:
        return self.platformRecordIdUtil.getRecordId(abeClientInformation, self.RECORD_ID)
    

    # throws Exception
    def delete(self, abeClientInformation: AbeClientInformationInterface, gameInfo: GameInfo, deleteId: int) -> None:
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            self.logUtil.putF(str(StringMaker().append("Deleting: ").appendint(deleteId)), self, self.commonStrings.delete)
            recordStore = RecordStore.openRecordStore(self.getRecordId(abeClientInformation), True)
            recordStore.deleteRecord(deleteId)
        except Exception as e:
            raise e
        finally:
            if recordStore is not None:
                PreLogUtil.put("Closing RecordStore", self, self.commonStrings.delete)
                recordStore.closeRecordStore()
    

    def getIds(self) -> BasicArrayList:
        return self.nameBasicArrayList
    

    def load(self, abeClientInformation: AbeClientInformationInterface, gameInfo: GameInfo) -> str:
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            if self.name == StringUtil.getInstance().EMPTY_STRING:
                LOADING_ID: str = "Loading id: "
                recordStore = RecordStore.openRecordStore(self.getRecordId(abeClientInformation), True)
                recordEnum: RecordEnumeration = recordStore.enumerateRecords(NullRecordFilter.NULL_RECORD_FILTER, NullRecordComparator.NULL_RECORD_COMPARATOR, True)
                smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
                recordAsBytes: list[int] = None
                byteArrayInputStream: ByteArrayInputStream = None
                inputStream: DataInputStream = None
                while recordEnum.hasNextElement():
                    id: int = recordEnum.nextRecordId()
                    self.logUtil.putF(str(StringMaker().append(LOADING_ID).appendint(id)), self, self.commonStrings.LOAD)
                    recordAsBytes = self.tsUtil.getRecord(recordStore, id)
                    byteArrayInputStream = ByteArrayInputStream(recordAsBytes)
                    inputStream = DataInputStream(byteArrayInputStream)
                    while inputStream.available() > 0:
                        self.name = inputStream.readUTF()
                    self.nameBasicArrayList.add(smallIntegerSingletonFactory.getAt(id))
        except Exception as e:
            self.save(abeClientInformation, gameInfo, self.name)
            self.logUtil.putF(str(StringMaker().append(self.commonStrings.EXCEPTION_LABEL).append(ExceptionUtil.getInstance().getStackTrace(e))), self, self.commonStrings.LOAD)
        finally:
            try:
                if recordStore is not None:
                    PreLogUtil.put("Closing RecordStore", self, self.commonStrings.LOAD)
                    recordStore.closeRecordStore()
            except RecordStoreException as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.LOAD, e)
        return self.name
    

    def save(self, abeClientInformation: AbeClientInformationInterface, gameInfo: GameInfo, name: str) -> None:
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            self.logUtil.putF(str(StringMaker().append("Saving: ").append(name)), self, self.commonStrings.SAVE)
            recordStore = RecordStore.openRecordStore(self.getRecordId(abeClientInformation), True)
            byteArrayOutputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            outputStream: DataOutputStream = DataOutputStream(byteArrayOutputStream)
            outputStream.writeUTF(name)
            savedGameBytes: list[int] = byteArrayOutputStream.toByteArray()
            recordStore.addRecord(savedGameBytes, 0, len(savedGameBytes))
            self.name = name
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.SAVE, e)
        finally:
            try:
                if recordStore is not None:
                    PreLogUtil.put("Closing RecordStore", self, self.commonStrings.SAVE)
                    recordStore.closeRecordStore()
            except RecordStoreException as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.SAVE, e)
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.DataInputStream import DataInputStream
# from java.io.DataOutputStream import DataOutputStream
# from javax.microedition.rms.RecordEnumeration import RecordEnumeration
# from javax.microedition.rms.RecordStore import RecordStore
# from javax.microedition.rms.RecordStoreException import RecordStoreException
from org.allbinary.TsUtil import TsUtil
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.configuration.persistance.NullRecordComparator import NullRecordComparator
from org.allbinary.game.configuration.persistance.NullRecordFilter import NullRecordFilter
from org.allbinary.game.configuration.persistance.NullRecordStore import NullRecordStore
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.java.exception.ExceptionUtil import ExceptionUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.persistance.PlatformRecordIdUtil import PlatformRecordIdUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


HighScoreNamePersistanceSingleton.SINGLETON = HighScoreNamePersistanceSingleton()

