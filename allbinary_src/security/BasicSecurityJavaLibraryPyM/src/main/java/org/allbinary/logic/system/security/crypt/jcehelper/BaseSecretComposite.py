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



class BaseSecretComposite:
    NULL_SECRET_COMPOSITE: BaseSecretComposite = None
    

    # throws Exception
    def encrypt(self, array: list[int]) -> list[int]:
        return NullUtil.getInstance().NULL_BYTE_ARRAY
    

    # throws Exception
    def decrypt(self, array: list[int]) -> list[int]:
        return NullUtil.getInstance().NULL_BYTE_ARRAY
from org.allbinary.logic.NullUtil import NullUtil


BaseSecretComposite.NULL_SECRET_COMPOSITE = BaseSecretComposite()

