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
# package org.allbinary.business.user.modules.admin.configuration

from __future__ import annotations

import threading
from org.allbinary.business.user.modules.admin.configuration.AdminConfigurationInterface import AdminConfigurationInterface


class AdminConfiguration(AdminConfigurationInterface):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "contextConfigurationInterface" not in vars(self): self.contextConfigurationInterface: ContextConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "HttpServletRequest" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor0(self) -> None:
        from org.allbinary.business.user.modules.admin.configuration.AdminConfigurationData import AdminConfigurationData
        from org.allbinary.business.context.configuration.ContextConfigurationInterfaceFactory import ContextConfigurationInterfaceFactory
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.contextConfigurationInterface = ContextConfigurationInterfaceFactory.getInstance().getInstance(AdminConfigurationData.CONTEXTNAME)
    

    def _constructor1_1(self, request: HttpServletRequest) -> None:
        from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.getFormData(RequestParams(request).toHashMap())
    

    def _constructor1_2(self, storeHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.getFormData(storeHashMap)
    

    # throws Exception
    def getFormData(self, storeHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.configuration.ContextConfiguration import ContextConfiguration
        from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
        self.logUtil.putF(self.commonStrings.START, self, "getFormData")
        self.setContextConfigurationInterface(ContextConfiguration(storeHashMap))
    

    # throws Exception
    def write(self) -> None:
        with self._lock:
            return __class__.__dict__["_write_unlocked"].__get__(self, __class__)()

    def _write_unlocked(self) -> None:
        from org.allbinary.business.user.modules.admin.configuration.AdminConfigurationData import AdminConfigurationData
        from org.allbinary.business.context.configuration.ContextConfigurationData import ContextConfigurationData
        from org.allbinary.business.context.configuration.ContextConfigurationDomDocumentMapping import ContextConfigurationDomDocumentMapping
        from org.allbinary.business.context.configuration.ContextConfigurationPathUtil import ContextConfigurationPathUtil
        from org.allbinary.logic.control.crypt.file.CryptFileWriter import CryptFileWriter
        contextConfigurationDomDocumentMapping: ContextConfigurationDomDocumentMapping = ContextConfigurationDomDocumentMapping(self.getContextConfigurationInterface())
        cryptFileWriter: CryptFileWriter = CryptFileWriter(ContextConfigurationData.getInstance().UNCRYPTED_EXTENSION, ContextConfigurationData.getInstance().ENCRYPTED_EXTENSION)
        cryptFileWriter.write(ContextConfigurationPathUtil.getAbPath(AdminConfigurationData.CONTEXTNAME), contextConfigurationDomDocumentMapping.toXmlDoc())
    

    def getContextConfigurationInterface(self) -> ContextConfigurationInterface:
        from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
        return self.contextConfigurationInterface
    

    def setContextConfigurationInterface(self, contextConfigurationInterface: ContextConfigurationInterface) -> None:
        from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
        self.contextConfigurationInterface = contextConfigurationInterface
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.business.context.configuration.ContextConfiguration import ContextConfiguration
# from org.allbinary.business.context.configuration.ContextConfigurationData import ContextConfigurationData
# from org.allbinary.business.context.configuration.ContextConfigurationDomDocumentMapping import ContextConfigurationDomDocumentMapping
# from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface
# from org.allbinary.business.context.configuration.ContextConfigurationInterfaceFactory import ContextConfigurationInterfaceFactory
# from org.allbinary.business.context.configuration.ContextConfigurationPathUtil import ContextConfigurationPathUtil
# from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.crypt.file.CryptFileWriter import CryptFileWriter
# from org.allbinary.string.CommonStrings import CommonStrings


