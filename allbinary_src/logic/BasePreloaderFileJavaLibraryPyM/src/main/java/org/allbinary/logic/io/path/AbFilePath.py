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
# package org.allbinary.logic.io.path

from __future__ import annotations

from org.allbinary.logic.io.path.AbPath import AbPath


class AbFilePath(AbPath):
    

    def __init__(self, aPath: str) -> None:
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.io.path.PathUtil import PathUtil
        super().__init__(StringUtil.getInstance().EMPTY_STRING, StringUtil.getInstance().EMPTY_STRING)
        pathData: AbPathData = AbPathData.getInstance()
        abPathUtil: PathUtil = PathUtil.getInstance()
        self.schema = self.getSchema(aPath)
        self.setName(pathData.getNameFromPath(aPath))
        self.setPath(abPathUtil.adjust(self.getPathFromPath(str(abPathUtil.removeNameFromPath(aPath)))))
from org.allbinary.logic.string.StringUtil import StringUtil


