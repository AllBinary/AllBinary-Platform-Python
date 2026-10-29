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



class KeySpecFactory:
    instance: KeySpecFactory = None

    def _init_fields(self) -> None:
        self.DES: str = "DES"
        self.DESEDE: str = "DESede"
        self.BLOWFISH: str = "Blowfish"
    

    @staticmethod
    def getInstance() -> KeySpecFactory:
        return KeySpecFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, algorithm: str, keyData: list[int]) -> KeySpec:
        try:
            tsUtil: TsUtil = TsUtil.getInstance()
            if ((algorithm > self.DES) - (algorithm < self.DES)) == 0:
                return DESKeySpec(keyData)
            elif ((algorithm > self.DESEDE) - (algorithm < self.DESEDE)) == 0:
                return DESedeKeySpec(keyData)
            else:
                raise RuntimeError()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.putOE(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            raise RuntimeError()
# from java.security.spec.KeySpec import KeySpec
# from javax.crypto.spec.DESKeySpec import DESKeySpec
# from javax.crypto.spec.DESedeKeySpec import DESedeKeySpec
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings


KeySpecFactory.instance = KeySpecFactory()

