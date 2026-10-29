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
# package taghelpers

from __future__ import annotations



class OrderHistoryHelperFactory:
    CLASSNAME: str = "taghelpers.OrderHistoryHelper"
    FACTORYNAME: str = "taghelpers.OrderHistoryHelperFactory"
    

    def __init__(self) -> None:
        pass
    

    # throws LicensingException
    @staticmethod
    def getInstance(hashMap: dict, pageContext: PageContext) -> object:
        return HelperFactory.getInstance(OrderHistoryHelperFactory.FACTORYNAME, OrderHistoryHelperFactory.CLASSNAME, hashMap, pageContext)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from admin.taghelpers.HelperFactory import HelperFactory


