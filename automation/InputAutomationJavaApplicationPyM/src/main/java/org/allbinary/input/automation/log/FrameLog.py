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
# package org.allbinary.input.automation.log

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class FrameLog:
    frameBytes: list[int] = None
    info: list[int] = None
    actions: list[int] = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.frame: int = None
        self.infoStringBuffer: StringMaker = StringMaker()
        self.actionsStringBuffer: StringMaker = StringMaker()
    

    def __init__(self, frame: int) -> None:
        self._init_fields()
        self.frame = frame
    

    def addInfo(self, infoString: str) -> None:
        self.infoStringBuffer.append(infoString)
    

    def addActions(self, vectorOfStrings: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        size: int = vectorOfStrings.size()
        for index in range(0, size):
            self.addAction(vectorOfStrings.get(index))
    

    def addAction(self, action: str) -> None:
        from org.allbinary.string.CommonSeps import CommonSeps
        self.actionsStringBuffer.append(action)
        self.actionsStringBuffer.append(CommonSeps.getInstance().NEW_LINE)
    

    # throws Exception
    def write(self) -> None:
        from java.io.FileOutputStream import FileOutputStream
        from org.allbinary.input.automation.ImageOutputData import ImageOutputData
        from org.allbinary.logic.java.number.LongUtil import LongUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        filePathStringBuffer: StringMaker = StringMaker()
        filePathStringBuffer.append(ImageOutputData.SAVE_PATH)
        filePathStringBuffer.append(LongUtil.fillIn(str(self.frame)))
        filePathStringBuffer.append(".txt")
        filePath: str = str(filePathStringBuffer)
        fileOutputStream: FileOutputStream = FileOutputStream(File(filePath))
        fileOutputStream.write(FrameLog.frameBytes)
        fileOutputStream.write(list(str(self.getFrame()).encode()))
        fileOutputStream.write('\n')
        fileOutputStream.write(FrameLog.info)
        fileOutputStream.write(list(str(self.infoStringBuffer).encode()))
        fileOutputStream.write('\n')
        fileOutputStream.write(FrameLog.actions)
        fileOutputStream.write(list(str(self.actionsStringBuffer).encode()))
        fileOutputStream.close()
    

    def getFrame(self) -> int:
        return self.frame
# from java.io.File import File
# from java.io.FileOutputStream import FileOutputStream
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.input.automation.ImageOutputData import ImageOutputData
# from org.allbinary.logic.java.number.LongUtil import LongUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps


def _FrameLog_frameBytes() -> object:
    return str("Frame: ").getBytes()

lazy_static(FrameLog, "frameBytes", _FrameLog_frameBytes)

def _FrameLog_info() -> object:
    return str("Info: \n").getBytes()

lazy_static(FrameLog, "info", _FrameLog_info)

def _FrameLog_actions() -> object:
    return str("Actions: \n").getBytes()

lazy_static(FrameLog, "actions", _FrameLog_actions)

