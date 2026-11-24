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


class AuthenticationHelperFactory(TagHelperFactoryInterface):
    CLASSNAME: str = "admin.taghelpers.AuthenticationHelper"
    FACTORYNAME: str = "AuthenticationHelperFactory"
    

    def __init__(self) -> None:
        pass
    

    # throws LicensingException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j2_1(self, hashMap: HashMap, pageContext: PageContext) -> object:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        return HelperFactory.getInstance(AuthenticationHelperFactory.FACTORYNAME, AuthenticationHelperFactory.CLASSNAME, hashMap, pageContext)
    

    # throws LicensingException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j2_2(self, hashMap: HashMap, httpServletRequest: HttpServletRequest) -> object:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        return HelperFactory.getInstance(AuthenticationHelperFactory.FACTORYNAME, AuthenticationHelperFactory.CLASSNAME, hashMap, httpServletRequest)

    def getInstance(self, *args):
        if len(args) == 2 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)):
            return self.getInstance_j2_1(*args)
        if len(args) == 2:
            return self.getInstance_j2_2(*args)
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from javax.servlet.http.HttpServletRequest import HttpServletRequest


