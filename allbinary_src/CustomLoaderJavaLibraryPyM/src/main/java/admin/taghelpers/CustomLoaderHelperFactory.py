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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface


class CustomLoaderHelperFactory(TagHelperFactoryInterface):
    CLASSNAME: str = "admin.taghelpers.CustomLoaderHelper"
    FACTORYNAME: str = "CustomLoaderHelperFactory"
    

    def __init__(self) -> None:
        pass
    

    # throws LicensingException
    def getInstance(self, hashMap: dict, pageContext: PageContext) -> object:
        from admin.taghelpers.HelperFactory import HelperFactory
        abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        return HelperFactory.getInstance(abeClientInformation, CustomLoaderHelperFactory.FACTORYNAME, CustomLoaderHelperFactory.CLASSNAME, hashMap, pageContext)
    

    # throws LicensingException
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface) -> object:
        from admin.taghelpers.HelperFactory import HelperFactory
        return HelperFactory.getInstance(abeClientInformation, CustomLoaderHelperFactory.FACTORYNAME, CustomLoaderHelperFactory.CLASSNAME)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory


