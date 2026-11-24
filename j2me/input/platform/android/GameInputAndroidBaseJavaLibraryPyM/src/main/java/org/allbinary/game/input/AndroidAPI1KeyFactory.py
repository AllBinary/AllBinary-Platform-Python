# Generated Code Do Not Modify
# package org.allbinary.game.input

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.input.AndroidKeyFactory import AndroidKeyFactory


class AndroidAPI1KeyFactory(AndroidKeyFactory):
    instance: object = None
    

    @staticmethod
    def getInstance() -> AndroidAPI1KeyFactory:
        from org.allbinary.logic.NullUtil import NullUtil
        if AndroidAPI1KeyFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            AndroidAPI1KeyFactory.instance = AndroidAPI1KeyFactory()
        return AndroidAPI1KeyFactory.instance
    

    def __init__(self) -> None:
        super().__init__()
# from org.allbinary.logic.NullUtil import NullUtil


def _AndroidAPI1KeyFactory_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(AndroidAPI1KeyFactory, "instance", _AndroidAPI1KeyFactory_instance)

