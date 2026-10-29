# Generated Code Do Not Modify
# package org.allbinary

from __future__ import annotations



class AndroidResources:
    instance: AndroidResources = None

    def _init_fields(self) -> None:
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
from org.allbinary.game.testgamedemo.R import R


AndroidResources.instance = AndroidResources()

