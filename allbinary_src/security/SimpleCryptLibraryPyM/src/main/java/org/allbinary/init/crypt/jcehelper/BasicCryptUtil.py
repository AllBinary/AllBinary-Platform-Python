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
# package org.allbinary.init.crypt.jcehelper

from __future__ import annotations



class BasicCryptUtil:
    instance: BasicCryptUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.XML_START: str = "<?xml"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicCryptUtil:
        return BasicCryptUtil.instance
    

    # throws Exception
    def getDecryptedInputStream(self, inputStream: InputStream, cryptInterface: CryptInterface) -> InputStream:
        buffer: ByteArrayOutputStream = ByteArrayOutputStream()
        ch: int = 0
        while True:
            ch = inputStream.read()
            if ch == -1:
                break
            buffer.write(ch)
        decrypted: list[int] = cryptInterface.decrypt(buffer.toByteArray())
        decryptedString: str = bytes(decrypted).decode()
        index: int = decryptedString.find(self.XML_START)
        if index > 0:
            decryptedString = decryptedString[index:]
        return ByteArrayInputStream(self.tsUtil.getByteArray(decryptedString))
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.InputStream import InputStream
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil


BasicCryptUtil.instance = BasicCryptUtil()

