# Generated Code Do Not Modify
# package org.allbinary.graphics.form

from __future__ import annotations



class ScreenInfo:
    instance: ScreenInfo = None

    def _init_fields(self) -> None:
        self.SMALL_WIDTH: int = 320
        self.SMALL_HEIGHT: int = 240
        self.MEDIUM_WIDTH: int = 800
        self.MEDIUM_HEIGHT: int = 600

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ScreenInfo:
        return ScreenInfo.instance


ScreenInfo.instance = ScreenInfo()

