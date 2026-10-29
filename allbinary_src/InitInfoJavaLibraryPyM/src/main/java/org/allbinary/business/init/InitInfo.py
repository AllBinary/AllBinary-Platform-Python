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
# package org.allbinary.business.init

from __future__ import annotations

import threading


class InitInfo:
    instance: InitInfo = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.TESTING: str = "TESTING"
        self.MAINPATH: str = "MAINPATH"
        self.TESTHTMLPATH: str = "TESTHTMLPATH"
        self.testing: str = None
        self.mainPath: AbPath = None
        self.testHtmlPath: AbPath = None
        self.hasRead: bool = False
    

    @staticmethod
    def getInstance() -> InitInfo:
        return InitInfo.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws InitException
    def set(self) -> None:
        with self._lock:
            return self._set_unlocked()

    def _set_unlocked(self) -> None:
        from org.allbinary.business.init.InitInfoEntity import InitInfoEntity
        try:
            initInfoEntity: InitInfoEntity = InitInfoEntity()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
                PreLogUtil.put("created entity", "InitInfo", "set()")
            if not initInfoEntity.is_():
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
                    PreLogUtil.put("adding", "InitInfo", "set()")
                initInfoEntity.add()
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
                    PreLogUtil.put("update", "InitInfo", "set()")
                initInfoEntity.update()
            self.hasRead = False
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE("error", "InitInfo", "set()", e)
    

    # Java overloaded method: Python keeps the last definition
    def set(self, hashMap: dict) -> None:
        with self._lock:
            return self._set_unlocked(hashMap)

    def _set_unlocked(self, hashMap: dict) -> None:
        try:
            self.testing = hashMap.get(self.TESTING)
            self.mainPath = AbPath(hashMap.get(self.MAINPATH), StringUtil.getInstance().EMPTY_STRING)
            self.testHtmlPath = AbPath(hashMap.get(self.TESTHTMLPATH), StringUtil.getInstance().EMPTY_STRING)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE("error", "InitInfo", "set()", e)
    

    def get(self) -> None:
        with self._lock:
            return self._get_unlocked()

    def _get_unlocked(self) -> None:
        from org.allbinary.business.init.InitInfoEntity import InitInfoEntity
        try:
            self.testing = None
            self.mainPath = None
            self.testHtmlPath = None
            initInfoEntity: InitInfoEntity = InitInfoEntity()
            initInfoEntity.get()
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE("error", "InitInfo", "set()", e)
            return
    

    def setHasRead(self, value: bool) -> None:
        with self._lock:
            return self._setHasRead_unlocked(value)

    def _setHasRead_unlocked(self, value: bool) -> None:
        self.hasRead = value
    

    def updateIfNeeded(self) -> None:
        with self._lock:
            return self._updateIfNeeded_unlocked()

    def _updateIfNeeded_unlocked(self) -> None:
        try:
            if not self.hasRead:
                self.hasRead = True
                self.get()
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE("error", "InitInfo", "updateIfNeeded()", e)
            return
    

    def isTesting(self) -> bool:
        try:
            self.updateIfNeeded()
            return BooleanUtil.getInstance().getFromString(self.testing)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE("error", "InitInfo", "updateIfNeeded()", e)
            return False
    

    def getTesting(self) -> str:
        self.updateIfNeeded()
        return self.testing
    

    def getTestHtmlPath(self) -> str:
        self.updateIfNeeded()
        if self.testHtmlPath is not None:
            return str(self.testHtmlPath)
        else:
            return None
    

    def getMainPath(self) -> str:
        self.updateIfNeeded()
        if self.mainPath is not None:
            return str(self.mainPath)
        else:
            return None
    

    def setTesting(self, value: str) -> None:
        self.testing = value
    

    def setTestHtmlPath(self, value: AbPath) -> None:
        self.testHtmlPath = value
    

    def setMainPath(self, value: AbPath) -> None:
        self.mainPath = value
    

    def isMainPathValid(self, abPath: AbPath) -> bool:
        return True
    

    def isTestHtmlPathValid(self, abPath: AbPath) -> bool:
        return True
    

    # throws Exception
    def isTestingValid(self, testing: str) -> bool:
        return BooleanUtil.getInstance().isStringBoolean(testing)
    

    def toHashMap(self) -> dict:
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(self.TESTING, self.getTesting())
        hashMap.put(self.MAINPATH, self.getMainPath())
        hashMap.put(self.TESTHTMLPATH, self.getTestHtmlPath())
        return hashMap
# from java.util.HashMap import HashMap
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
from org.allbinary.logic.string.StringUtil import StringUtil


InitInfo.instance = InitInfo()

