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
# package org.allbinary.logic.math

from __future__ import annotations



class J2SEMath:
    instance: J2SEMath = None
    

    @staticmethod
    def getInstance() -> J2SEMath:
        return J2SEMath.instance
    

    def round(self, value: float) -> int:
        return int(value)
    

    def abs(self, value: float) -> float:
        return (-value if (value < 0.0) else value)
    

    def absdouble(self, value: float) -> float:
        return (-value if (value < 0.0) else value)


J2SEMath.instance = J2SEMath()

