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


class BasicCrypt(CryptInterface):

    def _init_fields(self) -> None:
        self.byteUtil: ByteUtil = ByteUtil.getInstance()
        self.key: list[int] = None
    

    def __init__(self, keyAsString: str) -> None:
        self._init_fields()
        key: list[int] = NullUtil.getInstance().NULL_BYTE_ARRAY
        try:
            key = TsUtil.getInstance().getByteArray(keyAsString)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putOE(commonStrings.EXCEPTION, self, "AbCrypt(alg,key)", e)
        self.key = key
    

    def encrypt(self, array: list[int]) -> list[int]:
        try:
            return self.mutilate(array)
        except Exception as e:
            PreLogUtil.putOE("Encrypt Failed", self, "encrypt", e)
            return NullUtil.getInstance().NULL_BYTE_ARRAY
    

    def decrypt(self, array: list[int]) -> list[int]:
        try:
            return self.mutilate(array)
        except Exception as e:
            PreLogUtil.putOE("decrypt Failed", self, "decrypt", e)
            return NullUtil.getInstance().NULL_BYTE_ARRAY
    

    def mutilate(self, array: list[int]) -> list[int]:
        value: int = 0
        for index in range(0, len(self.key)):
            value = self.key[index]
            array = self.byteUtil.xor(array, value)
        return array
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.java.byteutil.ByteUtil import ByteUtil
from org.allbinary.string.CommonStrings import CommonStrings


