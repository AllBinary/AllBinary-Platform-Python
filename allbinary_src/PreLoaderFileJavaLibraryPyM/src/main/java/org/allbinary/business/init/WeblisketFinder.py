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
# package org.allbinary.business.init

from __future__ import annotations



class WeblisketFinder:
    instance: WeblisketFinder = None
    KEY: str = "installerdata.dat"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.subDirectory: SubDirectory = SubDirectory.getInstance()
    

    @staticmethod
    def getInstance() -> WeblisketFinder:
        return WeblisketFinder.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def findAll(self, path: str) -> BasicArrayList:
        try:
            self.logUtil.putF(self.commonStrings.START, self, "findAll")
            return self.subDirectory.search(WeblisketFinder.KEY, AbFile.createAbFile(path))
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "findAll", e)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "findAll", e)
            return None
    

    def getInstallationPath(self, file: AbFile) -> str:
        try:
            filePath: str = file.getPath()
            end: int = filePath.find(WeblisketFinder.KEY)
            if end < 0:
                return None
            return filePath[0:end]
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PRELOADERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstallationPath", e)
            return None
    

    # throws Exception
    @staticmethod
    def main(args: list[str]) -> None:
        stringUtil: StringUtil = StringUtil.getInstance()
        vector: BasicArrayList = WeblisketFinder.getInstance().findAll(stringUtil.EMPTY_STRING)
        print(vector.size())
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.directory.SubDirectory import SubDirectory
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


WeblisketFinder.instance = WeblisketFinder()

