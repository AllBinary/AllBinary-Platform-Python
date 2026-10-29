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
# package dynamic

from __future__ import annotations



class NativeLibraryHelper:

    def _init_fields(self) -> None:
        self.library: str = None
    

    def __init__(self, library: str) -> None:
        self._init_fields()
        self.library = library
    

    def load(self) -> None:
        System.loadLibrary(self.library)


