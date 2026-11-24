# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.osgi.framework

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class NullServiceReferenceFactory:
    instance: NullServiceReferenceFactory = None

    def _init_fields(self) -> None:
        self.NULL_SERVICE_REFERENCE: NullServiceReference = NullServiceReference()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> NullServiceReferenceFactory:
        return NullServiceReferenceFactory.instance
from org.osgi.framework.NullServiceReference import NullServiceReference


def _NullServiceReferenceFactory_instance() -> object:
    return NullServiceReferenceFactory()

lazy_static(NullServiceReferenceFactory, "instance", _NullServiceReferenceFactory_instance)

