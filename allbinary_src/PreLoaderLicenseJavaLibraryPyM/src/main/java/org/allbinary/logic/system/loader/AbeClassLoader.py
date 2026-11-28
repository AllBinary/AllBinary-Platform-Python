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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.ClassLoader import ClassLoader
from java.lang.JavaRuntimeStatic import lazy_static


@java_inherited_overloads
class AbeClassLoader(ClassLoader):
    classes: Map = None
    PATH: str = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("abCryptUtil", None)
        vars(self).setdefault("LOAD_CLASS", None)
        vars(self).setdefault("ENCRYPTED_EXTENSION", None)
        vars(self).setdefault("key", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.system.security.AbCryptUtil import AbCryptUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abCryptUtil: AbCryptUtil = AbCryptUtil.getInstance()
        self.LOAD_CLASS: str = "loadClass"
        self.ENCRYPTED_EXTENSION: str = str(AbPathData.getInstance().EXTENSION_SEP) + "abc"
        if "key" not in vars(self): self.key: str = None
    

    def __init__(self, parent: ClassLoader, key: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        super().__init__(parent)
        __class__._init_fields(self)
        self.key = key
        AbeClassLoader.PATH = str(URLGLOBALS.getWebappPath()) + "WEB-INF/classes/"
    

    def findLoadedClass1(self, name: str) -> type:
        return AbeClassLoader.classes.get(name)
    

    # throws ClassNotFoundException
    def loadClass_j1(self, name: str) -> type:
        with self._lock:
            return __class__.__dict__["_loadClass_j1_unlocked"].__get__(self, __class__)(name)

    def _loadClass_j1_unlocked(self, name: str) -> type:
        return self.loadClass(name, False)
    

    # throws ClassNotFoundException
    def loadClass_j2(self, name: str, resolve: bool) -> type:
        with self._lock:
            return __class__.__dict__["_loadClass_j2_unlocked"].__get__(self, __class__)(name, resolve)

    def _loadClass_j2_unlocked(self, name: str, resolve: bool) -> type:
        from org.allbinary.logic.communication.log.LogBuffer import LogBuffer
        from org.allbinary.logic.communication.log.LogFactory import LogFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        loadedWith: str = "findLoadedClass1"
        logBuffer: LogBuffer = LogBuffer()
        try:
            myClass: type = self.findLoadedClass1(name)
            if myClass is None:
                try:
                    loadedWith = "super.loadClass"
                    normalClass: type = java_super_call(super(), "loadClass", name, resolve)
                    if normalClass is not None:
                        return normalClass
                except ImportError as e:
                    logBuffer.add(LogFactory.getInstance("Failed to Load Class: " + name + "\nwith: " + loadedWith, self, self.LOAD_CLASS, e))
                except Exception as e:
                    logBuffer.add(LogFactory.getInstance("Failed to Load Class: " + name + "\nwith: " + loadedWith, self, self.LOAD_CLASS, e))
                except RuntimeError as e:
                    logBuffer.add(LogFactory.getInstanceF("NoClassDefFoundError Failed Loaded Class: " + name + "\nwith: " + loadedWith, self, self.LOAD_CLASS))
                classBytes: list[int] = self.loadClassBytesFromFile(name)
                if classBytes is None:
                    raise ImportError("My Bytes not loaded for: " + name + "\nwith: " + "loadClassBytes")
                myClass = self.defineClass(name, classBytes, 0, len(classBytes))
                if myClass is None:
                    raise ImportError("My Class Not Defineable for: " + name + "\nwith: " + "loadClassBytes")
                AbeClassLoader.classes.put(name, myClass)
            else:
                logBuffer.add(LogFactory.getInstanceF("Already Loaded: " + name + "\nwith: " + loadedWith, self, self.LOAD_CLASS))
            self.resolveClass(myClass)
            return myClass
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                logBuffer.logAll()
                self.logUtil.put("Failure loading: " + name + "\nwith: " + loadedWith, self, self.LOAD_CLASS, e)
            return None

    def loadClass(self, *args):
        implementation = __class__.__dict__.get("loadClass_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().loadClass(*args)
    

    def loadClassBytesFromFile(self, name: str) -> list[int]:
        from java.io.FileInputStream import FileInputStream
        from org.allbinary.logic.io.StreamUtil import StreamUtil
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        in_: FileInputStream = None
        cname: str = StringUtil.getInstance().EMPTY_STRING
        try:
            cname = str(AbeClassLoader.PATH) + name.replace('.', AbPathData.getInstance().SEPARATORCHAR) + self.ENCRYPTED_EXTENSION
            in_ = FileInputStream(cname)
            decrypted: list[int] = self.abCryptUtil.decrypt(in_, self.key)
            return decrypted
        except OSError as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.put("(Before LogBuffer Output) Failure loading Encrypted: " + name + " File: " + cname, "AbeClassLoader", "loadClassBytes", e)
            StreamUtil.getInstance().close(in_)
        except Exception as e:
            loadedWith: str = "loadClassBytes"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.put("(Before LogBuffer Output) Failed to Loaded Class: " + name + " File: " + cname + "\nwith: " + loadedWith, self, "loadClassBytes", e)
        except RuntimeError as e:
            loadedWith: str = "loadClassBytes"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.putF("(Before LogBuffer Output) NoClassDefFoundError Failed Loaded Class: " + name + " File: " + cname + "\nwith: " + loadedWith, self, "loadClassBytes")
        return None
    

    # throws ClassNotFoundException
    def oldLoadClass(self, name: str, resolve: bool) -> type:
        with self._lock:
            return __class__.__dict__["_oldLoadClass_unlocked"].__get__(self, __class__)(name, resolve)

    def _oldLoadClass_unlocked(self, name: str, resolve: bool) -> type:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        loadedWith: str = "findLoadedClass1"
        try:
            myClass: type = self.findLoadedClass1(name)
            if myClass is None:
                try:
                    loadedWith = "super.loadClass"
                    normalClass: type = java_super_call(super(), "loadClass", name, resolve)
                    if normalClass is not None:
                        return normalClass
                except ImportError as e:
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADER):
                        self.logUtil.putF("Failed Loaded Class: " + name + " with: " + loadedWith, self, self.LOAD_CLASS)
                except Exception as e:
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADER):
                        self.logUtil.putF("Failed Loaded Class: " + name + " with: " + loadedWith, self, self.LOAD_CLASS)
                except RuntimeError as e:
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADER):
                        self.logUtil.putF("Failed Loaded Class: " + name + " with: " + loadedWith, self, self.LOAD_CLASS)
                loadedWith = "loadClassBytes"
                classBytes: list[int] = self.loadClassBytesFromFile(name)
                if classBytes is None:
                    raise ImportError("Bytes not loaded for: " + name)
                myClass = self.defineClass(name, classBytes, 0, len(classBytes))
                if myClass is None:
                    raise ImportError("Class Not Defineable for: " + name)
                AbeClassLoader.classes.put(name, myClass)
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADER):
                    self.logUtil.putF("Already Loaded: " + name + " with: " + loadedWith, self, self.LOAD_CLASS)
            self.resolveClass(myClass)
            return myClass
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.put("Failure loading: " + name, "AbeClassLoader", self.LOAD_CLASS, e)
            return None
# from java.io.FileInputStream import FileInputStream
# from java.io.IOException import IOException
# from java.util.Map import Map
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogBuffer import LogBuffer
# from org.allbinary.logic.communication.log.LogFactory import LogFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.StreamUtil import StreamUtil
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.system.security.AbCryptUtil import AbCryptUtil
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _AbeClassLoader_classes() -> object:
    from java.util.Map import Map
    from org.allbinary.logic.StdUtil import StdUtil
    return StdUtil.getInstance().createHashMap()

lazy_static(AbeClassLoader, "classes", _AbeClassLoader_classes)

