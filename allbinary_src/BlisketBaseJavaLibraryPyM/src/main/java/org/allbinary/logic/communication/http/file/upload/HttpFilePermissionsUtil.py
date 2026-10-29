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



class HttpFilePermissionsUtil:
    instance: HttpFilePermissionsUtil = None
    

    @staticmethod
    def getInstance() -> HttpFilePermissionsUtil:
        return HttpFilePermissionsUtil.instance
    

    # throws Exception
    def create(self, path: AbPath) -> None:
        file: AbFile = AbFile.createAbFileFromAbPath(path)
        if not file.isFile():
            file.createNewFile()
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.path.AbPath import AbPath


HttpFilePermissionsUtil.instance = HttpFilePermissionsUtil()

