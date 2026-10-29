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
# package org.allbinary.logic.io

from __future__ import annotations



class BufferedWriterUtil:
    instance: BufferedWriterUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonLabels: CommonLabels = CommonLabels.getInstance()
        self.REMOVING_OLD: str = "Remove old for overwriting: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BufferedWriterUtil:
        return BufferedWriterUtil.instance
    

    # throws Exception
    def overwrite(self, path: str, data: str) -> None:
        abFile: AbFile = AbFile.createAbFile(path)
        if abFile.exists():
            self.logUtil.putF(self.REMOVING_OLD + path, self, self.commonStrings.CREATE)
            abFile.delete()
        else:
            name: str = AbPathData.getInstance().removeNameFromPath(path)
            abFileDirectory: AbFile = AbFile.createAbFile(name)
            if abFileDirectory.exists():
                pass
            else:
                stringBuilder: StringMaker = StringMaker()
                self.logUtil.putF(str(stringBuilder.append(self.commonStrings.CREATE).append(self.commonLabels.COLON_SEP).append(name)), self, self.commonStrings.CREATE)
                result: bool = abFileDirectory.mkdirs()
                stringBuilder.delete(0, stringBuilder.length())
                self.logUtil.putF(str(stringBuilder.append(self.commonLabels.RESULT_).appendboolean(result)), self, self.commonStrings.CREATE)
        self.write(abFile, data)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def overwrite(self, abFile: AbFile, data: str) -> None:
        if abFile.exists():
            self.logUtil.putF(self.REMOVING_OLD + str(abFile.getPath()), self, self.commonStrings.CREATE)
            abFile.delete()
        else:
            name: str = AbPathData.getInstance().removeNameFromPath(abFile.getAbsolutePath())
            abFileDirectory: AbFile = AbFile.createAbFile(name)
            if abFileDirectory.exists():
                pass
            else:
                stringBuilder: StringMaker = StringMaker()
                self.logUtil.putF(str(stringBuilder.append(self.commonStrings.CREATE).append(self.commonLabels.COLON_SEP).append(name)), self, self.commonStrings.CREATE)
                result: bool = abFileDirectory.mkdirs()
                stringBuilder.delete(0, stringBuilder.length())
                self.logUtil.putF(str(stringBuilder.append(self.commonLabels.RESULT_).appendboolean(result)), self, self.commonStrings.CREATE)
        self.write(abFile, data)
    

    # throws Exception
    def write(self, abFile: AbFile, data: str) -> None:
        fileOut: BufferedWriter = BufferedWriter(FileWriter(AbFileNativeUtil.get(abFile)))
        fileOut.write(data, 0, len(data))
        fileOut.newLine()
        fileOut.flush()
# from java.io.BufferedWriter import BufferedWriter
# from java.io.FileWriter import FileWriter
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings


BufferedWriterUtil.instance = BufferedWriterUtil()

