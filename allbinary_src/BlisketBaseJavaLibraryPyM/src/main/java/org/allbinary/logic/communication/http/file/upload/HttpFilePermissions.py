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
# package org.allbinary.logic.communication.http.file.upload

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate


class HttpFilePermissions:

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "file" not in vars(self): self.file: AbFile = None
        self.userRoles: BasicArrayList = BasicArrayListD()
    

    def __init__(self, fullPath: AbPath) -> None:
        from org.allbinary.logic.communication.http.file.upload.FileUploadData import FileUploadData
        from org.allbinary.business.user.role.BasicUserRoleFactory import BasicUserRoleFactory
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        self.file = AbFile.createAbFileFromAbPath(AbPath(fullPath.toFileSystemString(), FileUploadData.getInstance().FILE))
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
            self.logUtil.putF("Loading Privileges: " + str(fullPath.toFileSystemString()), self, self.commonStrings.CONSTRUCTOR)
        if java_predicate(self, "isFile"):
            self.userRoles.add(BasicUserRoleFactory.getInstance().ADMINISTRATOR)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
            self.logUtil.putF("User Roles: " + str(self.userRoles), self, self.commonStrings.CONSTRUCTOR)
    

    def isFile(self) -> bool:
        return java_predicate(self.file, "isFile")
    

    def getUserRoles(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.userRoles
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.user.role.BasicUserRoleFactory import BasicUserRoleFactory
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


