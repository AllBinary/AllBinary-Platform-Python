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
# package org.allbinary.logic.system.loader

from __future__ import annotations

from org.allbinary.logic.system.loader.ClassLoader import ClassLoader


class NativeLibraryClassLoader(ClassLoader):

    def _init_fields(self) -> None:
        self.message: str = "This Class Loader Does Not Load Classes - Only For Loading and Unloading of Native Libraries"
    

    def __init__(self, parent: ClassLoader) -> None:
        super().__init__(parent)
        self._init_fields()


