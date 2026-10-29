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
# package org.allbinary.ai

from __future__ import annotations

from org.allbinary.graphics.IdentifierInterface import IdentifierInterface


# Java interface
class ArtificialIntelligenceInterface(IdentifierInterface):
    

    # throws Exception
    def processAI(self, layerManager: AllBinaryLayerManager) -> None:
        raise NotImplementedError()
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


