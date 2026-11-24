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

from java.lang.JavaRuntimeStatic import lazy_static


class LicenseInterfaceSingleton:
    licenseInterface: AbeLicenseInterface = None
    

    @staticmethod
    def getInstance() -> AbeLicenseInterface:
        return LicenseInterfaceSingleton.licenseInterface
    

    @staticmethod
    def init(licenseInterface: AbeLicenseInterface) -> None:
        if licenseInterface is not None:
            LicenseInterfaceSingleton.licenseInterface = licenseInterface


def _LicenseInterfaceSingleton_licenseInterface() -> object:
    from org.allbinary.logic.system.security.licensing.AbeNoLicense import AbeNoLicense
    return AbeNoLicense.getInstance()

lazy_static(LicenseInterfaceSingleton, "licenseInterface", _LicenseInterfaceSingleton_licenseInterface)

