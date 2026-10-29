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
# package org.allbinary.bundle.logic.preloader

from __future__ import annotations

from org.osgi.framework.BundleActivator import BundleActivator


class AllBinaryPreloaderActivator(BundleActivator):
    context: BundleContext = None
    CRYPT_REGISTRY_NAME: str = "bundle.abcs.logic.system.loader.CryptService"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getBundleContext() -> BundleContext:
        return AllBinaryPreloaderActivator.context
    

    # throws Exception
    def start(self, context: BundleContext) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, "start")
            AllBinaryPreloaderActivator.context = context
            self.registerAsService()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "start", e)
            raise e
    

    # throws Exception
    def registerAsService(self) -> None:
        properties: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        serviceRegistration: ServiceRegistration = AllBinaryPreloaderActivator.context.registerService(AllBinaryPreloaderActivator.CRYPT_REGISTRY_NAME, CryptServiceFactory(), properties)
        serviceReference: ServiceReference = serviceRegistration.getReference()
        serviceReference = AllBinaryPreloaderActivator.context.getServiceReference(AllBinaryPreloaderActivator.CRYPT_REGISTRY_NAME)
        if serviceReference is None:
            raise Exception("No Such Service Reference")
    

    # throws Exception
    def stop(self, context: BundleContext) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "stop")
from org.osgi.framework.BundleContext import BundleContext
from org.osgi.framework.ServiceReference import ServiceReference
from org.osgi.framework.ServiceRegistration import ServiceRegistration
from org.allbinary.bundle.logic.system.loader.CryptServiceFactory import CryptServiceFactory
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable


