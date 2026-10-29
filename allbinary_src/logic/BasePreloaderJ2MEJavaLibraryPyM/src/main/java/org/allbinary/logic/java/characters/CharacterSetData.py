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
# package org.allbinary.logic.java.characters

from __future__ import annotations



class CharacterSetData:
    instance: CharacterSetData = None

    def _init_fields(self) -> None:
        self.US_ASCII: str = "US-ASCII"
        self.ISO_8859_1: str = "ISO-8859-1"
        self.UTF_8: str = "UTF-8"
        self.UTF_16: str = "UTF-16"
        self.UTF_16BE: str = "UTF-16BE"
        self.UTF_16LE: str = "UTF-16LE"
    

    @staticmethod
    def getInstance() -> CharacterSetData:
        return CharacterSetData.instance
    

    def __init__(self) -> None:
        self._init_fields()


CharacterSetData.instance = CharacterSetData()

