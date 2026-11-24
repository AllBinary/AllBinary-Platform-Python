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
# package org.allbinary.init

from __future__ import annotations

from java.lang.ClassLoader import ClassLoader


class NoLicense:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def init(classLoader: ClassLoader, pathString: str) -> None:
        from org.allbinary.globals.Globals import Globals
        Globals.init(classLoader, pathString)
# from org.allbinary.globals.Globals import Globals


