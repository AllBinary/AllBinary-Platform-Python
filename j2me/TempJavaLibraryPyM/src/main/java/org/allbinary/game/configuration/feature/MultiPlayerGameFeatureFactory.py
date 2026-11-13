# Generated Code Do Not Modify
# package org.allbinary.game.configuration.feature

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class MultiPlayerGameFeatureFactory:
    instance: MultiPlayerGameFeatureFactory = None
    

    @staticmethod
    def getInstance() -> MultiPlayerGameFeatureFactory:
        return MultiPlayerGameFeatureFactory.instance
    

    def __init__(self) -> None:
        pass
    

    def addCommands(self, anyType: object) -> None:
        pass


def _MultiPlayerGameFeatureFactory_instance() -> object:
    return MultiPlayerGameFeatureFactory()

lazy_static(MultiPlayerGameFeatureFactory, "instance", _MultiPlayerGameFeatureFactory_instance)

