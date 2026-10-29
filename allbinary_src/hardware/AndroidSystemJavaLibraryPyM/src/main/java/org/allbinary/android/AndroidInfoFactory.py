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
# package org.allbinary.android

from __future__ import annotations



class AndroidInfoFactory:
    instance: AndroidInfoFactory = None

    def _init_fields(self) -> None:
        self.version: int = int(Build.VERSION.SDK)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AndroidInfoFactory:
        return AndroidInfoFactory.instance
    

    def getVersion(self) -> int:
        return self.version
from android.os.Build import Build


AndroidInfoFactory.instance = AndroidInfoFactory()

