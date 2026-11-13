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
# package org.allbinary.graphics.paint

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ProcessPaintableSingletonFactory:
    SINGLETON: ProcessPaintable = None
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> ProcessPaintable:
        return ProcessPaintableSingletonFactory.SINGLETON


def _ProcessPaintableSingletonFactory_SINGLETON() -> object:
    from org.allbinary.graphics.paint.ProcessPaintable import ProcessPaintable
    return ProcessPaintable()

lazy_static(ProcessPaintableSingletonFactory, "SINGLETON", _ProcessPaintableSingletonFactory_SINGLETON)

