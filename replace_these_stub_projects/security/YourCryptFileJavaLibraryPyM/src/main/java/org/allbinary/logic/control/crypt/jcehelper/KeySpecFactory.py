# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
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
# package org.allbinary.logic.control.crypt.jcehelper

from __future__ import annotations



class KeySpecFactory:
    DES: str = "DES"
    DESEDE: str = "DESede"
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance(algorithm: str, keyData: list[int]) -> KeySpec:
        return None
# from java.security.spec.KeySpec import KeySpec


