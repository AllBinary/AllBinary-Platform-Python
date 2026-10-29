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



class OSGIServiceUtil:
    instance: OSGIServiceUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> OSGIServiceUtil:
        return OSGIServiceUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getServicesObjectVector(self, bundleContext: BundleContext, serviceReferences: list[ServiceReference]) -> BasicArrayList:
        vector: BasicArrayList = BasicArrayListD()
        if serviceReferences is not None:
            size: int = len(serviceReferences)
            self.logUtil.putF("Service References: " + str(size), self, "getServicesObjectVector")
            for index in range(0, size):
                serviceReference: ServiceReference = serviceReferences[index]
                if serviceReference is not None:
                    osgiServiceInterface: OSGIServiceInterface = bundleContext.getService(serviceReference)
                    if osgiServiceInterface is None:
                        raise Exception("No Service For Reference")
                    vector.add(osgiServiceInterface)
        return vector
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.osgi.framework.BundleContext import BundleContext
from org.osgi.framework.ServiceReference import ServiceReference
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.osgi.OSGIServiceInterface import OSGIServiceInterface


OSGIServiceUtil.instance = OSGIServiceUtil()

