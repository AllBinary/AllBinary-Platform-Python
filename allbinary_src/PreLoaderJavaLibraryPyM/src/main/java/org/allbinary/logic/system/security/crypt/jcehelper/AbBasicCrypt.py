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
# package org.allbinary.logic.system.security.crypt.jcehelper

from __future__ import annotations

from org.allbinary.init.crypt.jcehelper.CryptInterface import CryptInterface


class AbBasicCrypt(CryptInterface):

    def _init_fields(self) -> None:
        self.cipher: Cipher = None
        self.secretKey: SecretKey = None
        self.algorithm: str = None
        self.key: list[int] = None
    

    def __init__(self, algorithm: str, key: str) -> None:
        self._init_fields()
        try:
            self.algorithm = algorithm
            self.key = key.getBytes()
            self.init()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putOE(commonStrings.EXCEPTION, self, "AbCrypt(alg,key)", e)
    

    def init(self) -> None:
        from org.allbinary.logic.system.security.crypt.jcehelper.SunJCE import SunJCE
        from org.allbinary.logic.system.security.crypt.jcehelper.KeySpecFactory import KeySpecFactory
        try:
            sunJce: Provider = SunJCE()
            Security.addProvider(sunJce)
            keySpec: KeySpec = KeySpecFactory.getInstance().getInstance(self.algorithm, self.key)
            keyFactory: SecretKeyFactory = SecretKeyFactory.getInstance(self.algorithm)
            self.secretKey = keyFactory.generateSecret(keySpec)
            self.cipher = Cipher.getInstance(self.algorithm)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putOE("init Failed", self, commonStrings.INIT, e)
    

    def encrypt(self, array: list[int]) -> list[int]:
        try:
            self.cipher.init(Cipher.ENCRYPT_MODE, self.secretKey)
            ivArray: list[int] = self.secretKey.getEncoded()
            encrypted: list[int] = self.cipher.doFinal(array)
            result: list[int] = [0] * (len(ivArray) + len(encrypted))
            PreLogUtil.put("ivArray Length: " + str(len(ivArray)), self, "encrypt")
            for index in range(0, len(ivArray)):
                result[index] = ivArray[index]
            for index in range(0, len(encrypted)):
                result[index + len(ivArray)] = encrypted[index]
            return result
        except Exception as e:
            PreLogUtil.putOE("Encrypt Failed", self, "encrypt", e)
            return None
    

    def decrypt(self, array: list[int]) -> list[int]:
        try:
            self.cipher.init(Cipher.DECRYPT_MODE, self.secretKey)
            ivArray: list[int] = [0] * (8)
            for index in range(0, 8):
                ivArray[index] = array[index]
            PreLogUtil.put("ivArray Length: " + str(len(ivArray)), self, "encrypt")
            result: list[int] = [0] * (len(array) - len(ivArray))
            for index in range(len(ivArray), len(array)):
                result[index - len(ivArray)] = array[index]
            decrypted: list[int] = self.cipher.doFinal(result)
            return result
        except Exception as e:
            PreLogUtil.putOE("decrypt Failed", self, "decrypt", e)
            return None
# from java.security.Provider import Provider
# from java.security.Security import Security
# from java.security.spec.KeySpec import KeySpec
# from javax.crypto.Cipher import Cipher
# from javax.crypto.SecretKey import SecretKey
# from javax.crypto.SecretKeyFactory import SecretKeyFactory
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings


