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


class ServiceClientInformationInterfaceFactory:
    instance: TestClientInformation = None
    

    @staticmethod
    def getInstance() -> AbeClientInformationInterface:
        return ServiceClientInformationInterfaceFactory.instance


def _ServiceClientInformationInterfaceFactory_instance() -> object:
    from org.allbinary.logic.system.security.licensing.TestClientInformation import TestClientInformation
    return TestClientInformation()

lazy_static(ServiceClientInformationInterfaceFactory, "instance", _ServiceClientInformationInterfaceFactory_instance)

