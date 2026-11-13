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
# package org.allbinary.animation.transition.shake

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.animation.transition.shake.ShakeAnimationListener import ShakeAnimationListener


class NoShakeAnimationListener(ShakeAnimationListener):
    NO_SHAKE_ANIMATION_LISTENER: ShakeAnimationListener = None

    def __init__(self) -> None:
        super().__init__()


def _NoShakeAnimationListener_NO_SHAKE_ANIMATION_LISTENER() -> object:
    return NoShakeAnimationListener()

lazy_static(NoShakeAnimationListener, "NO_SHAKE_ANIMATION_LISTENER", _NoShakeAnimationListener_NO_SHAKE_ANIMATION_LISTENER)

