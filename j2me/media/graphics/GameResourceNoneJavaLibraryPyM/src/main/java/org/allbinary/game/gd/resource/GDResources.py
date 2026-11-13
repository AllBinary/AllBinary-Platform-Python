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
# package org.allbinary.game.gd.resource

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class GDResources:
    instance: GDResources = None

    def _init_fields(self) -> None:
        self.resourceStringArray: list[str] = []
        self.currentLayoutRequiredTotal: int = 0

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GDResources:
        return GDResources.instance


def _GDResources_instance() -> object:
    return GDResources()

lazy_static(GDResources, "instance", _GDResources_instance)

