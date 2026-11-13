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
# package org.allbinary.input.motion.button

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class NoButtonsTouchInputFactory:
    instance: BaseTouchInput = None
    

    @staticmethod
    def getInstance() -> BaseTouchInput:
        return NoButtonsTouchInputFactory.instance


def _NoButtonsTouchInputFactory_instance() -> object:
    from org.allbinary.input.motion.button.BaseTouchInput import BaseTouchInput
    return BaseTouchInput()

lazy_static(NoButtonsTouchInputFactory, "instance", _NoButtonsTouchInputFactory_instance)

