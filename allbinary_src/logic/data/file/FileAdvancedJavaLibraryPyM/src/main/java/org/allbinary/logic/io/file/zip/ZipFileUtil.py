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
# package org.allbinary.logic.io.file.zip

from __future__ import annotations



class ZipFileUtil:
    instance: ZipFileUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ZipFileUtil:
        return ZipFileUtil.instance
    

    def create(self, outFilename: str, fileBasicArrayList: BasicArrayList) -> None:
        try:
            zipFile: AbFile = AbFile.createAbFile(outFilename)
            if zipFile.exists():
                zipFile.delete()
            zipFile.createNewFile()
            outputStream: ZipOutputStream = ZipOutputStream(AbFileOutputStream.createFromAbFile(zipFile))
            streamUtil: StreamUtil = StreamUtil.getInstance()
            stringBuffer: StringMaker = StringMaker()
            byteArray: list[int] = [0] * (16384)
            fileInputStream: AbFileInputStream = None
            size: int = fileBasicArrayList.size()
            current: int = 0
            for i in range(0, size):
                file: AbFile = fileBasicArrayList.get(i)
                if file.isDirectory():
                    pass
                elif file.isFile():
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.appendint(current)
                    stringBuffer.append(" Creating Zip File Entry: ")
                    stringBuffer.append(file.getPath())
                    self.logUtil.putF(str(stringBuffer), self, "create()")
                    try:
                        fileInputStream = AbFileInputStream(file)
                        outputStream.putNextEntry(ZipEntry(file.getPath()))
                        streamUtil.get(fileInputStream, outputStream, byteArray)
                        outputStream.closeEntry()
                        streamUtil.close(fileInputStream)
                    except Exception as e:
                        self.logUtil.putF("Skipping File (Probably Local): " + str(file.getPath()), self, "create()")
                current += 1
            streamUtil.close(outputStream)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "create", e)
    

    # throws Exception
    def unzip(self, path: str, zipFile: AbFile, fileName: str) -> None:
        buffer: list[int] = [0] * (16384)
        inputStream: ZipInputStream = None
        try:
            inputStream = ZipInputStream(AbFileInputStream(zipFile))
            zipEntry: ZipEntry = None
            stringBuffer: StringMaker = StringMaker()
            fileUtil: FileUtil = FileUtil.getInstance()
            while ((zipEntry := inputStream.getNextEntry())) is not None:
                entryName: str = zipEntry.getName()
                if zipEntry.isDirectory():
                    pass
                else:
                    entryFile: AbFile = AbFile.createAbFile(path + entryName)
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append("ZipEntry Name: ")
                    stringBuffer.append(entryName)
                    stringBuffer.append(" isFile: ")
                    stringBuffer.appendboolean(entryFile.isFile())
                    stringBuffer.append(" isDirectory: ")
                    stringBuffer.appendboolean(entryFile.isDirectory())
                    stringBuffer.append(" getParent: ")
                    stringBuffer.append(entryFile.getParent())
                    self.logUtil.putF(str(stringBuffer), self, "unzip")
                    dataOutputStream: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(entryFile)
                    fileUtil.write(inputStream, dataOutputStream, buffer)
                inputStream.closeEntry()
        finally:
            StreamUtil.getInstance().close(inputStream)
# from java.util.zip.ZipEntry import ZipEntry
# from java.util.zip.ZipInputStream import ZipInputStream
# from java.util.zip.ZipOutputStream import ZipOutputStream
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FileUtil import FileUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


ZipFileUtil.instance = ZipFileUtil()

