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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations



class LicenseServerInitFileUtil:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.NULL_OUTPUT_STREAM: OutputStream = SimpleFileUtil.nullOutputStream()

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self) -> None:
        try:
            filePath: str = LicenseInitInfoUtil.getInstance().INITFILENAME
            LicenseInitInfoUtil.getInstance().setFilePath(StringUtil.getInstance().EMPTY_STRING)
            if FileFactory.getInstance().isFile(filePath):
                self.logUtil.putF("Using Existing License File", self, self.commonStrings.INIT)
            else:
                self.write()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
    

    def write(self) -> None:
        fileOutputStream: OutputStream = self.NULL_OUTPUT_STREAM
        try:
            resourceUtil: ResourceUtil = ResourceUtil.getInstance()
            filePath: str = LicenseInitInfoUtil.getInstance().INITFILENAME
            inputStream: InputStream = resourceUtil.getResourceAsStream(filePath)
            self.logUtil.putF("Writing Default License File", self, self.commonStrings.INIT)
            fileStreamFactory: FileStreamFactory = FileStreamFactory.getInstance()
            fileOutputStream = fileStreamFactory.getFileOutputStreamInstance(StringUtil.getInstance().EMPTY_STRING, filePath)
            b: int = 0
            index: int = 0
            while True:
                b = inputStream.read()
                if b == -1:
                    break
                fileOutputStream.write(b)
                index += 1
            self.logUtil.putF("Wrote Bytes: " + str(index), self, self.commonStrings.INIT)
            fileOutputStream.flush()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
        finally:
            StreamUtil.getInstance().close(fileOutputStream)
# from java.io.InputStream import InputStream
# from java.io.OutputStream import OutputStream
from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.FileStreamFactory import FileStreamFactory
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.FileFactory import FileFactory
from org.allbinary.logic.io.file.SimpleFileUtil import SimpleFileUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


