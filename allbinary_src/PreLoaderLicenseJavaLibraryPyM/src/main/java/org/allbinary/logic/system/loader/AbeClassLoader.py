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
# package org.allbinary.logic.system.loader

from __future__ import annotations

import threading
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.system.loader.ClassLoader import ClassLoader


class AbeClassLoader(ClassLoader):
    classes: Map = StdUtil.getInstance().createHashMap()
    PATH: str = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abCryptUtil: AbCryptUtil = AbCryptUtil.getInstance()
        self.LOAD_CLASS: str = "loadClass"
        self.ENCRYPTED_EXTENSION: str = str(AbPathData.getInstance().EXTENSION_SEP) + "abc"
        self.key: str = None
    

    def __init__(self, parent: ClassLoader, key: str) -> None:
        super().__init__(parent)
        self._init_fields()
        self.key = key
        AbeClassLoader.PATH = str(org.allbinary.globals.URLGLOBALS.getWebappPath()) + "WEB-INF/classes/"
    

    def findLoadedClass1(self, name: str) -> type:
        return AbeClassLoader.classes.get(name)
    

    # throws ClassNotFoundException
    def loadClass(self, name: str) -> type:
        with self._lock:
            return self._loadClass_unlocked(name)

    def _loadClass_unlocked(self, name: str) -> type:
        return self.loadClass(name, False)
    

    # throws ClassNotFoundException
    # Java overloaded method: Python keeps the last definition
    def loadClass(self, name: str, resolve: bool) -> type:
        with self._lock:
            return self._loadClass_unlocked(name, resolve)

    def _loadClass_unlocked(self, name: str, resolve: bool) -> type:
        from org.allbinary.logic.system.loader.ClassNotFoundException import ClassNotFoundException
        from org.allbinary.logic.system.loader.ClassNotFoundException import ClassNotFoundException
        loadedWith: str = "findLoadedClass1"
        logBuffer: LogBuffer = LogBuffer()
        try:
            myClass: type = self.findLoadedClass1(name)
            if myClass is None:
                try:
                    loadedWith = "super.loadClass"
                    normalClass: type = super().loadClass(name, resolve)
                    if normalClass is not None:
                        return normalClass
                except ClassNotFoundException as e:
                    logBuffer.add(LogFactory.getInstance("Failed to Load Class: " + name + "\nwith: " + loadedWith, self, self.LOAD_CLASS, e))
                except Exception as e:
                    logBuffer.add(LogFactory.getInstance("Failed to Load Class: " + name + "\nwith: " + loadedWith, self, self.LOAD_CLASS, e))
                except NoClassDefFoundError as e:
                    logBuffer.add(LogFactory.getInstanceF("NoClassDefFoundError Failed Loaded Class: " + name + "\nwith: " + loadedWith, self, self.LOAD_CLASS))
                classBytes: list[int] = self.loadClassBytesFromFile(name)
                if classBytes is None:
                    raise ClassNotFoundException("My Bytes not loaded for: " + name + "\nwith: " + "loadClassBytes")
                myClass = self.defineClass(name, classBytes, 0, len(classBytes))
                if myClass is None:
                    raise ClassNotFoundException("My Class Not Defineable for: " + name + "\nwith: " + "loadClassBytes")
                AbeClassLoader.classes.put(name, myClass)
            else:
                logBuffer.add(LogFactory.getInstanceF("Already Loaded: " + name + "\nwith: " + loadedWith, self, self.LOAD_CLASS))
            self.resolveClass(myClass)
            return myClass
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LOADERERROR):
                logBuffer.logAll()
                self.logUtil.put("Failure loading: " + name + "\nwith: " + loadedWith, self, self.LOAD_CLASS, e)
            return None
    

    def loadClassBytesFromFile(self, name: str) -> list[int]:
        in_: FileInputStream = None
        cname: str = StringUtil.getInstance().EMPTY_STRING
        try:
            cname = str(AbeClassLoader.PATH) + name.replace('.', AbPathData.getInstance().SEPARATORCHAR) + self.ENCRYPTED_EXTENSION
            in_ = FileInputStream(cname)
            decrypted: list[int] = self.abCryptUtil.decrypt(in_, self.key)
            return decrypted
        except OSError as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.put("(Before LogBuffer Output) Failure loading Encrypted: " + name + " File: " + cname, "AbeClassLoader", "loadClassBytes", e)
            StreamUtil.getInstance().close(in_)
        except Exception as e:
            loadedWith: str = "loadClassBytes"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.put("(Before LogBuffer Output) Failed to Loaded Class: " + name + " File: " + cname + "\nwith: " + loadedWith, self, "loadClassBytes", e)
        except NoClassDefFoundError as e:
            loadedWith: str = "loadClassBytes"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.putF("(Before LogBuffer Output) NoClassDefFoundError Failed Loaded Class: " + name + " File: " + cname + "\nwith: " + loadedWith, self, "loadClassBytes")
        return None
    

    # throws ClassNotFoundException
    def oldLoadClass(self, name: str, resolve: bool) -> type:
        with self._lock:
            return self._oldLoadClass_unlocked(name, resolve)

    def _oldLoadClass_unlocked(self, name: str, resolve: bool) -> type:
        from org.allbinary.logic.system.loader.ClassNotFoundException import ClassNotFoundException
        from org.allbinary.logic.system.loader.ClassNotFoundException import ClassNotFoundException
        loadedWith: str = "findLoadedClass1"
        try:
            myClass: type = self.findLoadedClass1(name)
            if myClass is None:
                try:
                    loadedWith = "super.loadClass"
                    normalClass: type = super().loadClass(name, resolve)
                    if normalClass is not None:
                        return normalClass
                except ClassNotFoundException as e:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LOADER):
                        self.logUtil.putF("Failed Loaded Class: " + name + " with: " + loadedWith, self, self.LOAD_CLASS)
                except Exception as e:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LOADER):
                        self.logUtil.putF("Failed Loaded Class: " + name + " with: " + loadedWith, self, self.LOAD_CLASS)
                except NoClassDefFoundError as e:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LOADER):
                        self.logUtil.putF("Failed Loaded Class: " + name + " with: " + loadedWith, self, self.LOAD_CLASS)
                loadedWith = "loadClassBytes"
                classBytes: list[int] = self.loadClassBytesFromFile(name)
                if classBytes is None:
                    raise ClassNotFoundException("Bytes not loaded for: " + name)
                myClass = self.defineClass(name, classBytes, 0, len(classBytes))
                if myClass is None:
                    raise ClassNotFoundException("Class Not Defineable for: " + name)
                AbeClassLoader.classes.put(name, myClass)
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LOADER):
                    self.logUtil.putF("Already Loaded: " + name + " with: " + loadedWith, self, self.LOAD_CLASS)
            self.resolveClass(myClass)
            return myClass
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.put("Failure loading: " + name, "AbeClassLoader", self.LOAD_CLASS, e)
            return None
# from java.io.FileInputStream import FileInputStream
# from java.io.IOException import IOException
# from java.util.Map import Map
from org.allbinary.logic.communication.log.LogBuffer import LogBuffer
from org.allbinary.logic.communication.log.LogFactory import LogFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.AbCryptUtil import AbCryptUtil


