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
# package org.allbinary.logic.string

from __future__ import annotations



class StringValidationJSEUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def isBlank(string: str) -> bool:
        len_: int = len(string)
        for i in range(0, len_):
            c: str = string[i]
            if c.isspace() == False:
                return False
        return True


