# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.logic.system.security.crypt.jcehelper

from __future__ import annotations

from org.allbinary.logic.system.security.crypt.jcehelper.BaseSecretComposite import BaseSecretComposite


class SecretComposite(BaseSecretComposite):

    def _init_fields(self) -> None:
        self.byteUtil: ByteUtil = ByteUtil.getInstance()
        self.cipher: Cipher = None
        self.secretKey: SecretKey = None
        self.key: list[int] = None
    

    def __init__(self, secretKey: SecretKey, cipher: Cipher, key: list[int]) -> None:
        super().__init__()
        self._init_fields()
        self.secretKey = secretKey
        self.cipher = cipher
        self.key = key
    

    # throws Exception
    def encrypt(self, array: list[int]) -> list[int]:
        array = self.mutilate(array)
        self.cipher.init(Cipher.ENCRYPT_MODE, self.secretKey)
        return self.cipher.doFinal(array)
    

    # throws Exception
    def decrypt(self, array: list[int]) -> list[int]:
        self.cipher.init(Cipher.DECRYPT_MODE, self.secretKey)
        return self.mutilate(self.cipher.doFinal(array))
    

    def mutilate(self, array: list[int]) -> list[int]:
        for index in range(0, len(self.key)):
            value: int = self.key[index]
            if value < 8 and value > 0:
                array = self.byteUtil.xorByte(array, value)
        return array
# from javax.crypto.Cipher import Cipher
# from javax.crypto.SecretKey import SecretKey
from org.allbinary.logic.java.byteutil.ByteUtil import ByteUtil


