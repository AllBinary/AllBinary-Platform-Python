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
# package org.allbinary.logic.system.security

from __future__ import annotations



class AbCryptUtil:
    instance: AbCryptUtil = None

    def _init_fields(self) -> None:
        self.streamUtil: StreamUtil = StreamUtil.getInstance()
    

    @staticmethod
    def getInstance() -> AbCryptUtil:
        return AbCryptUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def decrypt(self, inputStream: InputStream, key: str) -> list[int]:
        outputStream: ByteArrayOutputStream = None
        try:
            outputStream = self.streamUtil.get(inputStream, ByteArrayOutputStream(), [0] * (16384))
            abCrypt: AbCrypt = AbCrypt(KeySpecFactory.getInstance().DESEDE)
            abCrypt.init(key)
            return abCrypt.decrypt(outputStream.toByteArray())
        finally:
            self.streamUtil.close(outputStream)
            self.streamUtil.close(inputStream)
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.InputStream import InputStream
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.system.security.crypt.jcehelper.AbCrypt import AbCrypt
from org.allbinary.logic.system.security.crypt.jcehelper.KeySpecFactory import KeySpecFactory


AbCryptUtil.instance = AbCryptUtil()

