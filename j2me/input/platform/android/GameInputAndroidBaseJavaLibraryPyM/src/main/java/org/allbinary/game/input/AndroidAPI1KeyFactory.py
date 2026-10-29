# Generated Code Do Not Modify
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.game.input.AndroidKeyFactory import AndroidKeyFactory


class AndroidAPI1KeyFactory(AndroidKeyFactory):
    instance: object = NullUtil.getInstance().NULL_OBJECT
    

    @staticmethod
    def getInstance() -> AndroidAPI1KeyFactory:
        if AndroidAPI1KeyFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            AndroidAPI1KeyFactory.instance = AndroidAPI1KeyFactory()
        return AndroidAPI1KeyFactory.instance
    

    def __init__(self) -> None:
        super().__init__()


