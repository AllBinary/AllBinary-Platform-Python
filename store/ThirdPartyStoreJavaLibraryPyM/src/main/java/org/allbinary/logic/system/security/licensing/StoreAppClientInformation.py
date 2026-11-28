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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.thirdparty.store.LongArrayIdentifierInterface import LongArrayIdentifierInterface
from org.allbinary.logic.system.security.licensing.AbeClientInformation import AbeClientInformation


@java_inherited_overloads
class StoreAppClientInformation(*java_bases(AbeClientInformation, LongArrayIdentifierInterface)):
    def _java_defaults(self):
        vars(self).setdefault("longArrayIdentifier", None)

    def _init_fields(self) -> None:
        if "longArrayIdentifier" not in vars(self): self.longArrayIdentifier: list[int] = None
    

    def __init__(self, name: str, version: str, specialName: str, shortName: str, longArrayIdentifier: list[int]) -> None:
        __class__._java_defaults(self)
        super().__init__(name, version, specialName, shortName)
        __class__._init_fields(self)
        self.longArrayIdentifier = longArrayIdentifier
    

    def getLongArrayIdentifier(self) -> list[int]:
        return self.longArrayIdentifier


