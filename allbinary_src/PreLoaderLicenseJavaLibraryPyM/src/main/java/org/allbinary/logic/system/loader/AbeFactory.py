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
from java.lang.ClassLoader import ClassLoader
from java.lang.JavaRuntimeStatic import lazy_static


class AbeFactory:
    instance: AbeFactory = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.useCustomLoader: bool = False
    

    @staticmethod
    def getInstance_j0() -> AbeFactory:
        return AbeFactory.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws LicensingException
    def getInstance_j2(self, abeClientInformation: AbeClientInformationInterface, className: str) -> object:
        with self._lock:
            return __class__.__dict__["_getInstance_j2_unlocked"].__get__(self, __class__)(abeClientInformation, className)

    def _getInstance_j2_unlocked(self, abeClientInformation: AbeClientInformationInterface, className: str) -> object:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return self.getClass(abeClientInformation, className).newInstance()
        except LicensingException as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.put("Failure for: " + className, self, "getInstance(classname)", e)
            raise e
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.put("Failure for: " + className, self, "getInstance(classname)", e)
            return None
    

    # throws LicensingException
    def getInstance_j4(self, abeClientInformation: AbeClientInformationInterface, className: str, classes: list[type], params: list[object]) -> object:
        with self._lock:
            return __class__.__dict__["_getInstance_j4_unlocked"].__get__(self, __class__)(abeClientInformation, className, classes, params)

    def _getInstance_j4_unlocked(self, abeClientInformation: AbeClientInformationInterface, className: str, classes: list[type], params: list[object]) -> object:
        from org.allbinary.logic.system.loader.WebappClassLoaderInfo import WebappClassLoaderInfo
        from org.allbinary.logic.system.loader.AbeClassLoader import AbeClassLoader
        from org.allbinary.logic.java.anyType.ConstructorUtil import ConstructorUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.system.security.AbKeys import AbKeys
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        constructor: Constructor = None
        try:
            parent: ClassLoader = WebappClassLoaderInfo.getLoader()
            if self.useCustomLoader:
                loader: ClassLoader = AbeClassLoader(parent, AbKeys.getInstance().getKey(abeClientInformation, className))
                myClass: type = loader.loadClass(className)
                constructor = myClass.getConstructor(classes)
                return constructor.newInstance(params)
            else:
                myClass: type = parent.loadClass(className)
                constructor = myClass.getConstructor(classes)
                return constructor.newInstance(params)
        except LicensingException as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Failure for: ")
                stringBuffer.append(className)
                stringBuffer.append(CommonSeps.getInstance().SPACE)
                stringBuffer.append(ConstructorUtil.view(constructor, CommonSeps.getInstance().NEW_LINE))
                self.logUtil.put(str(stringBuffer), self, "getInstance(className,params)", e)
            raise e
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Failure for: ")
                stringBuffer.append(className)
                stringBuffer.append(CommonSeps.getInstance().SPACE)
                stringBuffer.append(ConstructorUtil.view(constructor, CommonSeps.getInstance().NEW_LINE))
                self.logUtil.put(str(stringBuffer), self, "getInstance(className,params)", e)
            return None

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
    

    # throws LicensingException
    def getClass(self, abeClientInformation: AbeClientInformationInterface, className: str) -> type:
        with self._lock:
            return __class__.__dict__["_getClass_unlocked"].__get__(self, __class__)(abeClientInformation, className)

    def _getClass_unlocked(self, abeClientInformation: AbeClientInformationInterface, className: str) -> type:
        from org.allbinary.logic.system.loader.WebappClassLoaderInfo import WebappClassLoaderInfo
        from org.allbinary.logic.system.loader.AbeClassLoader import AbeClassLoader
        from org.allbinary.logic.system.security.AbKeys import AbKeys
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            parent: ClassLoader = WebappClassLoaderInfo.getLoader()
            if self.useCustomLoader:
                loader: ClassLoader = AbeClassLoader(parent, AbKeys.getInstance().getKey(abeClientInformation, className))
                c: type = loader.loadClass(className)
                return c
            else:
                c: type = parent.loadClass(className)
                return c
        except LicensingException as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.put("Failure for: " + className, self, "getClass(className)", e)
            raise e
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LOADERERROR):
                self.logUtil.put("Failure for: " + className, self, "getClass(className)", e)
            return None
# from java.lang.reflect.Constructor import Constructor
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.anyType.ConstructorUtil import ConstructorUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.system.security.AbKeys import AbKeys
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _AbeFactory_instance() -> object:
    return AbeFactory()

lazy_static(AbeFactory, "instance", _AbeFactory_instance)

