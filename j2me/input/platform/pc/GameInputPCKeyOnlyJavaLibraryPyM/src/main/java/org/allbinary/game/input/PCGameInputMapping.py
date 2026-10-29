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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.game.input.mapping.PersistentInputMapping import PersistentInputMapping


class PCGameInputMapping(PersistentInputMapping):
    

    def __init__(self) -> None:
        super().__init__(GamePersistanceStrings.getInstance().SAVED_INPUT_CONFIGURATION_RECORD_ID)
    

    # throws Exception
    def init(self, abeClientInformation: AbeClientInformationInterface) -> None:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.INIT)
        PCKeyFactory.getInstance()
        super().init(abeClientInformation)
        if self.getTotalMapped() == 0 or self.isDefaultNew():
            self.getInputMapping().addMapping(self.getDefault())
            self.save(abeClientInformation)
    

    def isDelete(self, input: Input) -> bool:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        if input == PCKeyFactory.getInstance().DEL:
            return True
        else:
            return False
    

    def isSystemInput(self, input: Input) -> bool:
        return False
from org.allbinary.game.configuration.persistance.GamePersistanceStrings import GamePersistanceStrings
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


