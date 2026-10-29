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
# package org.allbinary.animation.transition

from __future__ import annotations

from org.allbinary.animation.transition.AnimationListenerInterface import AnimationListenerInterface


class RunAtEndAnimationListener(AnimationListenerInterface):

    def _init_fields(self) -> None:
        self.runnable: object = None
    

    def __init__(self, runnable: object) -> None:
        self._init_fields()
        self.runnable = runnable
    

    def onPlatformAnimationStart(self) -> None:
        pass
    

    def onPlatformAnimationEnd(self) -> None:
        pass
    

    def onPlatformAnimationRepeat(self) -> None:
        pass


