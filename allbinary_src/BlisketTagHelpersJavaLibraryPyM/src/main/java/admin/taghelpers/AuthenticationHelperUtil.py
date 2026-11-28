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

from java.lang.JavaRuntimeStatic import lazy_static


class AuthenticationHelperUtil:
    instance: AuthenticationHelperUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> AuthenticationHelperUtil:
        return AuthenticationHelperUtil.instance
    

    # throws Exception
    def isAuthorized(self, authenticationHelper: AuthenticationHelper, filePath: str) -> bool:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.business.user.role.BasicUserRole import BasicUserRole
        from org.allbinary.business.user.role.UserRole import UserRole
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.communication.http.file.upload.HttpFilePermissions import HttpFilePermissions
        from org.allbinary.logic.communication.http.request.HttpRequestUtil import HttpRequestUtil
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.string.CommonLabels import CommonLabels
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
            self.logUtil.putF(str(CommonLabels.getInstance().START) + filePath, self, "isAuthorized()")
        endIndex: int = HttpRequestUtil.getInstance().getLastSeparatorIndex(filePath)
        fullPath: AbPath = AbPath(str(URLGLOBALS.getWebappPath()) + filePath[0:endIndex], StringUtil.getInstance().EMPTY_STRING)
        downloadFilePermissions: HttpFilePermissions = HttpFilePermissions(fullPath)
        userRoles: BasicArrayList = downloadFilePermissions.getUserRoles()
        userRole: UserRole = authenticationHelper.getRole()
        basicUserRole: BasicUserRole = userRole.getBasicUserRole()
        if userRoles.contains(basicUserRole):
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Authorized", self, "isAuthorized()")
            return True
        else:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Not Authorized: " + str(basicUserRole), self, "isAuthorized()")
            return False
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.user.role.BasicUserRole import BasicUserRole
# from org.allbinary.business.user.role.UserRole import UserRole
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.http.file.upload.HttpFilePermissions import HttpFilePermissions
# from org.allbinary.logic.communication.http.request.HttpRequestUtil import HttpRequestUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _AuthenticationHelperUtil_instance() -> object:
    return AuthenticationHelperUtil()

lazy_static(AuthenticationHelperUtil, "instance", _AuthenticationHelperUtil_instance)

