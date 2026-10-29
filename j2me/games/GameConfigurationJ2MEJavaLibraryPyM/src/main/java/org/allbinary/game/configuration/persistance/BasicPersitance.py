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



class BasicPersitance:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.persistanceStrings: PersistanceStrings = PersistanceStrings.getInstance()
        self.platformRecordIdUtil: PlatformRecordIdUtil = PlatformRecordIdUtil.getInstance()
        self.recordId: str = None
        self.valueList: BasicArrayList = BasicArrayListD()
        self.idList: BasicArrayList = BasicArrayListD()
    

    def __init__(self, recordId: str) -> None:
        self._init_fields()
        self.recordId = recordId
    

    # throws Exception
    def deleteRecoreStore(self, abeClientInformation: AbeClientInformationInterface) -> None:
        RecordStore.deleteRecordStore(self.getRecordId(abeClientInformation))
    

    # throws Exception
    def deleteAll(self, abeClientInformation: AbeClientInformationInterface) -> None:
        size: int = self.idList.size()
        for index in range(0, size):
            integer: int = self.idList.objectArray[index]
            self.delete(abeClientInformation, int(integer))
        self.clear()
    

    # throws Exception
    def delete(self, abeClientInformation: AbeClientInformationInterface, deleteId: int) -> None:
        from org.allbinary.game.configuration.persistance.NullRecordStore import NullRecordStore
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            self.logUtil.putF(str(StringMaker().append(self.persistanceStrings.DELETING_WITH_ID).appendint(deleteId)), self, self.commonStrings.delete)
            recordStore = RecordStore.openRecordStore(self.getRecordId(abeClientInformation), True)
            recordStore.deleteRecord(deleteId)
        except Exception as e:
            raise e
        finally:
            if recordStore is not None:
                PreLogUtil.put(self.persistanceStrings.CLOSING_RECORDSTORE, self, self.commonStrings.delete)
                recordStore.closeRecordStore()
    

    def getRecordId(self, abeClientInformation: AbeClientInformationInterface) -> str:
        return self.platformRecordIdUtil.getRecordId(abeClientInformation, self.recordId)
    

    def getList(self) -> BasicArrayList:
        return self.valueList
    

    def getIds(self) -> BasicArrayList:
        return self.idList
    

    def clear(self) -> None:
        self.valueList.clear()
        self.idList.clear()
# from javax.microedition.rms.RecordStore import RecordStore
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.persistance.PlatformRecordIdUtil import PlatformRecordIdUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.game.configuration.persistance.PersistanceStrings import PersistanceStrings


