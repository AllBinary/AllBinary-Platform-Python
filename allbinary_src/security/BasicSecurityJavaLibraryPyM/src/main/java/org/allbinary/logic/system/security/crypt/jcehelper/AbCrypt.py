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


class AbCrypt(CryptInterface):

    def _init_fields(self) -> None:
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.secretComposite: BaseSecretComposite = BaseSecretComposite.NULL_SECRET_COMPOSITE
        self.algorithm: str = None
    

    def __init__(self, algorithm: str) -> None:
        self._init_fields()
        self.algorithm = algorithm
    

    def init(self, keyAsString: str) -> None:
        from org.allbinary.logic.system.security.crypt.jcehelper.KeySpecFactory import KeySpecFactory
        from org.allbinary.logic.system.security.crypt.jcehelper.SecretComposite import SecretComposite
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            try:
                Security.addProvider(BouncyCastleProvider())
            except Exception as e:
                PreLogUtil.putOE(commonStrings.EXCEPTION, self, commonStrings.INIT, e)
            key: list[int] = self.tsUtil.getByteArray(keyAsString)
            keySpec: KeySpec = KeySpecFactory.getInstance().getInstance(self.algorithm, key)
            keyFactory: SecretKeyFactory = SecretKeyFactory.getInstance(self.algorithm)
            secretKey: SecretKey = keyFactory.generateSecret(keySpec)
            cipher: Cipher = Cipher.getInstance(self.algorithm)
            self.secretComposite = SecretComposite(secretKey, cipher, key)
        except Exception as e:
            PreLogUtil.putOE("init Failed", self, commonStrings.INIT, e)
    

    def encrypt(self, array: list[int]) -> list[int]:
        try:
            return self.secretComposite.encrypt(array)
        except Exception as e:
            PreLogUtil.putOE("Encrypt Failed", self, "encrypt", e)
            return NullUtil.getInstance().NULL_BYTE_ARRAY
    

    def decrypt(self, array: list[int]) -> list[int]:
        try:
            return self.secretComposite.decrypt(array)
        except Exception as e:
            PreLogUtil.putOE("decrypt Failed", self, "decrypt", e)
            return NullUtil.getInstance().NULL_BYTE_ARRAY
# from java.security.Security import Security
# from java.security.spec.KeySpec import KeySpec
# from javax.crypto.Cipher import Cipher
# from javax.crypto.SecretKey import SecretKey
# from javax.crypto.SecretKeyFactory import SecretKeyFactory
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.bouncycastle.jce.provider.BouncyCastleProvider import BouncyCastleProvider
from org.allbinary.logic.system.security.crypt.jcehelper.BaseSecretComposite import BaseSecretComposite


