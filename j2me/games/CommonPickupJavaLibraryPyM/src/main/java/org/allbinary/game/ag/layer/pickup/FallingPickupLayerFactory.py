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
# package org.allbinary.game.ag.layer.pickup

from __future__ import annotations

from org.allbinary.layer.AllBinaryLayerFactoryInterface import AllBinaryLayerFactoryInterface


class FallingPickupLayerFactory(AllBinaryLayerFactoryInterface):
    

    # throws Exception
    def getInstance(self) -> AllBinaryLayer:
        from org.allbinary.game.ag.layer.pickup.FallingPickupLayer import FallingPickupLayer
        return FallingPickupLayer(RemoteInfo.REMOTE_INFO)
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


