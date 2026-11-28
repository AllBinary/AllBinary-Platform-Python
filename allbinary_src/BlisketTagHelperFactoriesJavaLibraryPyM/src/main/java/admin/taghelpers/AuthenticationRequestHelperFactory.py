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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from admin.taghelpers.TagHelperFactory import TagHelperFactory


@java_inherited_overloads
class AuthenticationRequestHelperFactory(TagHelperFactory):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    # throws LicensingException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j2_1(self, hashMap: HashMap, pageContext: PageContext) -> object:
        from admin.taghelpers.AuthenticationRequestHelper import AuthenticationRequestHelper
        from java.util.HashMap import HashMap
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return AuthenticationRequestHelper(hashMap, pageContext)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.GET_INSTANCE, e)
            return None
    

    # throws LicensingException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j2_2(self, hashMap: HashMap, httpServletRequest: HttpServletRequest) -> object:
        from admin.taghelpers.AuthenticationRequestHelper import AuthenticationRequestHelper
        from java.util.HashMap import HashMap
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return AuthenticationRequestHelper(hashMap, httpServletRequest)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.GET_INSTANCE, e)
            return None

    def getInstance(self, *args):
        if len(args) == 2 and True and not isinstance(args[0], (str, list, int, float)) and (args[1] is None or any(base.__name__ == "PageContext" for base in type(args[1]).__mro__)):
            return __class__.__dict__["getInstance_j2_1"].__get__(self, __class__)(*args)
        if len(args) == 2:
            return __class__.__dict__["getInstance_j2_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


