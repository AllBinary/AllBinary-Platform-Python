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

from java.lang.JavaRuntimeStatic import java_predicate
import threading
from java.lang.JavaRuntimeStatic import lazy_static


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
        __class__._init_fields(self)
    

    # throws InitException
    def set_j0(self) -> None:
        with self._lock:
            return __class__.__dict__["_set_j0_unlocked"].__get__(self, __class__)()

    def _set_j0_unlocked(self) -> None:
        from org.allbinary.business.init.InitInfoEntity import InitInfoEntity
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            initInfoEntity: InitInfoEntity = InitInfoEntity()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
                PreLogUtil.put("created entity", "InitInfo", "set()")
            if not (java_predicate(initInfoEntity, "is")):
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
    

    def set_j1(self, hashMap: HashMap) -> None:
        with self._lock:
            return __class__.__dict__["_set_j1_unlocked"].__get__(self, __class__)(hashMap)

    def _set_j1_unlocked(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        try:
            self.testing = hashMap.get(self.TESTING)
            self.mainPath = AbPath(hashMap.get(self.MAINPATH), StringUtil.getInstance().EMPTY_STRING)
            self.testHtmlPath = AbPath(hashMap.get(self.TESTHTMLPATH), StringUtil.getInstance().EMPTY_STRING)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE("error", "InitInfo", "set()", e)

    def set(self, *args):
        implementation = __class__.__dict__.get("set_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().set(*args)
    

    def get(self) -> None:
        with self._lock:
            return __class__.__dict__["_get_unlocked"].__get__(self, __class__)()

    def _get_unlocked(self) -> None:
        from org.allbinary.business.init.InitInfoEntity import InitInfoEntity
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
            return __class__.__dict__["_setHasRead_unlocked"].__get__(self, __class__)(value)

    def _setHasRead_unlocked(self, value: bool) -> None:
        self.hasRead = value
    

    def updateIfNeeded(self) -> None:
        with self._lock:
            return __class__.__dict__["_updateIfNeeded_unlocked"].__get__(self, __class__)()

    def _updateIfNeeded_unlocked(self) -> None:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if not (self.hasRead):
                self.hasRead = True
                self.get()
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE("error", "InitInfo", "updateIfNeeded()", e)
            return
    

    def isTesting(self) -> bool:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
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
        from org.allbinary.logic.io.path.AbPath import AbPath
        self.testHtmlPath = value
    

    def setMainPath(self, value: AbPath) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        self.mainPath = value
    

    def isMainPathValid(self, abPath: AbPath) -> bool:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return True
    

    def isTestHtmlPathValid(self, abPath: AbPath) -> bool:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return True
    

    # throws Exception
    def isTestingValid(self, testing: str) -> bool:
        from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
        return BooleanUtil.getInstance().isStringBoolean(testing)
    

    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(self.TESTING, self.getTesting())
        hashMap.put(self.MAINPATH, self.getMainPath())
        hashMap.put(self.TESTHTMLPATH, self.getTestHtmlPath())
        return hashMap
# from java.util.HashMap import HashMap
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
# from org.allbinary.logic.string.StringUtil import StringUtil


def _InitInfo_instance() -> object:
    return InitInfo()

lazy_static(InitInfo, "instance", _InitInfo_instance)

