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

from org.allbinary.logic.system.loader.NativeLibraryHelperWrapper import NativeLibraryHelperWrapper


class SecuredNativeLibraryHelperWrapper(NativeLibraryHelperWrapper):

    def _init_fields(self) -> None:
        self.securedNativeLibraryInterface: SecuredNativeLibraryInterface = None
    

    def __init__(self, securedNativeLibraryInterface: SecuredNativeLibraryInterface) -> None:
        super().__init__(securedNativeLibraryInterface.getLibraryName())
        self._init_fields()
        self.securedNativeLibraryInterface = securedNativeLibraryInterface
    

    # throws LicensingException
    def unlock(self, abeClientInformation: AbeClientInformationInterface) -> bool:
        return self.securedNativeLibraryInterface.unlock(AbKeys.getInstance().getKey(abeClientInformation, self.securedNativeLibraryInterface.getName()))
from org.allbinary.logic.system.security.AbKeys import AbKeys
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


