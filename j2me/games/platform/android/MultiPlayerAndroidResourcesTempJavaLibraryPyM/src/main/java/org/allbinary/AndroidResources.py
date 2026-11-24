# Generated Code Do Not Modify
# package org.allbinary

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class AndroidResources:
    instance: AndroidResources = None

    def _init_fields(self) -> None:
        from org.allbinary.game.testgamedemo.R import R
        self.drawable: drawable = drawable()
        self.id: id = id()
        self.layout: layout = layout()
        self.raw: raw = raw()
        self.string: string = string()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AndroidResources:
        return AndroidResources.instance
# from org.allbinary.game.testgamedemo.R import R


def _AndroidResources_instance() -> object:
    return AndroidResources()

lazy_static(AndroidResources, "instance", _AndroidResources_instance)

