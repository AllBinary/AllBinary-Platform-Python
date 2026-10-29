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
# package org.allbinary.business.category.store.theme

from __future__ import annotations

# from java.util.Comparator import Comparator


class ThemeComparator(Comparator):
    

    def __init__(self) -> None:
        pass
    

    def compare(self, anyType: object, object2: object) -> int:
        string: str = anyType
        string2: str = object2
        return ((string > string2) - (string < string2))


