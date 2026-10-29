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
# package org.allbinary.osgi.service

from __future__ import annotations



class InputAutomationServiceConsumer:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.osgiServiceUtil: OSGIServiceUtil = OSGIServiceUtil.getInstance()
        self.registryName: str = None
        self.bundleContext: BundleContext = None
        self.osgiServiceVisitorInterface: OSGIServiceVisitorInterface = None
    

    def __init__(self, registryName: str, bundleContext: BundleContext, osgiServiceVisitorInterface: OSGIServiceVisitorInterface) -> None:
        self._init_fields()
        self.setRegistryName(registryName)
        self.setBundleContext(bundleContext)
        self.setOsgiServiceVisitorInterface(osgiServiceVisitorInterface)
    

    # throws Exception
    def process(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.PROCESS)
        vector: BasicArrayList = self.osgiServiceUtil.getServicesObjectVector(self.getBundleContext(), self.getServiceReferences())
        self.logUtil.putF("Processing " + str(vector.size()) + " Services", self, self.commonStrings.PROCESS)
        size: int = vector.size()
        osgiServiceInterface: OSGIServiceInterface = None
        for index in range(0, size):
            osgiServiceInterface = vector.get(index)
            if not self.getOsgiServiceVisitorInterface().visit(osgiServiceInterface):
                raise Exception("Unable to process service: " + str(osgiServiceInterface))
    

    # throws Exception
    def getServiceReferences(self) -> list[ServiceReference]:
        return self.getBundleContext().getServiceReferences(self.getRegistryName(), None)
    

    def getBundleContext(self) -> BundleContext:
        return self.bundleContext
    

    def setBundleContext(self, aBundleContext: BundleContext) -> None:
        self.bundleContext = aBundleContext
    

    def getRegistryName(self) -> str:
        return self.registryName
    

    def setRegistryName(self, registryName: str) -> None:
        self.registryName = registryName
    

    def getOsgiServiceVisitorInterface(self) -> OSGIServiceVisitorInterface:
        return self.osgiServiceVisitorInterface
    

    def setOsgiServiceVisitorInterface(self, osgiServiceVisitorInterface: OSGIServiceVisitorInterface) -> None:
        self.osgiServiceVisitorInterface = osgiServiceVisitorInterface
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.osgi.framework.BundleContext import BundleContext
from org.osgi.framework.ServiceReference import ServiceReference
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.osgi.OSGIServiceInterface import OSGIServiceInterface
from org.allbinary.osgi.OSGIServiceVisitorInterface import OSGIServiceVisitorInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.osgi.service.OSGIServiceUtil import OSGIServiceUtil


