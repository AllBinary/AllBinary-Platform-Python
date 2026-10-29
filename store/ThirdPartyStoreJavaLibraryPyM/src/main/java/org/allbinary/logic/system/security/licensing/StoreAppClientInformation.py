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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations

from org.allbinary.thirdparty.store.LongArrayIdentifierInterface import LongArrayIdentifierInterface
from org.allbinary.logic.system.security.licensing.AbeClientInformation import AbeClientInformation


class StoreAppClientInformation(AbeClientInformation, LongArrayIdentifierInterface):

    def _init_fields(self) -> None:
        self.longArrayIdentifier: list[int] = None
    

    def __init__(self, name: str, version: str, specialName: str, shortName: str, longArrayIdentifier: list[int]) -> None:
        super().__init__(name, version, specialName, shortName)
        self._init_fields()
        self.longArrayIdentifier = longArrayIdentifier
    

    def getLongArrayIdentifier(self) -> list[int]:
        return self.longArrayIdentifier


