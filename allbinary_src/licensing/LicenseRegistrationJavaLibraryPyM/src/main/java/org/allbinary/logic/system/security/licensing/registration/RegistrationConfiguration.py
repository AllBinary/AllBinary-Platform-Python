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
# package org.allbinary.logic.system.security.licensing.registration

from __future__ import annotations



class RegistrationConfiguration:
    SINGLETON: RegistrationConfiguration = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.registrationCode: str = "No Registration Code"
        self.NAME: str = "registrationid"
        self.FILE: str = "Registration.dat"
    

    def __init__(self) -> None:
        self._init_fields()
        try:
            if FileFactory.getInstance().isFile(self.FILE):
                self.read()
            else:
                self.write()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
    

    @staticmethod
    def getInstance() -> RegistrationConfiguration:
        return RegistrationConfiguration.SINGLETON
    

    # throws Exception
    def read(self) -> None:
        fileInputStreamFactory: FileStreamFactory = FileStreamFactory.getInstance()
        fileInputStream: InputStream = fileInputStreamFactory.getFileInputStreamInstance(StringUtil.getInstance().EMPTY_STRING, self.FILE)
        dataInputStream: DataInputStream = DataInputStream(fileInputStream)
        self.setRegistrationCode(dataInputStream.readUTF())
        PreLogUtil.put(str(StringMaker().append("Read Configuration: ").append(str(self))), self, "read")
    

    # throws Exception
    def write(self) -> None:
        dataOutputStream: AbDataOutputStream = None
        try:
            self.logUtil.putF(str(StringMaker().append("Write Configuration: ").append(str(self))), self, "write")
            fileInputStreamFactory: FileStreamFactory = FileStreamFactory.getInstance()
            fileOutputStream: OutputStream = fileInputStreamFactory.getFileOutputStreamInstance(StringUtil.getInstance().EMPTY_STRING, self.FILE)
            dataOutputStream = AbDataOutputStream(fileOutputStream)
            dataOutputStream.writeUTF(self.getRegistrationCode())
            dataOutputStream.flush()
        finally:
            StreamUtil.getInstance().close(dataOutputStream)
    

    def toString(self) -> str:
        return str(StringMaker().append("Registration Code: ").append(self.getRegistrationCode()))

    def __str__(self) -> str:
        return self.toString()
    

    def setRegistrationCode(self, registrationCode: str) -> None:
        self.registrationCode = registrationCode
    

    def getRegistrationCode(self) -> str:
        return self.registrationCode
# from java.io.DataInputStream import DataInputStream
# from java.io.InputStream import InputStream
# from java.io.OutputStream import OutputStream
from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
from org.allbinary.logic.io.FileStreamFactory import FileStreamFactory
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.FileFactory import FileFactory
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil


RegistrationConfiguration.SINGLETON = RegistrationConfiguration()

