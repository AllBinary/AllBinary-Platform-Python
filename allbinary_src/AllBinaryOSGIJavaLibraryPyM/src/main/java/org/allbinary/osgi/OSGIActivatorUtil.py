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
# package org.allbinary.osgi

from __future__ import annotations



class OSGIActivatorUtil:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def registerAsService(bundleContext: BundleContext, anyType: object, serviceName: str) -> None:
        OSGIActivatorUtil.registerAsService(bundleContext, anyType, serviceName, StdUtil.getInstance().createHashtable())
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def registerAsService(bundleContext: BundleContext, anyType: object, serviceName: str, properties: ABHashtable[object, object]) -> None:
        serviceRegistration: ServiceRegistration = bundleContext.registerService(serviceName, anyType, properties)
        serviceReference: ServiceReference = serviceRegistration.getReference()
        serviceReference = bundleContext.getServiceReference(serviceName)
        if serviceReference == NullServiceReferenceFactory.getInstance().NULL_SERVICE_REFERENCE:
            raise Exception("No Such Service Reference")
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.osgi.framework.BundleContext import BundleContext
from org.osgi.framework.NullServiceReferenceFactory import NullServiceReferenceFactory
from org.osgi.framework.ServiceReference import ServiceReference
from org.osgi.framework.ServiceRegistration import ServiceRegistration


