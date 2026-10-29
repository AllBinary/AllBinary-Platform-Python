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

import threading
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.game.score.HighScores import HighScores


class RecordStoreHighScores(HighScores):
    hashTable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.platformRecordIdUtil: PlatformRecordIdUtil = PlatformRecordIdUtil.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.RECORD_ID: str = "_HS"
        self.MAXHIGHSCORES: int = 100
        self.gameInfo: GameInfo = None
        self.abeClientInformation: AbeClientInformationInterface = None
        self.recordComparatorInterface: RecordComparator = None
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, gameInfo: GameInfo, name: str, heading: str, columnTwoHeading: str, recordComparatorInterface: RecordComparator) -> None:
        super().__init__(name, heading, columnTwoHeading)
        self._init_fields()
        self.abeClientInformation = abeClientInformation
        self.gameInfo = gameInfo
        self.recordComparatorInterface = recordComparatorInterface
        self.load()
    

    @staticmethod
    def getInstance(abeClientInformation: AbeClientInformationInterface, gameInfo: GameInfo, highScoreName: str, heading: str, columnTwoHeading: str, recordComparatorInterface: RecordComparator) -> HighScores:
        with RecordStoreHighScores._lock:
            return RecordStoreHighScores._getInstance_unlocked(abeClientInformation, gameInfo, highScoreName, heading, columnTwoHeading, recordComparatorInterface)

    @staticmethod
    def _getInstance_unlocked(abeClientInformation: AbeClientInformationInterface, gameInfo: GameInfo, highScoreName: str, heading: str, columnTwoHeading: str, recordComparatorInterface: RecordComparator) -> HighScores:
        highScoresCanBeNull: object = RecordStoreHighScores.hashTable.get(highScoreName)
        if highScoresCanBeNull is None:
            highScores: HighScores = RecordStoreHighScores(abeClientInformation, gameInfo, highScoreName, heading, columnTwoHeading, recordComparatorInterface)
            RecordStoreHighScores.hashTable.put(highScores.getName(), highScores)
            return highScores
        return highScoresCanBeNull
    

    def getRecordId(self, abeClientInformation: AbeClientInformationInterface) -> str:
        return self.platformRecordIdUtil.getRecordId(abeClientInformation, str(StringMaker().append(CommonSeps.getInstance().UNDERSCORE).append(self.getName()).append(self.RECORD_ID)))
    

    def addHighScore(self, newHighScore: HighScore) -> None:
        with self._lock:
            return self._addHighScore_unlocked(newHighScore)

    def _addHighScore_unlocked(self, newHighScore: HighScore) -> None:
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            self.logUtil.putF(str(StringMaker().append("Adding HighScore: ").appendlong(int(newHighScore.getScore()))), self, self.commonStrings.ADD)
            if self.isTooManyHighScores():
                self.logUtil.putF("Removing Lowest Score", self, self.commonStrings.ADD)
                self.removeLowestHighScore()
            recordStore = RecordStore.openRecordStore(self.getRecordId(self.abeClientInformation), True)
            highScoreBytes: list[int] = newHighScore.getAsBytes()
            recordId: int = recordStore.addRecord(highScoreBytes, 0, len(highScoreBytes))
            self.load()
        except RecordStoreException as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.ADD, e)
        except OSError as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.ADD, e)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.ADD, e)
        finally:
            try:
                if recordStore is not None:
                    PreLogUtil.put("Closing RecordStore", self, self.commonStrings.ADD)
                    recordStore.closeRecordStore()
            except RecordStoreException as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.ADD, e)
    

    def removeLowestHighScore(self) -> None:
        from org.allbinary.game.score.HighScore import HighScore
        from org.allbinary.game.score.HighScore import HighScore
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            recordStore = RecordStore.openRecordStore(self.getRecordId(self.abeClientInformation), True)
            recordEnum: RecordEnumeration = recordStore.enumerateRecords(NullRecordFilter.NULL_RECORD_FILTER, NullRecordComparator.NULL_RECORD_COMPARATOR, True)
            scoreComparator: ScoreComparator = (self.recordComparatorInterface)
            bestHighScore: HighScore = HighScore(-1, "none", GameInfo.NONE, scoreComparator.getBestScore())
            recordAsBytes: list[int] = None
            byteArrayInputStream: ByteArrayInputStream = None
            inputStream: DataInputStream = None
            while recordEnum.hasNextElement():
                id: int = recordEnum.nextRecordId()
                recordAsBytes = self.tsUtil.getRecord(recordStore, id)
                if recordAsBytes is not None:
                    byteArrayInputStream = ByteArrayInputStream(recordAsBytes)
                    inputStream = DataInputStream(byteArrayInputStream)
                    name: str = inputStream.readUTF()
                    nextScore: int = inputStream.readLong()
                    nextCurrentHighScore: HighScore = HighScore(id, name, GameInfo.NONE, nextScore)
                    if self.recordComparatorInterface.compare(nextCurrentHighScore.getAsBytes(), bestHighScore.getAsBytes()) == RecordComparator.FOLLOWS:
                        bestHighScore = nextCurrentHighScore
            if bestHighScore.getId() != -1:
                self.logUtil.putF(str(StringMaker().append("Removing Lowest HighScore: ").appendlong(int(bestHighScore.getScore()))), self, self.commonStrings.LOAD)
                recordStore.deleteRecord(bestHighScore.getId())
        except RecordStoreException as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "removeLowestHighScore", e)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "removeLowestHighScore", e)
        finally:
            try:
                if recordStore is not None:
                    PreLogUtil.put("Closing RecordStore", self, "removeLowestHighScore")
                    recordStore.closeRecordStore()
            except RecordStoreException as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "removeLowestHighScore", e)
    

    def load(self) -> None:
        from org.allbinary.game.score.HighScore import HighScore
        recordStore: RecordStore = NullRecordStore.NULL_RECORD_STORE
        try:
            recordStore = RecordStore.openRecordStore(self.getRecordId(self.abeClientInformation), True)
            self.setList(BasicArrayListD())
            recordEnum: RecordEnumeration = recordStore.enumerateRecords(NullRecordFilter.NULL_RECORD_FILTER, NullRecordComparator.NULL_RECORD_COMPARATOR, True)
            recordAsBytes: list[int] = None
            byteArrayInputStream: ByteArrayInputStream = None
            inputStream: DataInputStream = None
            while recordEnum.hasNextElement():
                id: int = recordEnum.nextRecordId()
                recordAsBytes = self.tsUtil.getRecord(recordStore, id)
                if recordAsBytes is not None:
                    byteArrayInputStream = ByteArrayInputStream(recordAsBytes)
                    inputStream = DataInputStream(byteArrayInputStream)
                    try:
                        name: str = inputStream.readUTF()
                        score: int = inputStream.readLong()
                        newHighScore: HighScore = HighScore(id, name, GameInfo.NONE, score)
                        list_: BasicArrayList = self.getList()
                        size: int = list_.size()
                        lastIndex: int = size
                        for index in range(0, size):
                            highScore: HighScore = list_.objectArray[index]
                            if self.recordComparatorInterface.compare(newHighScore.getAsBytes(), highScore.getAsBytes()) == RecordComparator.PRECEDES:
                                lastIndex = index
                                break
                        list_.addAt(lastIndex, newHighScore)
                    except EOFException as e:
                        self.logUtil.put("EOF", self, self.commonStrings.LOAD, e)
                        raise e
        except RecordStoreNotFoundException as e:
            self.logUtil.put("No High Scores", self, self.commonStrings.LOAD, e)
        except RecordStoreException as e:
            self.logUtil.put(self.commonStrings.UNKNOWN, self, self.commonStrings.LOAD, e)
        except OSError as e:
            self.logUtil.put(self.commonStrings.UNKNOWN, self, self.commonStrings.LOAD, e)
        except Exception as e:
            self.logUtil.put(self.commonStrings.UNKNOWN, self, self.commonStrings.LOAD, e)
        finally:
            try:
                if recordStore is not None:
                    PreLogUtil.put("Closing RecordStore", self, self.commonStrings.LOAD)
                    recordStore.closeRecordStore()
            except RecordStoreException as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.LOAD, e)
    

    def isTooManyHighScores(self) -> bool:
        if self.getList() is not None and self.getList().size() < self.MAXHIGHSCORES:
            return False
        else:
            self.logUtil.putF(str(StringMaker().append("HighScores RecordStore Max Reached: ").appendint(self.MAXHIGHSCORES)), self, "isTooManyHighScores")
            return True
    

    # throws Exception
    def isBestScore(self, newHighScore: HighScore) -> bool:
        with self._lock:
            return self._isBestScore_unlocked(newHighScore)

    def _isBestScore_unlocked(self, newHighScore: HighScore) -> bool:
        try:
            if not self.isTooManyHighScores():
                self.logUtil.putF("Slot Available for a High Score", self, "isBestScore")
                return True
            else:
                list_: BasicArrayList = self.getList()
                size: int = list_.size()
                for index in range(0, size):
                    highScore: HighScore = list_.objectArray[index]
                    if self.recordComparatorInterface.compare(newHighScore.getAsBytes(), highScore.getAsBytes()) == RecordComparator.FOLLOWS:
                        self.logUtil.putF("Obtained a High Score", self, "isBestScore")
                        return True
            self.logUtil.putF("Not a High Score", self, "isBestScore")
            return False
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.ADD, e)
            raise e
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(super()))
        list_: BasicArrayList = self.getList()
        size: int = list_.size()
        for index in range(0, size):
            highScore: HighScore = list_.objectArray[index]
            stringBuffer.append(highScore.getScoreString())
            stringBuffer.append(CommonSeps.getInstance().COMMA_SEP)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.DataInputStream import DataInputStream
# from java.io.EOFException import EOFException
# from java.io.IOException import IOException
# from javax.microedition.rms.RecordComparator import RecordComparator
# from javax.microedition.rms.RecordEnumeration import RecordEnumeration
# from javax.microedition.rms.RecordStore import RecordStore
# from javax.microedition.rms.RecordStoreException import RecordStoreException
# from javax.microedition.rms.RecordStoreNotFoundException import RecordStoreNotFoundException
from org.allbinary.TsUtil import TsUtil
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.configuration.persistance.NullRecordComparator import NullRecordComparator
from org.allbinary.game.configuration.persistance.NullRecordFilter import NullRecordFilter
from org.allbinary.game.configuration.persistance.NullRecordStore import NullRecordStore
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.persistance.PlatformRecordIdUtil import PlatformRecordIdUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


