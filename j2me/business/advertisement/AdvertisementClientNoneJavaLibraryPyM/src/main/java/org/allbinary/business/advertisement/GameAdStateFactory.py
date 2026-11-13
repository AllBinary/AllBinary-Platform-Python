# Generated Code Do Not Modify
# package org.allbinary.business.advertisement

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.business.advertisement.GameAdStateFactoryInterface import GameAdStateFactoryInterface


class GameAdStateFactory(GameAdStateFactoryInterface):
    instance: GameAdStateFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.game.GameAdState import GameAdState
        self.gameAdStateArray: list[GameAdState] = [GameAdState(AppNameLicensingAdConfiguration())]
        self.gameAdState: GameAdState = self.gameAdStateArray[0]

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameAdStateFactory:
        return GameAdStateFactory.instance
    

    def getCurrentInstance(self) -> GameAdState:
        from org.allbinary.game.GameAdState import GameAdState
        return self.gameAdState
    

    # throws Exception
    def getInstanceForApp(self, softwareInformation: SoftwareInformation) -> GameAdStateBase:
        from org.allbinary.logic.system.SoftwareInformation import SoftwareInformation
        self.gameAdState = self.gameAdStateArray[0]
        return self.gameAdStateArray[0]
    

    def isEnabled(self) -> bool:
        return False
# from org.allbinary.game.GameAdState import GameAdState
# from org.allbinary.logic.system.SoftwareInformation import SoftwareInformation
from org.allbinary.business.advertisement.AppNameLicensingAdConfiguration import AppNameLicensingAdConfiguration


def _GameAdStateFactory_instance() -> object:
    return GameAdStateFactory()

lazy_static(GameAdStateFactory, "instance", _GameAdStateFactory_instance)

