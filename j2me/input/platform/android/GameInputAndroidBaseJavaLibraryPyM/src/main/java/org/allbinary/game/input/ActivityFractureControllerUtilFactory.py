# Generated Code Do Not Modify
# package org.allbinary.game.input

from __future__ import annotations



class ActivityFractureControllerUtilFactory:
    

    @staticmethod
    def getInstance() -> AndroidKeyFactory:
        from org.allbinary.game.input.AndroidAPI12KeyFactory import AndroidAPI12KeyFactory
        from org.allbinary.game.input.AndroidAPI9KeyFactory import AndroidAPI9KeyFactory
        from org.allbinary.game.input.AndroidAPI1KeyFactory import AndroidAPI1KeyFactory
        SDK_VERSION: int = AndroidInfoFactory.getInstance().getVersion()
        if SDK_VERSION <= 8:
            return AndroidAPI1KeyFactory.getInstance()
        elif SDK_VERSION <= 11:
            return AndroidAPI9KeyFactory.getInstance()
        else:
            return AndroidAPI12KeyFactory.getAPI12Instance()
from org.allbinary.android.AndroidInfoFactory import AndroidInfoFactory


